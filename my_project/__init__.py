import logging
from os.path import dirname, abspath

from my_project import promain
from my_project import sub_package


ROOT_DIR = dirname(abspath(__file__))

#logging
logging.basicConfig(level=logging.INFO)