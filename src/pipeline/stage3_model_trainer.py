from src.components.model_trainer import ModelTrainerConfig,ModelTrainer
from src.pipeline.stage1_data_ingestion import *
from src.pipeline.stage2_data_transformation import *
import os
import sys
from typing import Any
from src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass


if __name__=="__main__":

    train_data = 'artifacts/train.csv'
    test_data = 'artifacts/test.csv'

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))