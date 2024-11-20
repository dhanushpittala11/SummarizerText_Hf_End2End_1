from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage1_dataIngestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage2_DataTransformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage3_modeltrainer_pipeline import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage4_modelevaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME="Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info("Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data Transformation stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataTransformationTrainingPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info("Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_data_transformation()
    logger.info("Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelEvaluationTrainingPipeline()
    model_trainer_pipeline.initiate_model_evaluation()
    logger.info("Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
