from utils.sagemaker_integration import query
from utils.common import read_yaml
import pandas as pd
import json




data = pd.read_json('{"fixed acidity":{"0":7.4},"volatile acidity":{"0":0.7},"citric acid":{"0":0},"residual sugar":{"0":1.9},"chlorides":{"0":0.076},"free sulfur dioxide":{"0":11},"total sulfur dioxide":{"0":34}, "density":{"0":0.9978},"pH":{"0":3.51},"sulphates":{"0":0.56},"alcohol":{"0":9.4} }')
#data = pd.read_csv("test.csv",sep=";")
#input = json.dumps(data.to_json())


#data = pd.read_json('{columns : [\"fixed acidity\", \"volatile acidity\", \"citric acid\", \"residual sugar\", \"chlorides\", \"free sulfur dioxide\", \"total sulfur dioxide\", \"density\", \"pH\", \"sulphates\", \"alcohol\"],\"data\":[[6.2, 0.66, 0.48, 1.2, 0.029, 29, 75, 0.98, 3.33, 0.39, 12.8]]}')

if __name__ == "__main__":
    config = read_yaml("./config.yaml")
    # print(input)
    input_json = data.to_json(orient="split")
    #print(type(dict(data.to_json(orient="split"))))
    #inputs = json.dumps(input_json)
    print(input_json)
    Response = query(input_json,config)
    print(f"Prediction From Model Endpoint :{Response}")



