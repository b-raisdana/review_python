from pydantic import ValidationError

from trade_order_package.Asset import Asset


def test_assets_name_and_symbol():
    num_test = 0
    # wrong usage of Asset
    catch_wrong_symbol = False
    try:
        t_wrong_asset = Asset(symbol='BB', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert catch_wrong_symbol

    catch_wrong_symbol = False
    try:
        t_wrong_asset = Asset(symbol='bb', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert catch_wrong_symbol

    catch_wrong_symbol = False
    try:
        t_right_asset = Asset(symbol='0BBB', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert catch_wrong_symbol

    catch_wrong_symbol = False
    try:
        t_right_asset = Asset(symbol='bbb', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert catch_wrong_symbol

    # right usage of Asset

    catch_right_symbol = True
    try:
        t_right_asset = Asset(symbol='BBB', name='b')
    except ValidationError as err:
        catch_right_symbol = False
    assert catch_right_symbol

    catch_wrong_symbol = False
    try:
        t_right_asset = Asset(symbol='BBB', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert not catch_wrong_symbol

    catch_wrong_symbol = False
    try:
        t_right_asset = Asset(symbol='BBBBBBBBBBBBBBBBB', name='b')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert not catch_wrong_symbol

    catch_wrong_symbol = False
    try:
        t_right_asset = Asset(symbol='BBB', name='bbbbbbbbbbbbbbbbbbbbb')
    except ValidationError as err:
        catch_wrong_symbol = True
    assert not catch_wrong_symbol
