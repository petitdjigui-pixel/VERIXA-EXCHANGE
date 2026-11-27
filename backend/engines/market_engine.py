from typing import Dict, List

MARKET_CATEGORIES = {
    "COMPUTE": "Computing Capacity",
    "STORAGE": "Digital Storage",
    "NETWORK": "Network Capacity",
    "DATA": "Data Processing"
}


def get_market_categories() -> Dict[str, str]:
    return MARKET_CATEGORIES.copy()


def validate_resource_category(category: str) -> bool:
    return category.upper() in MARKET_CATEGORIES


def get_market_overview() -> Dict:
    return {
        "platform": "VERIXA EXCHANGE",
        "symbol": "VRX",
        "mode": "simulation",
        "market_status": "development",
        "categories": [
            {
                "code": code,
                "name": name,
                "status": "development"
            }
            for code, name in MARKET_CATEGORIES.items()
        ]
    }


def get_available_markets() -> List[Dict]:
    return [
        {
            "code": code,
            "name": name,
            "trading_enabled": False,
            "mode": "simulation"
        }
        for code, name in MARKET_CATEGORIES.items()
    ]
  
