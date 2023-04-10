from utils.sagemaker_integration import query
from utils.common import read_yaml
import pandas as pd




data = pd.read_json('{"fixed acidity":{"0":7.4},"volatile acidity":{"0":0.7},"citric acid":{"0":0},\
                    "residual sugar":{"0":1.9},"chlorides":{"0":0.076},"free sulfur dioxide":{"0":11},\
                    "total sulfur dioxide":{"0":34},"density":{"0":0.9978},"pH":{"0":3.51},"sulphates":{"0":0.56},"alcohol":{"0":9.4} \
                    }')

if __name__ == "__main__":
    config = read_yaml("./config.yaml")
    input_json = data.to_json(orient='split')
    sagemaker = query(input_json)
    Response = sagemaker.query(input_json)
    print(f"Prediction From Model Endpoint :{Response}")
    