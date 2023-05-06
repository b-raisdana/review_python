from pydantic import BaseModel, confloat

from trade_order_package.BaseOrder import _BaseOrder


class _OrderAction:
    class Market(BaseModel):
        is_market: bool = True

    class Limit(BaseModel):
        limit: float = confloat(gt=0)

    class Stop(BaseModel):
        stop: float = confloat(gt=0)

    class StopLimit(Limit, Stop):
        pass
        # def __init__(self, limit: float, stop: float):
        #     _OrderAction.Limit.__init__( limit=limit)
        #     _OrderAction.Stop.__init__( stop=stop)
