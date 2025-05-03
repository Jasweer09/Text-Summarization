from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from textSummarizer.pipeline.prediction import PredictionPipeline
import os
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return {"message": "Training completed!"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()
        text = data.get("text", "")
        obj = PredictionPipeline()
        output = obj.predict(text)
        return output
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
