import fastapi as FAST_API
from fastapi import Request
from pydantic import BaseModel
import pandas as pd
import cache_optimizer as CacheOptimizer
app = FAST_API.FastAPI()


class SpeedPredictionInput(BaseModel):
    service_provider: str
    network_type: str
    start_loc: str
    end_loc: str



@app.get("/")
def basicGet():
    return {"message":"kaam krle poora"}

@app.post("/predict")
def whatTocarry(request:Request, input_data: SpeedPredictionInput):

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

    session_id = request.client.host

    response = CacheOptimizer.perform_calculation(session_id,data)

    return {"response":response['result']} 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8002)