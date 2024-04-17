from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn
import bz2
import pickle
from sklearn.preprocessing import MinMaxScaler

app=FastAPI()

template = Jinja2Templates(directory="templates")


pickle_in = bz2.BZ2File('classification.pkl', 'rb')
classifier = pickle.load(pickle_in)

class ForestFire(BaseModel):
    Temperature: float
    Ws: float
    FFMC: float
    DMC: float
    ISI: float


@app.get("/")
def index(req: Request):
    return template.TemplateResponse(
        name = "index.html",
        context = {"request": req}
    )


@app.get("/input.html")
def input(req: Request):
    return template.TemplateResponse(
        name = "input.html",
        context = {"request": req}
    )


@app.post("/predict")
def predict(data: ForestFire):
    # Extract features from the request data
    Temperature = data.Temperature
    Ws = data.Ws
    FFMC = data.FFMC
    DMC = data.DMC
    ISI = data.ISI
    
    scaler = MinMaxScaler()
    features_normalized = scaler.fit_transform([[Temperature, Ws, FFMC, DMC, ISI]])

    # Make predictions using the loaded classifier
    prediction = classifier.predict(features_normalized)
    # Make predictions using the loaded classifier
    # prediction = classifier.predict([[Temperature, Ws, FFMC, DMC, ISI]])
    # prediction = classifier.predict([[12,14,85,6.7,6.7]])
    # Convert prediction to a human-readable format
    if prediction[0] < 0:
        prediction_label = "Forest Fire will nnot occur" 
    else:
        prediction_label = "Forest Fire will not occur"
    print(prediction[0])

    return {"prediction": prediction_label}
    

  


if __name__ == "__main__":
    uvicorn.run("main:app")