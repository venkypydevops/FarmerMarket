"""
purpose: Initial wrapper where customer can order his requirements
"""

## TODO: Include pyInquirer and generate bill when each item got added instantly..
import argparse

from bins.GenerateBill import GenerateBill

if __name__ == '__main__':
    print("###################          Welcome to Farmer's Market             ####################\n"
          "**** Farmer's Market have been completed its first anniversary with all our customer support ****\n"
          "**** Here is the Annual offer for our beloved customers. Please take a look and order accordingly ****\n"
                "\t1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)\n"
                "\t2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.\n"
                "\t3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)\n"
                "\t4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples\n")

    parser = argparse.ArgumentParser(description="Input the count of items in numbers (eg: 1,3,10..etc)")
    parser.add_argument("-ch", "--chai", dest="Chai", action="store", help="provide required number of chai",
                        default=0, required=False)
    parser.add_argument("-ap", "--apples", dest="Apples", action="store", help="provide required number of apples",
                        default=0, required=False)
    parser.add_argument("-cf", "--coffee", dest="Coffee", action="store", help="provide required number of Coffee",
                        default=0, required=False)
    parser.add_argument("-mk", "--milk ", dest="Milk", action="store", help="provide required number of Milk",
                        default=0, required=False)
    parser.add_argument("-om", "--oatmeal", dest="Oatmeal", action="store", help="provide required number of Oatmeal",
                        default=0, required=False)

    args = parser.parse_args()
    # Prepare the cart_items list to pass to Products class
    cart_counts = {
        "Chai" : int(args.Chai),
        "Apples": int(args.Apples),
        "Coffee": int(args.Coffee),
        "Milk": int(args.Milk),
        "Oatmeal": int(args.Oatmeal)
    }
    bill = GenerateBill()
    bill._update_products_with_count(cart_counts)
    gt, totalbilling = bill.return_current_cart_bill()
    print("## Grand Total after applying possible offers is: {}".format(gt))
    print(totalbilling)

