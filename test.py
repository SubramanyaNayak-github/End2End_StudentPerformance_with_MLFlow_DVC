import os
import sys
from typing import Any
from src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass

from src.components.data_ingestion import DataIngestionConfig,DataIngestion
from src.components.data_transformation import DataTransformationConfig,DataTransformation



if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()


    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
