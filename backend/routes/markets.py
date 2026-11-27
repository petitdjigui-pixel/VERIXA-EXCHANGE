from fastapi import APIRouter, HTTPException

from engines.market_engine import (
    get_market_overview,
    get_available_markets,
    validate_resource_category
)

router = APIRouter(
    prefix="/api/v1/markets",
    tags=["Markets"]
)


@router.get("/")
def list_markets():
    return get_market_overview()


@router.get("/available")
def available_markets():
    return {
        "markets": get_available_markets()
    }


@router.get("/{resource_code}")
def get_market(resource_code: str):

    code = resource_code.upper()

    if not validate_resource_category(code):
        raise HTTPException(
            status_code=404,
            detail="Market not found"
        )

    return {
        "code": code,
        "name": get_market_overview()["categories"][
            list(
                item["code"]
                for item in get_market_overview()["categories"]
            ).index(code)
        ]["name"],
        "mode": "simulation",
        "trading_enabled": False
    }
  
