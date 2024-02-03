import logging
import os 
import sys
from datetime import datetime




LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'

logs_path=os.path.join(os.getcwd(),log_dir,LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=logging_str,
    level=logging.INFO
)


logger = logging.getLogger('ProjectLogger')

