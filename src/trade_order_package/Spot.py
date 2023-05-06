from trade_order_package.OrderSide import OrderSide
from trade_order_package.BaseOrder import _BaseOrder
from trade_order_package._OrderAction import _OrderAction


class _SpotOrder(_BaseOrder):
    is_spot: bool = True


class SpotMarket(_OrderAction.Market, _SpotOrder):
    def __init__(self, base_properties: _BaseOrder) -> object:
        super().__init__()
        self.amount = base_properties.amount
        self.side = base_properties.side
        self.base_asset = base_properties.base_asset
        self.quote_asset = base_properties.quote_asset

    def __repr__(self):
        if self.side == OrderSide.BUY:
            return f'{self.base_asset}<{self.amount}{self.quote_asset}'
        if self.side == OrderSide.BUY:
            return f'{self.amount}{self.base_asset}>{self.quote_asset}'


class SpotLimit(_OrderAction.Limit, SpotMarket):
    def __init__(self, base_properties: _BaseOrder, action_properties: _OrderAction.Limit):
        SpotMarket.__init__(base_properties=base_properties)
        self.limit = action_properties.limit

    def __repr__(self):
        return super.__repr__() + f'@{self.limit}'
