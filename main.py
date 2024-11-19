from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage1_dataIngestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info("Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
