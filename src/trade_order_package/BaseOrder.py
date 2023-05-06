from enum import Enum

from pydantic import BaseModel, confloat

from trade_order_package.Asset import Asset, AllAssets
from trade_order_package.OrderSide import OrderSide


class _BaseOrder(BaseModel):
    side: OrderSide
    base_asset: AllAssets
    quote_asset: AllAssets
    amount: float = confloat(gt=0)
    market_type: Enum(['SPOT', 'CrossCFD'])
    constrain_type: Enum(['','LIMIT', 'STOP'])
