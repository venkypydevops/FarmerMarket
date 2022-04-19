import logging
import traceback

from conf.Products import Products
from tabulate import tabulate

class GenerateBill():
    """
    Purpose: GenerateBill generates the bill for the cart-items ordered by the customer
    """
    def __init__(self):
        self.prods = Products()

    def _update_products_with_count(self, cart_counts):
        """
        :param cart_counts: cart counts need to be updated
        :return: updated Products
        """
        try:
            self.prods._set_cart_items_count(cart_counts)
        except Exception as E:
            logging.debug(traceback.print_exc())
            logging.info('** Caught exception : ' + str(E))

    def get_offers(self):
        """
        :return: Return the applied offers
        """
        BOGO, APPL, CHMK, APOM = 0,0,0,0
        try:
            # 1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
            BOGO = 1 if self.prods._get_coffee_count() > 1 else 0

            # 2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
            APPL = 1 if self.prods._get_apples_count() > 2 else 0

            # 3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
            CHMK = 1 if self.prods._get_chai_count() > 0 else 0

            # 4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
            APOM = 1 if self.prods._get_oatmeal_count() > 0 else 0


        except Exception as E:
            logging.debug(traceback.print_exc())
            logging.info('** Caught exception : ' + str(E))

        finally:
            return BOGO, APPL, CHMK, APOM

    def return_current_cart_bill(self):
        """
        :return: Calculate the cart value by applying the offers
        """
        global grandtotal
        BOGO, APPL, CHMK, APOM = self.get_offers()
        billing_data = []
        headers = ['Item', 'OFFER', 'price']

        try:
            if self.prods._get_coffee_count():
                for cf in range(1,self.prods._get_coffee_count()+1):
                    billing_data.append([self.prods._get_coffee_code(), '', self.prods._get_coffee_cost()])
                    # To apply the BOGO offer
                    if cf%2 == 0:
                        billing_data.append(['', 'BOGO', self.prods._get_coffee_cost()*-1])

            if self.prods._get_apples_count():
                for ap in range(1,self.prods._get_apples_count()+1):
                    billing_data.append([self.prods._get_apples_code(), '', self.prods._get_apples_cost()])
                    if APPL:
                        billing_data.append(['', 'APPL', -1.5])

            if self.prods._get_chai_count():
                for ch in range(1,self.prods._get_chai_count()+1):
                    billing_data.append([self.prods._get_chai_code(), '', self.prods._get_chai_cost()])

            if self.prods._get_milk_count():
                for mk in range(1,self.prods._get_milk_count()+1):
                    billing_data.append([self.prods._get_milk_code(), '', self.prods._get_milk_cost()])
                    ## CHMK is used only once per bill - So, once consumed make the offer disable for current bill
                    if CHMK:
                        billing_data.append(['', 'CHMK', self.prods._get_milk_cost()*-1])
                        CHMK = 0

            if self.prods._get_oatmeal_count():
                for om in range(1,self.prods._get_oatmeal_count()+1):
                    billing_data.append([self.prods._get_oatmeal_code(), '', self.prods._get_oatmeal_cost()])
                    if APOM and self.prods._get_apples_count()>0:
                        if APPL:
                            self.prods._set_apples_cost(4.50)
                        AP1_cost = self.prods._get_apples_count() * self.prods._get_apples_cost()
                        billing_data.append(['', 'APOM', (AP1_cost/2) * -1])
                        ## Disable APOM offer once 50% discount applied on apples
                        APOM = 0

            grandtotal = round(sum(float(bdata[2]) for bdata in billing_data),2)
            billing_data.append([':-----------', '--------', '--------:'])
            billing_data.append(['Grand-Total', '', grandtotal])


        except Exception as E:
            logging.debug(traceback.print_exc())
            logging.info('** Caught exception : ' + str(E))

        finally:
            return grandtotal, tabulate(billing_data, headers=headers, tablefmt='pipe')
