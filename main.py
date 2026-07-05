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

def process_tasks(logger: logging.Logger, tasks: list) -> Dict[str, int]:
    
    result_summary: Dict[str, int] = {"success": 0, "failed": 0}

    for task in tasks:
        try:
            logger.debug(f"Processing task: {task}")
            if task == 0:
                raise ZeroDivisionError("Cannot process zero task")
            output = 100 / task
            logger.info(f"Task '{task}' processed successfully. Result: {output}")
            result_summary["success"] += 1
        except Exception:
            logger.error(f"Task '{task}' failed", exc_info=True)
            result_summary["failed"] += 1

    return result_summary 

# ---- main execution ----
app_env: str = os.getenv("APP_ENV", "dev")
logger = setup_logger(__name__, app_env)

logger.info(f"Application starting in '{app_env}' mode")

tasks = [5, 10, 0, 2, "invalid"]  # oru intentional bad input um vechirukom test ku
summary = process_tasks(logger, tasks)

logger.info(f"Final summary: {summary}")
print(summary)