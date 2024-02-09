# End2End_StudentPerformance_with_MLFlow_DVC


## Steps 


1. `setup git repo`
    - `New environment`
    - `setup.py`
    - `requiremets.txt`


2. `Logging And Exceptions Handler`
    - `Project Folder`
    - `ExceptionHandler`
    - `LoggingHandler`
    - `Utils- common`


3. `Notebook - transformation and training`
    - `EDA`
    - `Model Trainer`

4. `Components Creation`
    - `data ingestion`
    - `data transformation`
    - `model trainer`
    - `model evaluation`

5. `Prediction Pipeline Creation`
    - `train pipeline`
    - `prediction pipeline`


###  MlFlow


MLFLOW_TRACKING_URI=https://dagshub.com/subramanyanayak3/End2End_StudentPerformance_with_MLFlow_DVC.mlflow \
MLFLOW_TRACKING_USERNAME=subramanyanayak3 \
MLFLOW_TRACKING_PASSWORD=b18ad68cf0c678f5f616a47081e6c4c129e4a844 \
python script.py



380675867318.dkr.ecr.eu-north-1.amazonaws.com/student


### Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### Configure EC2 as self-hosted runner:

`Setup github secrets:`

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app