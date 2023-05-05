from pydantic import BaseModel, confloat

from sample_package.Asset import Asset, AllAssets
from sample_package.OrderSide import OrderSide


class _BaseOrder(BaseModel):
    side: OrderSide
    base_asset: AllAssets
    quote_asset: AllAssets
    amount: float = confloat(gt=0)
