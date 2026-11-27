from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone

app = FastAPI(
    title="VERIXA EXCHANGE API",
    description="A New Digital Market",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "name": "VERIXA EXCHANGE",
        "symbol": "VRX",
        "message": "Welcome to a new digital market.",
        "status": "running",
        "mode": "simulation"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "VERIXA API",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/api/v1/markets")
def get_markets():
    return {
        "mode": "simulation",
        "markets": [
            {
                "id": "COMPUTE",
                "name": "Computing Capacity",
                "status": "development"
            },
            {
                "id": "STORAGE",
                "name": "Digital Storage",
                "status": "development"
            },
            {
                "id": "NETWORK",
                "name": "Network Capacity",
                "status": "development"
            },
            {
                "id": "DATA",
                "name": "Data Processing",
                "status": "development"
            }
        ]
    }
  
