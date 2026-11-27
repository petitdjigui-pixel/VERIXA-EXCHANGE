from dataclasses import dataclass


@dataclass
class MarketPrice:
    resource_code: str
    reference_price: float
    currency: str
    supply: float
    demand: float


def calculate_indicative_price(
    reference_price: float,
    supply: float,
    demand: float
) -> float:
    if reference_price <= 0:
        raise ValueError("Reference price must be positive")

    if supply < 0 or demand < 0:
        raise ValueError("Supply and demand cannot be negative")

    if supply == 0 and demand == 0:
        return round(reference_price, 4)

    if supply == 0:
        ratio = 1.20
    elif demand == 0:
        ratio = 0.80
    else:
        ratio = demand / supply

    # Limiter les variations du modèle de démonstration.
    adjustment = max(0.80, min(1.20, ratio))

    return round(reference_price * adjustment, 4)


def get_price_simulation(
    resource_code: str,
    reference_price: float,
    supply: float,
    demand: float,
    currency: str = "USD"
) -> dict:

    price = calculate_indicative_price(
        reference_price,
        supply,
        demand
    )

    return {
        "resource_code": resource_code.upper(),
        "reference_price": reference_price,
        "indicative_price": price,
        "currency": currency.upper(),
        "supply": supply,
        "demand": demand,
        "mode": "simulation",
        "is_executable_market_price": False
    }
  
