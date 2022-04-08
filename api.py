import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import yaml
import pathlib
import uvicorn

def read_yaml(file_path):
    with open(file_path,'r') as f:
        return yaml.safe_load(f)
config=read_yaml('config.yaml')

model_path=config['MODEL']['MODEL_PATH']

with open(model_path,'rb') as f:
    automl=pickle.load(f)
# Print the best model
print(automl.model.estimator)

app=FastAPI()

class RequestBody(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

@app.get("/")
def read_root():
    return "Hello Ashish"

@app.post('/predict')
async def predict(data: RequestBody):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    test_data=np.array(test_data)
    class_probs = automl.predict_proba(test_data)
    return {'class_probs': str(class_probs)}

# if __name__=="__main__":
#     uvicorn.run("api:app",host='0.0.0.0', port=8001)


# if __name__ == "__main__":
#     uvicorn.run(app)
