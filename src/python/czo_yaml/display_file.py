#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import re
import os
import argparse
import string
import logging
import yaml
import genson
import json
from urllib2 import urlopen
import json
from jsonschema import validate, ValidationError, SchemaError,Draft4Validator,ErrorTree
from string import Formatter
from yaml import SafeDumper
import yaml.constructor

try:
    # included in standard lib from Python 2.7
    from collections import OrderedDict
except ImportError:
    # try importing the backported drop-in replacement
    # it's available on PyPI
    from ordereddict import OrderedDict

logging.basicConfig(level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

filelogger = logging.FileHandler('yaml2json.log',  mode='w',) # using w to truncate. Use a to append.
filelogger.setFormatter(logging.Formatter('\n%(message)s'))
logger = logging.getLogger('')
logger.addHandler(console)
logger.addHandler(filelogger)

def display_file():
    pass

def df_validate(args ):

    level = args.level

    validation_log =["validation starting"]
    stream = file(args.source)

    ymal_data = yaml.load (stream)

    validation_log.append("level 0: File valid JSON or YAML")
    if (level > 0 ):
        schema = file(args.schema)
        json_schema = json.load(schema)
        validation_log.append("Starting Level 2")
        try:
            v = Draft4Validator(json_schema)
            errors = v.iter_errors(ymal_data)
            # building an ErrorTree fails.
            # Means we can't use ErrorTree to get a count or provide more details.
            #   possibly to do  Space in KeyName?.
            #tree = ErrorTree(errors)
            #tree = ErrorTree(v.iter_errors(ymal_data))
            errorList =  list(sorted(errors, key=lambda e: e.path))

           #if (tree.total_errors==0 ) :
            if (len(errorList) == 0):
                logger.info('Level 2 validation; File valid to Display File Structural Specification')
                return

            #for error in tree.errors:
            for error in errorList:
                logger.info ('in iterated errors')
                logger.warn (  error.message + ' in ' +
                "/".join( [ str(element) for element in error.path ] )
                )
        except ValidationError as e:
            logger.info ('in validation error')
            logger.warn(e.message)
        except SchemaError as e:
            logger.error(e)


    pass

def construct_tuple(loader, node):
  return tuple(yaml.SafeLoader.construct_sequence(loader, node))

def represent_odict(dump, tag, mapping, flow_style=None):
    """Like BaseRepresenter.represent_mapping, but does not issue the sort().
    """
    value = []
    node = yaml.MappingNode(tag, value, flow_style=flow_style)
    if dump.alias_key is not None:
        dump.represented_objects[dump.alias_key] = node
    best_style = True
    if hasattr(mapping, 'items'):
        mapping = mapping.items()
    for item_key, item_value in mapping:
        node_key = dump.represent_data(item_key)
        node_value = dump.represent_data(item_value)
        if not (isinstance(node_key, yaml.ScalarNode) and not node_key.style):
            best_style = False
        if not (isinstance(node_value, yaml.ScalarNode) and not node_value.style):
            best_style = False
        value.append((node_key, node_value))
    if flow_style is None:
        if dump.default_flow_style is not None:
            node.flow_style = dump.default_flow_style
        else:
            node.flow_style = best_style
    return node



# frem https://gist.github.com/enaeseth/844388
class OrderedDictYAMLLoader(yaml.Loader):
    """
    A YAML loader that loads mappings into ordered dictionaries.
    """

    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

        self.add_constructor(u'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(u'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    def construct_yaml_map(self, node):
        data = OrderedDict()
        yield data
        value = self.construct_mapping(node)
        data.update(value)

    def construct_mapping(self, node, deep=False):
        if isinstance(node, yaml.MappingNode):
            self.flatten_mapping(node)
        else:
            raise yaml.constructor.ConstructorError(None, None,
                'expected a mapping node, but found %s' % node.id, node.start_mark)

        mapping = OrderedDict()
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                hash(key)
            except TypeError, exc:
                raise yaml.constructor.ConstructorError('while constructing a mapping',
                    node.start_mark, 'found unacceptable key (%s)' % exc, key_node.start_mark)
            value = self.construct_object(value_node, deep=deep)
            mapping[key] = value
        return mapping
def convert(args ):
    stream = file(args.source)

    # yaml.SafeLoader.add_constructor(u'tag:yaml.org,2002:seq', construct_tuple)
    # yaml.SafeDumper.add_representer(OrderedDict,
    #     lambda dumper, value: represent_odict(dumper, u'tag:yaml.org,2002:map', value))
    #yaml.SafeLoader.add_constructor(u'tag:yaml.org,2002:seq', construct_tuple)
    yaml.SafeDumper.add_representer(OrderedDict,
        lambda dumper, value: represent_odict(dumper, u'tag:yaml.org,2002:map', value))

    ymal_data = yaml.load(stream,Loader=OrderedDictYAMLLoader)

    logger.info( ymal_data )

    if (args.format == 'json'):
        # indent forces pretty print
        json_schema = json.dumps(ymal_data,indent=4,sort_keys=False)
        logger.info(json_schema)
        with open(args.output, 'w') as json_schema_file:
                json_schema_file.write(json_schema)

    if (args.format == 'yaml'):
        # indent forces pretty print
        yaml_schema = yaml.dump(ymal_data, Dumper=SafeDumper)
        #yaml_schema = yaml.dump(ymal_data)
        logger.info(yaml_schema)
        with open(args.output, 'w') as yaml_schema_file:
                yaml_schema_file.write(yaml_schema)

    # trying to dump objects one at a time to generate some oerdering at the top level
    if (args.format == 'hydroprofile'):
        # indent forces pretty print
        yaml_schema = yaml.dump(ymal_data, Dumper=SafeDumper)
        logger.info(yaml_schema)
        with open(args.output, 'w') as yaml_schema_file:
                yaml_schema_file.write(yaml_schema)
    pass

class CzoDisplayFile(yaml.YAMLObject):
    yaml_tag = u'CZO Display File'

def main():
    parser = argparse.ArgumentParser()

    default_parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_json = subparsers.add_parser('format', parents=[default_parser])
    parser_json.add_argument('format',choices=['json', 'yaml', 'hydroprofile'], help='json  file output path')
    parser_json.add_argument('source', type=str, help='json or yaml file')
    parser_json.add_argument('output', type=str, help='json or yaml file')
    parser_json.set_defaults(func=convert)

    parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    parser_validate.add_argument('source', type=str, help='json or yaml file')
    parser_validate.add_argument('schema',default='schema/df2_schema.json',nargs='?', help='schema to use to validate. default=')
    parser_validate.add_argument('level',choices=[0, 1],default=1,nargs='?', help='level of validation')
    parser_validate.set_defaults(func=df_validate)

    # parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    # parser_validate.add_argument('json_schema_file_path', type=str, help='json schema file path')
    # parser_validate.set_defaults(func=validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()