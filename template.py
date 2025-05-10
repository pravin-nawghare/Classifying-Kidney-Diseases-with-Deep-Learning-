import os 
from pathlib import Path
import logging

#logging string
#logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s -')

project_name = 'Deep_Learning'

# List of files and folders to create
list_of_files = [
    ".github/workflows/.gitkeep", # for cicd
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "reserach/training_template.ipynb",
    "templates/index.html"
]

# Create the project structure
for file_path in  list_of_files:
    filepath = Path(file_path)
    file_dir, file_name = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        #logging.info(f"Creating directory: {file_dir} for the file: {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(file_path, "w") as f:
            pass
            #logging.info(f"Creating file: {file_path}")
    
    else:
        #logging.info(f"{file_name} is already present in the directory: {file_dir}.")
        print(f"{file_name} is already present in the directory: {file_dir}.")