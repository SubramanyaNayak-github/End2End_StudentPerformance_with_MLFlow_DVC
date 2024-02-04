import os
import sys
from typing import Any
from src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path: str=os.path.join('artifacts','raw_data.csv')
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logger.info('Entered the data ingestion component')
        try:
            df = pd.read_csv('notebooks/data/student.csv')
            logger.info('Read the dataset')


            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logger.info('Train Test split Initiated')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logger.info("Data Ingestion of the data is completed")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        
        except Exception as e:
            raise CustomException(e,sys)
        



    