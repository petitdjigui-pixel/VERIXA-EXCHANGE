from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from engines.order_engine import Order, validate_order

router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders"]
)

# Stockage temporaire pour les essais.
# Les ordres seront perdus au redémarrage.
simulation_orders = []


class OrderRequest(BaseModel):
    user_id: int = Field(gt=0)
    resource_code: str = Field(min_length=1, max_length=30)
    side: str
    quantity: float = Field(gt=0)
    price: float = Field(gt=0)
    currency: str = "USD"


@router.post("/")
def create_order(request: OrderRequest):

    order = Order(
        order_id=str(uuid4()),
        user_id=request.user_id,
        resource_code=request.resource_code.upper(),
        side=request.side.upper(),
        quantity=request.quantity,
        price=request.price,
        currency=request.currency.upper()
    )

    valid, message = validate_order(order)

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    result = {
        "order_id": order.order_id,
        "user_id": order.user_id,
        "resource_code": order.resource_code,
        "side": order.side,
        "quantity": order.quantity,
        "price": order.price,
        "currency": order.currency,
        "status": "PENDING_SIMULATION",
        "money_transferred": False
    }

    simulation_orders.append(result)

    return result


@router.get("/")
def list_orders():
    return {
        "mode": "simulation",
        "total": len(simulation_orders),
        "orders": simulation_orders
    }
  
