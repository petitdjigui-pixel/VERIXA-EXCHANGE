from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/api/v1/wallet",
    tags=["Wallet"]
)

# Portefeuilles temporaires de démonstration.
wallets = {}

SUPPORTED_CURRENCIES = {
    "USD",
    "XOF",
    "EUR",
    "GBP"
}


class WalletRequest(BaseModel):
    user_id: int = Field(gt=0)
    currency: str = "XOF"


@router.post("/create")
def create_wallet(request: WalletRequest):

    currency = request.currency.upper()

    if currency not in SUPPORTED_CURRENCIES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported currency"
        )

    wallet_id = f"{request.user_id}_{currency}"

    if wallet_id in wallets:
        return wallets[wallet_id]

    wallet = {
        "wallet_id": wallet_id,
        "user_id": request.user_id,
        "currency": currency,
        "balance": 0.0,
        "mode": "simulation",
        "deposits_enabled": False,
        "withdrawals_enabled": False
    }

    wallets[wallet_id] = wallet

    return wallet


@router.get("/{user_id}")
def get_user_wallets(user_id: int):

    if user_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid user ID"
        )

    user_wallets = [
        wallet
        for wallet in wallets.values()
        if wallet["user_id"] == user_id
    ]

    return {
        "user_id": user_id,
        "wallets": user_wallets,
        "mode": "simulation"
}
  
