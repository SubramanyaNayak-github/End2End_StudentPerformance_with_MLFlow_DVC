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



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/subramanyanayak3/End2End_StudentPerformance_with_MLFlow_DVC.mlflow \
MLFLOW_TRACKING_USERNAME=subramanyanayak3 \
MLFLOW_TRACKING_PASSWORD=b18ad68cf0c678f5f616a47081e6c4c129e4a844 \
python script.py


**Run this to export as env variables:**

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/subramanyanayak3/EndToEnd_MLProject_With_CiCd-Docker.mlflow

export MLFLOW_TRACKING_USERNAME=subramanyanayak3 

export MLFLOW_TRACKING_PASSWORD=b18ad68cf0c678f5f616a47081e6c4c129e4a844

```

## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model




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




# How to run?
### STEPS:

Clone the repository

```bash
`https://github.com/SubramanyaNayak-github/End2End_StudentPerformance_with_MLFlow_DVC.git`

```
### STEP 01- Create a conda environment after opening the repository

```bash
python3 -m venv mlproj
```

```bash

source mlproj/bin/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## DVC 


- `Data Versioning`: DVC provides a mechanism to version control your datasets, ensuring that changes made to data are tracked and can be reverted if necessary. This enables reproducibility and collaboration in machine learning projects by maintaining a history of dataset changes over time.

- `Reproducibility`: Similar to MLflow's focus on experiment tracking, DVC emphasizes reproducibility in machine learning workflows by capturing the dependencies and configurations used to produce a particular result. It enables users to reproduce any experiment or result by tracking data, code, and model versions.

- `Model Dependency Management`: DVC extends version control beyond data to also include code and models. It helps manage dependencies between code, data, and models, ensuring that changes to one component are reflected in others. This ensures consistency and reliability in machine learning pipelines by maintaining the integrity of dependencies across different stages of development and deployment.

## DVC cmd
- `dvc init`
- `dvc repro`/ `dvc run`
- `dvc dag`


### `Dependency Tracking`
- `Output Versioning`
- `Simplified Configuration`
- `Experiment Tracking`




# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

    4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 380675867318.dkr.ecr.eu-north-1.amazonaws.com/student
	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:



###      optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
###      required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker




    # 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




# AZURE-CICD-Deployment-with-Github-Actions

		 `Docs for the Azure Web Apps Deploy action: https://github.com/Azure/webapps-deploy`
		 `More GitHub Actions for Azure: https://github.com/Azure/actions`

## Save pass:

-- #s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6 -- 


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 

