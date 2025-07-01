from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from fastapi import Request
import os
app = FastAPI()


# Find the model file in the MODEL_DIR using shutil
MODEL_DIR = "C:/Users/maste/Downloads/fast-API/cricketCast/cricket/cricketcast_test/New_cricket_cast/frontend/cricketcast/cricketcast"  # or the directory where your model is stored
model_filename = "modelETR.pkl"
model_path = None

# Search for the model file in MODEL_DIR and its subdirectories
for root, dirs, files in os.walk(MODEL_DIR):
    print("Searching in directory:", root)
    print("Files found:", files)
    if model_filename in files:
        model_path = os.path.join(root, model_filename)
        break

if model_path is None:
    raise FileNotFoundError(f"{model_filename} not found in {MODEL_DIR}")

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