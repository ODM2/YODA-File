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

def convert(args ):
    stream = file(args.source)
    ymal_data = yaml.load (stream)

    logger.info( ymal_data )

    if (args.format == 'json'):
        # indent forces pretty print
        json_schema = json.dumps(ymal_data,indent=4,sort_keys=False)
        logger.info(json_schema)
        with open(args.output, 'w') as json_schema_file:
                json_schema_file.write(json_schema)

    if (args.format == 'yaml'):
        # indent forces pretty print
        yaml_schema = yaml.dump(ymal_data)
        logger.info(yaml_schema)
        with open(args.output, 'w') as yaml_schema_file:
                yaml_schema_file.write(yaml_schema)
    pass

def main():
    parser = argparse.ArgumentParser()

    default_parser = argparse.ArgumentParser(add_help=False)

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_json = subparsers.add_parser('format', parents=[default_parser])
    parser_json.add_argument('format',choices=['json', 'yaml'], help='json  file output path')
    parser_json.add_argument('source', type=str, help='json or yaml file')
    parser_json.add_argument('output', type=str, help='json or yaml file')
    parser_json.set_defaults(func=convert)

    parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    parser_validate.add_argument('source', type=str, help='json or yaml file')
    parser_validate.add_argument('level',choices=[0, 1],default=1,nargs='?', help='level of validation')
    parser_validate.add_argument('schema',default='schema/df2_schema.json',nargs='?', help='schema to use to validate. default=')
    parser_validate.set_defaults(func=df_validate)

    # parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    # parser_validate.add_argument('json_schema_file_path', type=str, help='json schema file path')
    # parser_validate.set_defaults(func=validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()