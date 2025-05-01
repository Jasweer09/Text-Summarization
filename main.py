from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} is Completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} is Completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} is Completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_transformation = ModelTrainerPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} is Completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    data_transformation = ModelEvaluationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} is Completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e