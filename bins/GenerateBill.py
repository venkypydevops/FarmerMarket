from conf.Products import Products
from tabulate import tabulate

class GenerateBill():
    def __init__(self, cart_items):
        self.cart_items = cart_items
        self.products = Products()._get_product_details()

    def get_offers(self):
        """
        :return: Return the applied offers
        """
        print(self.cart_items)
        BOGO, APPL, CHMK, APOM = 0,0,0,0
        try:
            # 1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
            BOGO = 1 if self.cart_items['Coffee']['count'] > 1 else 0


            # 2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
            APPL = 1 if self.cart_items['Apples']['count'] > 2 else 0

            # 3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
            CHMK = 1 if self.cart_items['Chai']['count'] > 0 else 0

            # 4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
            APOM = 1 if self.cart_items['Oatmeal']['count'] > 0 else 0

        except Exception as E:
            print(E)

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
            if self.cart_items['Coffee']['count']:
                for cf in range(1,self.cart_items['Coffee']['count']+1):
                    billing_data.append([self.products['Coffee']['code'], '', self.products['Coffee']['cost']])
                    # To apply the BOGO offer
                    if cf%2 == 0:
                        billing_data.append(['', 'BOGO', self.products['Coffee']['cost']*-1])

            if self.cart_items['Apples']['count']:
                for ap in range(1,self.cart_items['Apples']['count']+1):
                    billing_data.append([self.products['Apples']['code'], '', self.products['Apples']['cost']])
                    if APPL:
                        billing_data.append(['', 'APPL', -1.5])

            if self.cart_items['Chai']['count']:
                for ch in range(1,self.cart_items['Chai']['count']+1):
                    billing_data.append([self.products['Chai']['code'], '', self.products['Chai']['cost']])

            if self.cart_items['Milk']['count']:
                for mk in range(1,self.cart_items['Milk']['count']+1):
                    billing_data.append([self.products['Milk']['code'], '', self.products['Milk']['cost']])
                    ## CHMK is used only once per bill - So, once consumed make the offer disable for current bill
                    if CHMK:
                        billing_data.append(['', 'CHMK', self.products['Milk']['cost']*-1])
                        CHMK = 0

            if self.cart_items['Oatmeal']['count']:
                for om in range(1,self.cart_items['Oatmeal']['count']+1):
                    billing_data.append([self.products['Oatmeal']['code'], '', self.products['Oatmeal']['cost']])
                    if APOM and self.cart_items['Apples']['count']>0:
                        AP1_cost = self.cart_items['Apples']['count'] * 4.50 if APPL else self.cart_items['Apples'][
                                                                                              'count'] * \
                                                                                          self.products['Apples']['cost']
                        billing_data.append(['', 'APOM', (AP1_cost/2) * -1])
                        ## Disable APOM offer once 50% discount applied on apples
                        APOM = 0

            grandtotal = round(sum(float(bdata[2]) for bdata in billing_data),2)
            billing_data.append([':-----------', '--------', '--------:'])
            billing_data.append(['Grand-Total', '', grandtotal])

        except Exception as E:
            print(E)

        finally:
            return grandtotal, tabulate(billing_data, headers=headers, tablefmt='pipe')
