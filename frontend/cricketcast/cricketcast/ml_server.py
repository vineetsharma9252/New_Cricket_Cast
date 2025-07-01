from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from fastapi import Request
import os
app = FastAPI()


# Find the model file in the MODEL_DIR using shutil
model_path = "modelETR.pkl"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

modelETR = load(model_path)

@app.post("/predict/")
async def root(request:Request):
    try:
        print(f"it is working ")
        data = await request.json()
        prediction = modelETR.predict([data])[0]
        final_score_prediction = int(prediction)
        print(f"Final score prediction is {final_score_prediction}")
    except Exception as e:
        final_score_prediction = None
    return {"final_prediction": final_score_prediction}


import uvicorn
import shutil
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
