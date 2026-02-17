from src.datascience import logger
from src.datascience.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline 

STAGE_NAME = "Data Ingestion Stage" 

try: 
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainPipeline()
    obj.intiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e