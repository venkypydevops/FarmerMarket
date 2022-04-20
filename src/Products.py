"""
Purpose: Define the products with costs as constant variables to use through out the project
"""
class Products:
    def __init__(self):
        """
        Purpose: Define products as they are constants for this scenario
        """
        self.products = {
            "Chai": dict({"code": "CH1", "cost": 3.11}),
            "Apples": dict({"code": "AP1", "cost": 6.00}),
            "Coffee": dict({"code": "CF1", "cost": 11.23}),
            "Milk": dict({"code": "MK1", "cost": 4.75}),
            "Oatmeal": dict({"code": "OM1", "cost": 3.69})
        }

    def _set_cart_items_count(self, cart_counts):
        """
        :param cart_counts: Get the orders from the end-user and Make the Products class updated with that dynamic information
        :return: Updated self.products dict
        """
        self.products["Chai"]["count"] = cart_counts["Chai"]
        self.products["Apples"]["count"] = cart_counts["Apples"]
        self.products["Coffee"]["count"] = cart_counts["Coffee"]
        self.products["Milk"]["count"] = cart_counts["Milk"]
        self.products["Oatmeal"]["count"] = cart_counts["Oatmeal"]

    def _get_chai_code(self):
        """
        :return: returns code of the chai product
        """
        return self.products['Chai']['code']

    def _get_chai_cost(self):
        """
        :return: returns cost of the chai
        """
        return self.products['Chai']['cost']

    def _get_chai_count(self):
        """
        :return: returns no.of the chai ordered
        """
        return self.products['Chai']['count']

    def _get_apples_code(self):
        """
        :return: returns code of the apples product
        """
        return self.products['Apples']['code']

    def _get_apples_cost(self):
        """
        :return: returns cost of the apples
        """
        return self.products['Apples']['cost']

    def _get_apples_count(self):
        """
        :return: returns no.of the apples ordered
        """
        return self.products['Apples']['count']

    def _get_coffee_code(self):
        """
        :return: returns code of the Coffee product
        """
        return self.products['Coffee']['code']

    def _get_coffee_cost(self):
        """
        :return: returns the cost of the coffee
        """
        return self.products['Coffee']['cost']

    def _get_coffee_count(self):
        """
        :return: returns the count of the coffee ordered
        """
        return self.products['Coffee']['count']

    def _get_milk_code(self):
        """
        :return: returns the code of the milk product
        """
        return self.products['Milk']['code']

    def _get_milk_cost(self):
        """
        :return: returns the cost of the milk
        """
        return self.products['Milk']['cost']

    def _get_milk_count(self):
        """
        :return: returns the count of the milk ordered
        """
        return self.products['Milk']['count']

    def _get_oatmeal_code(self):
        """
        :return: returns the code of the oatmeal product
        """
        return self.products['Oatmeal']['code']

    def _get_oatmeal_cost(self):
        """
        :return: returns the cost of the oatmeal
        """
        return self.products['Oatmeal']['cost']

    def _get_oatmeal_count(self):
        """
        :return: returns the no.of oatmeal ordered
        """
        return self.products['Oatmeal']['count']

    ## When there is discount and vary in the price of product.. set the value

    def _set_chai_cost(self, cost):
        """
        :param cost: get the new cost of the chai
        :return: set the value to Products
        """
        self.products['Chai']['cost'] = cost

    def _set_apples_cost(self, cost):
        """
        :param cost: get the new cost of the apples
        :return: set the value to Products
        """
        self.products['Apples']['cost'] = cost

    def _set_coffee_cost(self, cost):
        """
        :param cost: get the new cost of the coffee
        :return: set the value to Products
        """
        self.products['Coffee']['cost'] = cost

    def _set_milk_cost(self, cost):
        """
        :param cost: get the new cost of the milk
        :return: set the value to Products
        """
        self.products['Milk']['cost'] = cost

    def _set_oatmeal_cost(self, cost):
        """
        :param cost: get the new cost of the oatmeal
        :return: set the value to Products
        """
        self.products['Oatmeal']['cost'] = cost
