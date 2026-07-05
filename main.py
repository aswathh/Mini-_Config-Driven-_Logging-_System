import os
import logging
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

def setup_logger(name:str,env:str)-> logging.Logger:
    logger = logging.getLogger(name) # getting the logger
    logger.setLevel(logging.DEBUG) # setting the level for the logger
    logger.handlers.clear() # remove all the past handlers

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if env == "dev":
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    elif env == "prod":
        log_file_path = os.getenv("LOG_FILE_PATH", "app.log")
        file_handler = logging.FileHandler()
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

    