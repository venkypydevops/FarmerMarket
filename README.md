# FarmerMarket

  ### Welcome to Farmer's Market 
  Farmers market is the place where customers can order below products with reasonable price and product quality
          
          Chai: $3.11
          Apples: $6.00
          Coffee: $11.23
          Milk: $4.75
          Oatmeal: $3.69


  Farmer's Market have been completed its first anniversary with all our customer support.  
  Here is the Annual offer for our beloved customers. Please take a look and order accordingly

  ```
      1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
      2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
      3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
      4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples
```
               
## Usage

How to place the Order ?

  1. Checkout the docker-container from docker-public hub
      ``docker ``
  2. Run the container
      ```docker run <container-id>```
  3. Go to the live container
      ```docker run -it <container-id> /bin/bash```
  4. Run the below command to place the order 
      ```python3 PlaceOrder.py --hlep``` which will return the usage as below
      ```-ch CHAI, --chai CHAI 
                        provide required number of chai
      -ap APPLES, --apples APPLES
                        provide required number of apples
      -cf COFFEE, --coffee COFFEE
                        provide required number of Coffee
      -mk MILK, --milk  MILK
                        provide required number of Milk
      -om OATMEAL, --oatmeal OATMEAL
                        provide required number of Oatmeal```
                    
# Sample Execution

Placing Order 
```
> python PlaceOrder.py  -ap 4 -cf 2 -ch 1 -mk 3 -om 1

## Grand Total after applying possible offers is: 36.53
| Item         | OFFER    | price     |
|:-------------|:---------|:----------|
| CF1          |          | 11.23     |
| CF1          |          | 11.23     |
|              | BOGO     | -11.23    |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| CH1          |          | 3.11      |
| MK1          |          | 4.75      |
|              | CHMK     | -4.75     |
| MK1          |          | 4.75      |
| MK1          |          | 4.75      |
| OM1          |          | 3.69      |
|              | APOM     | -9.0      |
| :----------- | -------- | --------: |
| Grand-Total  |          | 36.53     |

```