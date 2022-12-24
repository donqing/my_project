import logging
from os.path import dirname, abspath


ROOT_DIR = dirname(abspath(__file__))

#logging
logging.basicConfig(level=logging.INFO)

__all__ = ["sub_package"]