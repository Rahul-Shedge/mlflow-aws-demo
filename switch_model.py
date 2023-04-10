from utils.sagemaker_integration import switching_models
from utils.common import read_yaml


if __name__ == "__main__":
    config = read_yaml("./config.yaml")
    response = switching_models(config)
    print(response)