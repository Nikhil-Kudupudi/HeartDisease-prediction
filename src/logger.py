import os
import logging
from datetime import datetime

LOG_FOLDER=os.path.join(os.getcwd(),"logs")
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(LOG_FOLDER,exist_ok=True)
FILE_PATH=os.path.join(LOG_FOLDER,LOG_FILE)
logging.basicConfig(filename=FILE_PATH, format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",level=logging.INFO)
