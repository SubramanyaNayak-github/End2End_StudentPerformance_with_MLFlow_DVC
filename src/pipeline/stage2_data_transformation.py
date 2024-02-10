import os
import sys
from typing import Any
from src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass

from src.pipeline.stage1_data_ingestion import *
from src.components.data_transformation import DataTransformationConfig,DataTransformation

if __name__=="__main__":

    train_data = 'artifacts/train.csv'
    test_data = 'artifacts/test.csv'

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)