import os.path
import sys
import yaml
import base64

from WasteProductDetection.exception import AppException
from WasteProductDetection.logger import logging


def read_yaml_file(file_path: str) -> dict:
    '''function to read yaml files'''
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    '''a function to write yaml file'''
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write_yaml_file")

    except Exception as e:
        raise AppException(e, sys)
    


def encodeImageIntoBase64(croppedImagePath):
    '''image encoder (base64)'''
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


def decodeImage(imgstring, fileName):
    '''image decoder'''
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


