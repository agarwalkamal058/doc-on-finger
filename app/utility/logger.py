import os
import time
import logging
import importlib
from logging.handlers import TimedRotatingFileHandler
properties = importlib.import_module("app.resources." + os.getenv('environment') + "_properties") 

def get_logger():
    formatter = logging.Formatter('%(asctime)s- %(threadName)s- %(name)s- %(levelname)s- %(message)s',"%b %d %H:%M:%S")
    handler = TimedRotatingFileHandler(properties.log_file_path + 'doc_on_finger.log', 
                                when='H',
                                backupCount=360)
    handler.setFormatter(formatter)
    logger = logging.getLogger("doc_on_finger")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

logger = get_logger()