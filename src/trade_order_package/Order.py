from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum

from pydantic.types import Any

from trade_order_package.AbstractOrder import AbstractOrder, AbstractOrderFactory, BaseOrder





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
    def factory(self, _type: _Types, base_properties: BaseOrder):
        match _type:
            case ZzOrder._Types.SpotMarket:
                assert base_properties.is_valid()
                return SpotMarket(base_properties=base_properties)
            case ZzOrder._Types.SpotLimit:
                return SpotMarket
