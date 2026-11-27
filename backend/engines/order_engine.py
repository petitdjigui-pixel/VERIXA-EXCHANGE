from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    order_id: str
    user_id: int
    resource_code: str
    side: str
    quantity: float
    price: float
    currency: str = "USD"


def validate_order(order: Order) -> tuple:
    if not order.order_id:
        return False, "Order ID is required"

    if order.user_id <= 0:
        return False, "Invalid user ID"

    if order.side.upper() not in ("BUY", "SELL"):
        return False, "Side must be BUY or SELL"

    if order.quantity <= 0:
        return False, "Quantity must be positive"

    if order.price <= 0:
        return False, "Price must be positive"

    if not order.resource_code:
        return False, "Resource code is required"

    return True, "Order validated"


def orders_are_compatible(
    buy_order: Order,
    sell_order: Order
) -> bool:

    valid_buy, _ = validate_order(buy_order)
    valid_sell, _ = validate_order(sell_order)

    if not valid_buy or not valid_sell:
        return False

    if buy_order.side.upper() != "BUY":
        return False

    if sell_order.side.upper() != "SELL":
        return False

    if buy_order.resource_code.upper() != sell_order.resource_code.upper():
        return False

    if buy_order.currency.upper() != sell_order.currency.upper():
        return False

    return buy_order.price >= sell_order.price


def prepare_match(
    buy_order: Order,
    sell_order: Order
) -> Optional[dict]:

    if not orders_are_compatible(buy_order, sell_order):
        return None

    matched_quantity = min(
        buy_order.quantity,
        sell_order.quantity
    )

    execution_price = sell_order.price

    return {
        "buy_order_id": buy_order.order_id,
        "sell_order_id": sell_order.order_id,
        "resource_code": buy_order.resource_code.upper(),
        "quantity": matched_quantity,
        "price": execution_price,
        "currency": buy_order.currency.upper(),
        "status": "SIMULATION_ONLY",
        "money_transferred": False,
        "resource_delivered": False
  }
  
