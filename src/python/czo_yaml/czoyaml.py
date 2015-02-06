__author__ = 'valentin'
import logging
import yaml
import genson
import json

# Playing: This read files
logging.basicConfig(level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

filelogger = logging.FileHandler('czoyaml.log')
filelogger.setFormatter(logging.Formatter('\n%(message)s'))
logger = logging.getLogger('')
logger.addHandler(console)
logger.addHandler(filelogger)

stream = file("../../../Examples/CRB_WELL_WATERLEVEL_2011_CZODisplay1.yml")
czowl = yaml.load (stream)

logger.info( czowl )

czo_yaml = yaml.dump(czowl)
logger.info(czo_yaml)

s = genson.Schema()
s.add_object(czowl)

# indent forces proetty pring
czo_json = s.to_json(indent=4)

logger.info(czo_json)


czo_json = s.to_json(indent=4,sort_keys=False)

logger.info(czo_json)