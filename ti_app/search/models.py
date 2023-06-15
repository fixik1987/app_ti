from django.db import models
from django.shortcuts import render, redirect
import requests


class Product(models.Model):
    mpn = models.CharField(max_length=100)
    generic_part_number = models.CharField(max_length=100)
    buy_now_url = models.URLField()
    quantity = models.IntegerField()
    description = models.TextField()
    minimum_order_quantity = models.IntegerField()
    standard_pack_quantity = models.IntegerField()
    export_control_classification_number = models.CharField(max_length=50)
    hts_code = models.CharField(max_length=50)
    pin_count = models.IntegerField()
    package_type = models.CharField(max_length=50)
    package_carrier = models.CharField(max_length=100)
    custom_reel = models.BooleanField()
    life_cycle = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    price_break_quantity = models.IntegerField()

    def comp_handler(self):
        url = 'https://transact.ti.com/v1/oauth/accesstoken'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': 'ib4NVBvVFf7eC3HGe5YtrttGxVu9kiVT',
            'client_secret': 'jhyMohTsfMaelXxI'
        }

        response = requests.post(url, headers=headers, data=data)

        code = response.status_code

        # Retrieve and process the authorization response
        response_auth = response.json()
        access_token = response_auth['access_token']
        token_type = response_auth['token_type']
        expires_in = response_auth['expires_in']
        scope = response_auth['scope']
        issued_at = response_auth['issued_at']
        client_id = response_auth['client_id']

        url = 'https://transact.ti.com/v2/store/products/TPS61240IDRVRQ1'
        params = {
            'currency': 'USD',
             'exclude-evms': 'true'
        }
        headers = {
           'accept': 'application/json',
           'Authorization': "Bearer " + access_token
        }

        response = requests.get(url, params=params, headers=headers)

        # Retrieve and process the response for a specific product
        response_info = response.json()

        mpn_ti = response_info['tiPartNumber']
        generic_part_number = response_info['genericPartNumber']
        buy_now_url = response_info['buyNowUrl']
        quantity = response_info['quantity']
        description = response_info['description']
        minimum_order_quantity = response_info['minimumOrderQuantity']
        standard_pack_quantity = response_info['standardPackQuantity']
        export_control_classification_number = response_info['exportControlClassificationNumber']
        hts_code = response_info['htsCode']
        pin_count = response_info['pinCount']
        package_type = response_info['packageType']
        package_carrier = response_info['packageCarrier']
        custom_reel = response_info['customReel']
        life_cycle = response_info['lifeCycle']
        print(mpn_ti)
        print(generic_part_number)
        print(buy_now_url)
        print(quantity)
        print(description)
        print(minimum_order_quantity)
        print(standard_pack_quantity)
        print(export_control_classification_number)
        print(hts_code)
        print(pin_count)
        print(package_type)
        print(package_carrier)
        print(custom_reel)
        print(life_cycle)

        # Access the parsed data
        currency = response_info['pricing'][0]['currency']

        # Extract the values of "priceBreakQuantity"
        pricing = response_info['pricing']
        price_breaks = pricing[0]['priceBreaks']

        # currentObjProduct = Product.objects.get(pk=1)  # Get the desired product

        product = Product(mpn_ti,
                          generic_part_number, 
                          buy_now_url, 
                          quantity, 
                          description, 
                          minimum_order_quantity, 
                          standard_pack_quantity, 
                          export_control_classification_number, 
                          hts_code,
                          pin_count,
                          package_type,
                          package_carrier,
                          custom_reel,
                          life_cycle,
                          currency)

        prices = []
        for item in price_breaks:
            price_qty = item['priceBreakQuantity']
            print(price_qty)
            price = item['price']
            print(price)
            prices.append({'priceQTY': price_qty, 'price': price})


#    product_price = Product.objects.get(pk=1)  # Get the desired product
#
 #   for item in price_breaks:
  #      price_qty = item['priceBreakQuantity']
   #     price_value = item['price']
    #    price = Price(product=product_price, priceQTY=price_qty, price=price_value)
     #   price.save()





        # Print the results for debugging
        print("Get information for a specific product by its OPN (Orderable Part Number) status_code:  ")
        print(response.status_code)
        print("Get information for a specific product by its OPN (Orderable Part Number) response:  ")
        print(response_info)
        print("\n------------------------------------------------\n")

        return render(self, 'search/details-handler.html', product)
