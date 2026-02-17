import os  
import urllib.request as request
from zipfile import ZipFile
from datascience.entity.config_entity import DataIngestionConfig
from src.datascience.config import CONFIG_FILE_PATH


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        print(f"Downloading data from {self.config.source_URL} to {self.config.local_data_file}")
        request.urlretrieve(self.config.source_URL, self.config.local_data_file)

    def unzip_data(self):
        print(f"Unzipping data from {self.config.local_data_file} to {self.config.unzip_dir}")
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

