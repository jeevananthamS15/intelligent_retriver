import uvicorn
from fastapi import FastAPI
from api.endpoints import router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="Insurance Policy Q&A API")

app.include_router(router, prefix="/api/v1")

@app.get("/")
def home():
    return {"message": "Service is running "}

if __name__ == "__main__":
    # Render assigns a port via the PORT env variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
