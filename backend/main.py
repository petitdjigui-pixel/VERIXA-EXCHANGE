from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.users import router as users_router
from routes.markets import router as markets_router
from routes.orders import router as orders_router
from routes.wallet import router as wallet_router

app = FastAPI(
    title="VERIXA EXCHANGE API",
    description="A New Digital Market",
    version="0.2.0"
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
        "slogan": "A New Digital Market",
        "status": "running",
        "mode": "simulation",
        "version": "0.2.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "VERIXA API",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


app.include_router(users_router)
app.include_router(markets_router)
app.include_router(orders_router)
app.include_router(wallet_router)


@app.get("/api/v1")
def api_information():
    return {
        "platform": "VERIXA EXCHANGE",
        "api_version": "0.2.0",
        "available_modules": [
            "users",
            "markets",
            "orders",
            "wallet"
        ],
        "mode": "simulation"
    }
    
