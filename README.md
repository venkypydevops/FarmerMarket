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

### Standalone

1. checkout the git repo
    ```git clone https://github.com/venkypydevops/FarmerMarket.git <local-project-dir>```
2. Execute the placeorder command with required cart items
    ```python PlaceOrder.py  -ap 4 -cf 2 -ch 1 -mk 3 -om 2```

### Container
1. checkout the git repo
    ```git clone https://github.com/venkypydevops/FarmerMarket.git <local-project-dir>```
2. Run the Dockerfile to create image
    ``` docker build - < Dockerfile```
3. Run the created image to create the container on it
    ```docker run <Image-ID>```
4. Get the container ID using below command
    ```docker ps```
5. Go to the live container and place the order
    ```docker exec -it <container-id> /bin/bash```
6. (OR) Directly get the container from public-docker-hub by pulling it to local repo

    `C:\Users\user\OneDrive\Desktop\DockerHub>docker pull venkypydevops/farmersmarket:fmkt_2.0
fmkt_2.0: Pulling from venkypydevops/farmersmarket
Digest: sha256:fa7c31ef0d2fafb6c959a5243bb9b24e243df4f8c26d6a618667e9cd1e9866b2
Status: Image is up to date for venkypydevops/farmersmarket:fmkt_2.0
docker.io/venkypydevops/farmersmarket:fmkt_2.0`

    Repo-url : https://hub.docker.com/layers/203913965/venkypydevops/farmersmarket/fmkt_2.0/images/sha256-fa7c31ef0d2fafb6c959a5243bb9b24e243df4f8c26d6a618667e9cd1e9866b2?context=repo

7. Run the below command to place the order 
    ```python3 PlaceOrder.py --hlep``` 
    which will return the usage as below
    ```
    -ch CHAI, --chai CHAI 
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

# Sample execution from docker container

```C:\Users\user>docker ps
CONTAINER ID   IMAGE          COMMAND            CREATED              STATUS              PORTS     NAMES
5778814e279d   eadc5ed71a66   "sleep infinity"   16 seconds ago       Up 15 seconds                 relaxed_sanderson
71e3d92d98c1   eadc5ed71a66   "sleep infinity"   About a minute ago   Up About a minute             farmersmarket

C:\Users\user>docker exec -it 5778814e279d /bin/bash
root@5778814e279d:/FarmerMarket# ls -lrt
total 32
-rwxr-xr-x 1 root root   17 Apr 16 17:11 requirements.txt
-rwxr-xr-x 1 root root 4687 Apr 20 10:05 Products.py
-rwxr-xr-x 1 root root 2436 Apr 20 10:17 PlaceOrder.py
-rwxr-xr-x 1 root root 4566 Apr 20 10:17 GenerateBill.py
-rwxr-xr-x 1 root root 1607 Apr 20 10:32 test_offers.py
-rwxr-xr-x 1 root root 2020 Apr 20 10:32 test_billing.py
root@5778814e279d:/FarmerMarket# python3 PlaceOrder.py -ap 5 -mk 2 -cf 3 -ch 2 -om 4
###################          Welcome to Farmer's Market             ####################
**** Farmer's Market have been completed its first anniversary with all our customer support ****
**** Here is the Annual offer for our beloved customers. Please take a look and order accordingly ****
        1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
        2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
        3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
        4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

## Grand Total after applying possible offers is: 59.44
| Item         | OFFER    | price     |
|:-------------|:---------|:----------|
| CF1          |          | 11.23     |
| CF1          |          | 11.23     |
|              | BOGO     | -11.23    |
| CF1          |          | 11.23     |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| AP1          |          | 6.0       |
|              | APPL     | -1.5      |
| CH1          |          | 3.11      |
| CH1          |          | 3.11      |
| MK1          |          | 4.75      |
|              | CHMK     | -4.75     |
| MK1          |          | 4.75      |
| OM1          |          | 3.69      |
|              | APOM     | -11.25    |
| OM1          |          | 3.69      |
| OM1          |          | 3.69      |
| OM1          |          | 3.69      |
| :----------- | -------- | --------: |
| Grand-Total  |          | 59.44     |
root@5778814e279d:/FarmerMarket#```
