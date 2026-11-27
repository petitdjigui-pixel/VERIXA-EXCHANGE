from datetime import datetime, timezone
from typing import List, Dict


def build_candle(
    resource_code: str,
    trades: List[Dict]
) -> dict:

    if not trades:
        return {
            "resource_code": resource_code.upper(),
            "status": "no_trades",
            "message": "No executed trades available."
        }

    prices = []

    for trade in trades:
        price = float(trade["price"])

        if price <= 0:
            raise ValueError("Trade prices must be positive")

        prices.append({
            "price": price,
            "quantity": float(trade.get("quantity", 0))
        })

    if any(item["quantity"] <= 0 for item in prices):
        raise ValueError("Trade quantities must be positive")

    open_price = prices[0]["price"]
    close_price = prices[-1]["price"]
    high_price = max(item["price"] for item in prices)
    low_price = min(item["price"] for item in prices)

    volume = sum(item["quantity"] for item in prices)

    return {
        "resource_code": resource_code.upper(),
        "open": open_price,
        "high": high_price,
        "low": low_price,
        "close": close_price,
        "volume": volume,
        "direction": (
            "bullish" if close_price >= open_price else "bearish"
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "simulation"
    }


def build_candle_series(
    resource_code: str,
    trade_groups: List[List[Dict]]
) -> List[dict]:

    return [
        build_candle(resource_code, group)
        for group in trade_groups
        if group
  ]
  
