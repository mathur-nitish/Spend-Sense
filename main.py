import fastapi as FAST_API
import Analyzer
from pydantic import BaseModel
import pandas as pd
import uvicorn
app = FAST_API.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SpeedPredictionInput(BaseModel):
    service_provider: str
    network_type: str
    start_loc: str
    end_loc: str


@app.get("/")
def basicGet():
    return {"message":"kaam krle poora"}

@app.post("/predict")
def whatTocarry(input_data: SpeedPredictionInput):

    start_location = input_data.start_loc
    end_location = input_data.end_loc
    service_provider = input_data.service_provider
    network_type = input_data.network_type

    data = pd.DataFrame({
        "Service Provider": [service_provider],
        "Technology": [network_type],
        "Test_type": ["Download"],
        "LSA": [end_location]
    })

    op1Analysis = Analyzer.analyze_payments(start_location,end_location)

    op2Analysis = Analyzer.predict_speed(data)
    if(op1Analysis=="Digital Payments"):
         op2Analysis = Analyzer.predict_speed(data)
         if(op2Analysis>4):
             return {"response":"Can rely on Digital Payments"}
         else:
             return {"response":"Digital Payments are accepted, but your mobile network network signals are poor!"}
    else:
         return {"response":"Use Cash!"}
