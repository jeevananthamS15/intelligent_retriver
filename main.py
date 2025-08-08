import uvicorn
from fastapi import FastAPI
from api.endpoints import router
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Insurance Policy Q&A API")

# Include your API routes
app.include_router(router, prefix="/api/v1")

# Root endpoint for health check
@app.get("/")
def home():
    return {"message": "Service is running "}

# Entry point
if __name__ == "__main__":
    # Use dynamic port for Render, default to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
