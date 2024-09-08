import os
import logging
from pathlib import Path

#seperate stages ml project like data injection,EDA,feature engineering, model building and model evaluation and compounents are part of pipelens, we have two pipeline first one is training pipeline and infercing pipeline

list_of_files=[
    ".github/workflows/.gitkeep", # .gitkeep user for deployment(CICD)
    "src/__init__.py",
    "src/components/__init__.py", 
    "src/components/data_injection.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    print(filepath)
    filedir, filename =os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creaating directory:{filedir} for file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass #create am empty file