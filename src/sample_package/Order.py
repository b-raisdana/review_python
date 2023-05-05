from enum import StrEnum

from sample_package.Spot import SpotMarket
from sample_package.BaseOrder import _BaseOrder


class Order:
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
            case Order._Types.SpotMarket:
                assert base_properties.is_valid()
                return SpotMarket(base_properties=base_properties)
            case Order._Types.SpotLimit:
                return SpotMarket