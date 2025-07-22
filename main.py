# main.py
# To run: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import time

# --- Pydantic Models for data validation ---
class PriceData(BaseModel):
    asset_id: str
    price: float
    timestamp: float

# --- Initialize FastAPI App ---
app = FastAPI(
    title="Real-Time Financial Data API",
    description="A secure and robust API for fetching financial data.",
    version="1.0.0",
)

# --- CORS Middleware ---
# This allows your frontend (running on a different domain/port)
# to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend's domain
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --- Mock Data Store (similar to the JS version) ---
# In a real-world scenario, this data would be fetched from a live API
# (e.g., Alpha Vantage, CoinGecko, Binance) or a database.
mock_db = {
    "BTC-USD": {"base": 68000, "volatility": 0.001, "current_price": 68000},
    "ETH-USD": {"base": 3500, "volatility": 0.0015, "current_price": 3500},
    "AAPL": {"base": 190, "volatility": 0.002, "current_price": 190},
    "GOOGL": {"base": 175, "volatility": 0.0018, "current_price": 175},
    "XAU-USD": {"base": 2300, "volatility": 0.0005, "current_price": 2300},
    "WTI-USD": {"base": 80, "volatility": 0.0025, "current_price": 80},
}

def get_simulated_price(asset_id: str) -> float:
    """Generates a new simulated price for an asset."""
    asset = mock_db[asset_id]
    change_percent = (random.random() - 0.49) * asset["volatility"]
    change = asset["current_price"] * change_percent
    new_price = asset["current_price"] + change
    mock_db[asset_id]["current_price"] = new_price  # Update the "database"
    return new_price

# --- API Endpoints ---
@app.get("/", summary="Root endpoint, checks API status")
async def read_root():
    """ A simple health check endpoint. """
    return {"status": "ok", "message": "RFD Monitor API is running."}


@app.get("/api/price/{asset_id}", response_model=PriceData, summary="Get latest price for an asset")
async def get_price(asset_id: str):
    """
    Fetches the latest price for a given financial asset.

    - **asset_id**: The ticker or symbol for the asset (e.g., `BTC-USD`, `AAPL`).
    """
    if asset_id not in mock_db:
        raise HTTPException(status_code=404, detail="Asset not found")

    try:
        # In a real app, this is where you'd call an external API.
        # For now, we simulate it.
        price = get_simulated_price(asset_id)
        
        return PriceData(
            asset_id=asset_id,
            price=price,
            timestamp=time.time()
        )
    except Exception as e:
        # Basic fault tolerance
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
