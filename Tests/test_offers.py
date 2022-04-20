from GenerateBill import GenerateBill
from Products import Products

def test_offers_case1():
    products = Products()
    cart_counts = {
        "Chai": 2,
        "Apples": 4,
        "Coffee": 2,
        "Milk": 0,
        "Oatmeal": 1
    }
    products._set_cart_items_count(cart_counts)
    BOGO, APPL, CHMK, APOM = GenerateBill().get_offers()
    assert APPL == 1
    assert BOGO == 1
    assert CHMK == 1
    assert APOM == 1

def test_offers_case2():
    products = Products()
    cart_counts = {
        "Chai": 0,
        "Apples": 2,
        "Coffee": 1,
        "Milk": 0,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    BOGO, APPL, CHMK, APOM = GenerateBill().get_offers()
    assert APPL == 0
    assert BOGO == 0
    assert CHMK == 0
    assert APOM == 0

def test_offers_case3():
    products = Products()
    cart_counts = {
        "Chai": 1,
        "Apples": 2,
        "Coffee": 0,
        "Milk": 2,
        "Oatmeal": 1
    }
    products._set_cart_items_count(cart_counts)
    BOGO, APPL, CHMK, APOM = GenerateBill().get_offers()
    assert APPL == 0
    assert BOGO == 0
    assert CHMK == 1
    assert APOM == 1

def test_offers_case4():
    products = Products()
    cart_counts = {
        "Chai": 0,
        "Apples": 10,
        "Coffee": 5,
        "Milk": 2,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    BOGO, APPL, CHMK, APOM = GenerateBill().get_offers()
    assert APPL == 1
    assert BOGO == 1
    assert CHMK == 0
    assert APOM == 0
