from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.entity.config_entity import ModelEvaluationConfig

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluationConfig(config = model_evaluation_config)
        model_evaluation.evaluate()