from bins.GenerateBill import GenerateBill

def test_billing_case1():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 1}),
        "Apples": dict({"code": "AP1", "count": 3}),
        "Coffee": dict({"code": "CF1", "count": 0}),
        "Milk": dict({"code": "MK1", "count": 1}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 16.61

def test_billing_case2():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 1}),
        "Apples": dict({"code": "AP1", "count": 1}),
        "Coffee": dict({"code": "CF1", "count": 1}),
        "Milk": dict({"code": "MK1", "count": 1}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 20.34

def test_billing_case3():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 0}),
        "Apples": dict({"code": "AP1", "count": 1}),
        "Coffee": dict({"code": "CF1", "count": 0}),
        "Milk": dict({"code": "MK1", "count": 1}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 10.75

def test_billing_case4():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 0}),
        "Apples": dict({"code": "AP1", "count": 0}),
        "Coffee": dict({"code": "CF1", "count": 2}),
        "Milk": dict({"code": "MK1", "count": 0}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 11.23

def test_billing_case5():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 1}),
        "Apples": dict({"code": "AP1", "count": 3}),
        "Coffee": dict({"code": "CF1", "count": 0}),
        "Milk": dict({"code": "MK1", "count": 0}),
        "Oatmeal": dict({"code": "OM1", "count": 0})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 16.61

def test_billing_case6():
    cart_items = {
        "Chai": dict({"code": "CH1", "count": 1}),
        "Apples": dict({"code": "AP1", "count": 5}),
        "Coffee": dict({"code": "CF1", "count": 5}),
        "Milk": dict({"code": "MK1", "count": 3}),
        "Oatmeal": dict({"code": "OM1", "count": 2})
    }
    gt, totalbill = GenerateBill(cart_items).return_current_cart_bill()
    assert gt == 64.93