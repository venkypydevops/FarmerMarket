from src.bins.GenerateBill import GenerateBill

def test_offers_case1():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 2}),
        "Apples": dict({"code": "AP1", "count": 4}),
        "Coffee": dict({"code": "CF1", "count": 2}),
        "Milk": dict({"code": "MK1", "count": 0}),
        "Oatmeal": dict({"code": "OM1", "count": 1})
    }
    BOGO, APPL, CHMK, APOM = GenerateBill(cart_items).get_offers()
    print(BOGO, APPL, CHMK, APOM)
    assert APPL == 1
    assert BOGO == 1
    assert CHMK == 1
    assert APOM == 1

def test_offers_case2():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 0}),
        "Apples": dict({"code": "AP1", "count": 2}),
        "Coffee": dict({"code": "CF1", "count": 1}),
        "Milk": dict({"code": "MK1", "count": 0}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    BOGO, APPL, CHMK, APOM = GenerateBill(cart_items).get_offers()
    print(BOGO, APPL, CHMK, APOM)
    assert APPL == 0
    assert BOGO == 0
    assert CHMK == 0
    assert APOM == 0

def test_offers_case3():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 1}),
        "Apples": dict({"code": "AP1", "count": 2}),
        "Coffee": dict({"code": "CF1", "count": 0}),
        "Milk": dict({"code": "MK1", "count": 2}),
        "Oatmeal": dict({"code": "OM1", "count": 1})
    }
    BOGO, APPL, CHMK, APOM = GenerateBill(cart_items).get_offers()
    print(BOGO, APPL, CHMK, APOM)
    assert APPL == 0
    assert BOGO == 0
    assert CHMK == 1
    assert APOM == 1

def test_offers_case4():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 0}),
        "Apples": dict({"code": "AP1", "count": 10}),
        "Coffee": dict({"code": "CF1", "count": 5}),
        "Milk": dict({"code": "MK1", "count": 2}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    BOGO, APPL, CHMK, APOM = GenerateBill(cart_items).get_offers()
    print(BOGO, APPL, CHMK, APOM)
    assert APPL == 1
    assert BOGO == 1
    assert CHMK == 0
    assert APOM == 0
