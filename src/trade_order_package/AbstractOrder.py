from __future__ import annotations

from dataclasses import dataclass
from pydantic import BaseModel, confloat
from trade_order_package.Asset import Asset, AllAssets
from trade_order_package.OrderSide import OrderSide
from abc import abstractmethod, ABC, abstractclassmethod


class AbstractOrderFactory(BaseModel, ABC):
    @classmethod
    @abstractmethod
    def factory_market(cls, base_asset: AllAssets, quote_asset: AllAssets,
                       amount: float, side: OrderSide) -> AbstractOrder.Market:
        pass

    @classmethod
    @abstractmethod
    def factory_limit(cls, base_asset: AllAssets, quote_asset: AllAssets,
                      amount: float, side: OrderSide, limit: float) -> AbstractOrder.Limit:
        pass

    @classmethod
    @abstractmethod
    def factory_stop(cls, base_asset: AllAssets, quote_asset: AllAssets,
                     amount: float, side: OrderSide, stop: float) -> AbstractOrder.Stop:
        pass

    @classmethod
    @abstractmethod
    def factory_stop_limit(cls, base_asset: AllAssets, quote_asset: AllAssets,
                           amount: float, side: OrderSide, limit: float, stop: float) -> AbstractOrder.StopLimit:
        pass


class BaseOrder(BaseModel, ABC):
    side: OrderSide
    base_asset: AllAssets
    quote_asset: AllAssets
    amount: float = confloat(gt=0)

    # market_type: Enum(['SPOT', 'CrossCFD'])
    # constrain_type: Enum(['MARKET', 'LIMIT', 'STOP'])

    @abstractmethod
    def do_order(self):
        pass

    def __repr__(self):
        if self.side == OrderSide.BUY:
            return f'{self.base_asset}<{self.amount}{self.quote_asset}'
        if self.side == OrderSide.BUY:
            return f'{self.amount}{self.base_asset}>{self.quote_asset}'


class AbstractOrder(ABC):
    class Market(BaseOrder, ABC):
        pass

    class Limit(BaseOrder, ABC):
        limit: float

        def __repr__(self):
            return super().__repr__() + f'@{self.limit}'

    class Stop(BaseOrder, ABC):
        stop: float

        def __repr__(self):
            return super().__repr__() + f'#{self.stop}'

    class StopLimit(Limit, Stop, ABC):
        pass

        def __repr__(self):
            return super().__repr__() + f'@{self.limit}#{self.stop}'
