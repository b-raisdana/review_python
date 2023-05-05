from enum import Enum

from pydantic import constr, BaseModel


class Asset(BaseModel):
    name: str
    symbol: str = constr(strip_whitespace=True, to_upper=True, min_length=3, max_length=10)

    def __init__(self, name, symbol, *args, **kwargs):
        super().__init__(*args, {**kwargs, **{name: name, symbol: symbol}})


class AllAssets(Asset, Enum):
    BTC = Asset(name='Bitcoin', symbol='BTC')
    ETH = Asset(name='Ethereum', symbol='ETH'),
    USDT = Asset(name='Tether', symbol='USDT'),
    TRX = Asset(name='Tron', symbol='TRX'),

