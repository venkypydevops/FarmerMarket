from src.GenerateBill import GenerateBill
from src.Products import Products

def test_billing_case1():
    products = Products()
    cart_counts = {
        "Chai": 1,
        "Apples": 3,
        "Coffee":0,
        "Milk": 1,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 16.61

def test_billing_case2():
    products = Products()
    cart_counts = {
        "Chai": 1,
        "Apples": 1,
        "Coffee":1,
        "Milk": 1,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 20.34

def test_billing_case3():
    products = Products()
    cart_counts = {
        "Chai": 0,
        "Apples": 1,
        "Coffee":0,
        "Milk": 1,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 10.75

def test_billing_case4():
    products = Products()
    cart_counts = {
        "Chai": 0,
        "Apples": 0,
        "Coffee":2,
        "Milk": 0,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 11.23

def test_billing_case5():
    products = Products()
    cart_counts = {
        "Chai": 1,
        "Apples": 3,
        "Coffee":0,
        "Milk": 0,
        "Oatmeal": 0
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 16.61

def test_billing_case6():
    products = Products()
    cart_counts = {
        "Chai": 1,
        "Apples": 5,
        "Coffee":5,
        "Milk": 3,
        "Oatmeal": 2
    }
    products._set_cart_items_count(cart_counts)
    gt, totalbill = GenerateBill().return_current_cart_bill()
    assert gt == 64.93
