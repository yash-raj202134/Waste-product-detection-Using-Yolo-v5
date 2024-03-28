from WasteProductDetection.logger import logging
from WasteProductDetection.exception import AppException
import sys




# Testing 

logging.info("test log")
try:
    1/0
except Exception as e:
    raise AppException(e,sys)

