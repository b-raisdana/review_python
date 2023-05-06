from abc import ABC, abstractmethod
from enum import StrEnum

from pydantic import BaseModel

from trade_order_package.Asset import Asset
from trade_order_package.Spot import SpotMarket
from trade_order_package.BaseOrder import _BaseOrder


class SpotOrder(_BaseOrder):
    market_type: bool = True

    @classmethod
    def factory_market(cls, base_properties: _BaseOrder):
        return SpotOrder(base_properties)

    @classmethod
    def factory_limit(cls, base_properties: _BaseOrder, limit: float):
        _t = SpotOrder(base_properties)

    @abstractmethod
    def factory_stop(self, stop: float):
        pass

    @abstractmethod
    def factory_stop_limit(self, limit: float, stop: float):
        pass


class SpotOrder(OrderConstrained):
    def factory_market(self):
        super().factory_market()

    def factory_limit(self, limit: float):
        s


class ZzOrder:
    class _Types(StrEnum):
        SpotMarket = 'SPOT_MARKET'
        SpotLimit = 'SPOT_LIMIT'
        SpotStop = 'SPOT_STOP'
        SpotStopLimit = 'SPOT_LIMIT'
        CrossCFDMarket = 'CROSS_CFD_MARKET'
        CrossCFDLimit = 'CROSS_CFD_LIMIT'
        CrossCFDStop = 'CROSS_CFD_STOP'
        CrossCFDStopLimit = 'CROSS_CFD_LIMIT'

    @staticmethod
    def factory(self, _type: _Types, base_properties: _BaseOrder):
        match _type:
            case ZzOrder._Types.SpotMarket:
                assert base_properties.is_valid()
                return SpotMarket(base_properties=base_properties)
            case ZzOrder._Types.SpotLimit:
                return SpotMarket
