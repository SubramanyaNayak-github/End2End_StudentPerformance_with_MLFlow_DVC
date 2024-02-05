import os
import sys
import json
from dataclasses import dataclass
from urllib.parse import urlparse
from pathlib import Path

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models,save_json

import mlflow
import mlflow.sklearn

# Export MLflow 
os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/subramanyanayak3/End2End_StudentPerformance_with_MLFlow_DVC.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'subramanyanayak3'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'b18ad68cf0c678f5f616a47081e6c4c129e4a844'


mlflow_uri = 'https://dagshub.com/subramanyanayak3/End2End_StudentPerformance_with_MLFlow_DVC.mlflow'

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
    evaluation_results_file_path: str = os.path.join("artifacts", "evaluation_results.json")
    mlflow_uri: str = os.environ.get('MLFLOW_TRACKING_URI')

class ModelTrainer:
    def __init__(self):
        
        self.model_trainer_config = ModelTrainerConfig(mlflow_uri=mlflow_uri)  # Set MLflow URI attribute

        #self.model_trainer_config=ModelTrainerConfig()

    def save_evaluation_results(self, evaluation_results):
        try:
            with open(self.model_trainer_config.evaluation_results_file_path, "w") as f:
                json.dump(evaluation_results, f, indent=4)
        except Exception as e:
            raise CustomException(e, sys)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.model_trainer_config.mlflow_uri)
        self.tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


    def initiate_model_trainer(self,train_array,test_array):
        try:
            with mlflow.start_run():
                logging.info("Split training and test input data")
                X_train,y_train,X_test,y_test=(
                    train_array[:,:-1],
                    train_array[:,-1],
                    test_array[:,:-1],
                    test_array[:,-1]
                )
                models = {
                    "Random Forest": RandomForestRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Gradient Boosting": GradientBoostingRegressor(),
                    "Linear Regression": LinearRegression(),
                    "XGBRegressor": XGBRegressor(),
                    "AdaBoost Regressor": AdaBoostRegressor()
                }
                param = {
                    "Decision Tree": {
                        'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    },
                    "Random Forest": {
                        'n_estimators': [8, 16, 32, 64, 128, 256]
                    },
                    "Gradient Boosting": {
                        'learning_rate': [.1, .01, .05, .001],
                        'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                        'n_estimators': [8, 16, 32, 64, 128, 256]
                    },
                    "Linear Regression": {
                         'fit_intercept': [True, False]
                         
                    },
                    "XGBRegressor": {
                        'learning_rate': [.1, .01, .05, .001],
                        'n_estimators': [8, 16, 32, 64, 128, 256]
                    },
                    "AdaBoost Regressor": {
                        'learning_rate': [.1, .01, 0.5, .001],
                        'n_estimators': [8, 16, 32, 64, 128, 256]
                    }
                }

                model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                                models=models,param=param)
                
                ## To get best model score from dict
                best_model_score = max(sorted(model_report.values()))

                ## To get best model name from dict

                best_model_name = list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)
                ]
                best_model = models[best_model_name]

                if best_model_score<0.6:
                    raise CustomException("No best model found")
                logging.info(f"Best found model on both training and testing dataset")

                save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model
                )

                mlflow.log_params(param[best_model_name])  # Log hyperparameters
                mlflow.log_metric("r2_score", best_model_score)  # Log model performance metric

                logging.info(f"Best model saved.")

                predicted=best_model.predict(X_test)

                r2_square = r2_score(y_test, predicted)
                evaluation_results = {
                    "r2_score": r2_square,
                    "best_params": param[best_model_name]
                }
                self.save_evaluation_results(evaluation_results)

                
                return r2_square

            

        except Exception as e:
            raise CustomException(e,sys)
        