from setuptools import find_packages , setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        This function will return a list of requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[requirement.replace('\n',' ')for requirement in requirements]


        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements


__version__ = '0.1'

REPO_NAME = "End2End_StudentPerformance_with_MLFlow_DVC"
AUTHOR_USER_NAME = "SubramanyaNayak-githiub"
SRC_REPO = "StudentPerformance"
AUTHOR_EMAIL = "subramanayanayak3@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    description=("Student Performance Prediction"),
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        ]

      )