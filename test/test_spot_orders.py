from trade_order_package.Asset import AllAssets
from trade_order_package.OrderSide import OrderSide
from trade_order_package.Spot import SpotMarket, SpotLimit, SpotStop, SpotStopLimit, SpotFactory


def test_market_order():
    t_market_order = SpotFactory.factory_market(base_asset=AllAssets.BTC, quote_asset=AllAssets.TRX, amount=0.5,
                                                side=OrderSide.BUY)
    assert t_market_order.__repr__() == 'SPOT' +
    assert True
