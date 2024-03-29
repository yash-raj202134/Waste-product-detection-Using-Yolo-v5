from WasteProductDetection.logger import logging
from WasteProductDetection.exception import AppException
from WasteProductDetection.utils.main_utils import *

import sys
import os




# Testing 

logging.info("test log")
try:
    1/0
except Exception as e:
    raise AppException(e,sys)


# read_yaml_file(os.path)


