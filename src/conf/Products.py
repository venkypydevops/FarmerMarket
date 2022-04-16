"""
Purpose: Define the products with costs as constant variables to use through out the project
"""
class Products:
    def __init__(self):
        pass
    def _get_product_details(self):
        Products = {
            "Chai": dict({"code": "CH1", "cost": 3.11}),
            "Apples": dict({"code": "AP1", "cost": 6.00}),
            "Coffee": dict({"code": "CF1", "cost": 11.23}),
            "Milk": dict({"code": "MK1", "cost": 4.75}),
            "Oatmeal": dict({"code": "OM1", "cost": 3.69})
        }
        return Products
