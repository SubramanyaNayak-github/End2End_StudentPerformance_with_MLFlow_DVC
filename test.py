from src.logger import logger
from src.exception import CustomException
import sys


try:
    a = 1/0
except Exception as e:
    logger.info('zero division error')
    raise CustomException(e, sys)