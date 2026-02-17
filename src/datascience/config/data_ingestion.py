from src.datascience.config.configuration import configuration
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainPipeline:
    def __init__(self):
        pass

def intiate_data_ingestion(self):
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        config = configuration()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
    
if __name__ == "__main__":
    obj = DataIngestionTrainPipeline()
    obj.intiate_data_ingestion()    