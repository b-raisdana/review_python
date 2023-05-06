from enum import Enum

from pydantic import constr, BaseModel


class Asset(BaseModel):
    name: str
    symbol: constr(regex=r'[A-Z][A-Z0-9]{2,9}')


class AllAssets(Enum):
    BTC = Asset(name='Bitcoin', symbol='BTC')
    ETH = Asset(name='Ethereum', symbol='ETH'),
    USDT = Asset(name='Tether', symbol='USDT'),
    TRX = Asset(name='Tron', symbol='TRX'),

