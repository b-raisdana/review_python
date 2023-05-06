from __future__ import annotations
from trade_order_package.Asset import AllAssets
from trade_order_package.OrderSide import OrderSide
from trade_order_package.AbstractOrder import AbstractOrder, AbstractOrderFactory


class SpotFactory(AbstractOrderFactory):
    # market_type: bool = True

    @classmethod
    def factory_market(cls, base_asset: AllAssets, quote_asset: AllAssets,
                       amount: float, side: OrderSide) -> SpotMarket:
        return SpotMarket(base_asset=base_asset, quote_asset=quote_asset,
                          amount=amount, side=side)

    @classmethod
    def factory_limit(cls, base_asset: AllAssets, quote_asset: AllAssets,
                      amount: float, side: OrderSide, limit: float):
        return SpotLimit(base_asset=base_asset, quote_asset=quote_asset,
                         amount=amount, side=side, limit=limit)

    @classmethod
    def factory_stop(cls, base_asset: AllAssets, quote_asset: AllAssets,
                     amount: float, side: OrderSide, stop: float):
        return SpotStop(base_asset=base_asset, quote_asset=quote_asset,
                        amount=amount, side=side, stop=stop)

    @classmethod
    def factory_stop_limit(cls, base_asset: AllAssets, quote_asset: AllAssets,
                           amount: float, side: OrderSide, limit: float, stop: float):
        return SpotStopLimit(base_asset=base_asset, quote_asset=quote_asset,
                             amount=amount, side=side, limit=limit, stop=stop)


class _SpotBase:
    def __repr__(self):
        return 'SPOT' + super().__repr__()


class SpotMarket(AbstractOrder.Market):

    def do_order(self):
        pass

    def __repr__(self):
        return 'SPOT' + super().__repr__()


class SpotLimit(_SpotBase, AbstractOrder.Limit):
    limit: float

    def do_order(self):
        pass


class SpotStop(_SpotBase, AbstractOrder.Stop):
    stop: float

    def do_order(self):
        pass


class SpotStopLimit(_SpotBase, AbstractOrder.StopLimit):
    limit: float

    def do_order(self):
        pass

# class _SpotOrder(AbstractOrder):
#     is_spot: bool = True
#
#
# class SpotMarket(_OrderAction.Market, _SpotOrder):
#     def __init__(self, base_properties: AbstractOrder) -> object:
#         super().__init__()
#         self.amount = base_properties.amount
#         self.side = base_properties.side
#         self.base_asset = base_properties.base_asset
#         self.quote_asset = base_properties.quote_asset
#
#     def __repr__(self):
#         if self.side == OrderSide.BUY:
#             return f'{self.base_asset}<{self.amount}{self.quote_asset}'
#         if self.side == OrderSide.BUY:
#             return f'{self.amount}{self.base_asset}>{self.quote_asset}'


# class SpotLimit(_OrderAction.Limit, SpotMarket):
#     def __init__(self, base_properties: AbstractOrder, action_properties: _OrderAction.Limit):
#         SpotMarket.__init__(base_properties=base_properties)
#         self.limit = action_properties.limit
#
#     def __repr__(self):
#         return super.__repr__() + f'@{self.limit}'
