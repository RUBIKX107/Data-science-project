import os
import yaml
from src.datascience import logger 
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns 

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError if yaml file is empty
        e: empty File
    
    Returns:
        ConfigBox : ConfigBox type 
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e 
    
@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose = True):
    """create list of directories

    Args:
        path_to_directories (list[Path]): list of path of directories
        verbose (bool, optional): whether to log info. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")