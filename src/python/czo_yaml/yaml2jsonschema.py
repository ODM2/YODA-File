__author__ = 'valentin'
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

logging.basicConfig(level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

filelogger = logging.FileHandler('yaml2json.log')
filelogger.setFormatter(logging.Formatter('\n%(message)s'))
logger = logging.getLogger('')
logger.addHandler(console)
logger.addHandler(filelogger)

def convert(args):
    stream = file(args.json_source)
    ymal_data = yaml.load (stream)

    logger.info( ymal_data )

    s = genson.Schema()
    s.add_object(ymal_data)

    # indent forces pretty print
    json_schema = s.to_json(indent=4,sort_keys=False)
    logger.info(json_schema)
    with open(args.json_schema_file_path, 'w') as json_schema_file:
            json_schema_file.write(json_schema)

def main():
    parser = argparse.ArgumentParser()

    default_parser = argparse.ArgumentParser(add_help=False)
    default_parser.add_argument('json_source', type=str, help='file')


    subparsers = parser.add_subparsers(help='sub-command help')

    parser_validate = subparsers.add_parser('json', parents=[default_parser])
    parser_validate.add_argument('json_schema_file_path', type=str, help='json schema file output path')
    parser_validate.set_defaults(func=convert)

    # parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    # parser_validate.add_argument('json_schema_file_path', type=str, help='json schema file path')
    # parser_validate.set_defaults(func=validate)



    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()