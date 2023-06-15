from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import DetailView
from .API_Accessor import API_Accessor
from .TI_API_Suite import TI_Orders, TI_Inventory
from django.core.mail import send_mail

import requests
import json


def new_search(request):
    context = {
        'id': '',
        'error': ''
    }
    error = ''
    if request.method == 'POST':

        # Store user credentials and server URL address.
        client_id = ""
        client_secret = ""
        server = "https://transact.ti.com"
        verify_ssl = True

        # Confirm to user.
        catalog = TI_Inventory(server=server, client_id=client_id, client_secret=client_secret, verify=verify_ssl)

        # Get inventory of the OPN below.
        print("\n\n\n# Step 1: Get inventory of the OPN below.")
        opn = request.POST.get('new_search_mpn_field')
        print("\nFirst, we are using the inventory API to get how many items of OPN {} there are.".format(opn))
        response = catalog.get_product_info(opn=opn, verify=verify_ssl)

        code = response.status_code
        server_response = '\nnew_search Response from server: ' + str(code)
        print(server_response)
        if code == 200:

            # Retrieve and process the response for a specific product
            response_info = response.json()

            mpn_ti = response_info['tiPartNumber']
            generic_part_number = response_info['genericPartNumber']
            buy_now_url = response_info['buyNowUrl']
            quantity = response_info['quantity']
            description = response_info['description']
            minimum_order_quantity = response_info['minimumOrderQuantity']
            standard_pack_quantity = response_info['standardPackQuantity']
            exp_ctr_class_num = response_info['exportControlClassificationNumber']
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
            print(exp_ctr_class_num)
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

            prices = []
            for item in price_breaks:
                price_qty = item['priceBreakQuantity']
                print(price_qty)
                price = item['price']
                print(price)
                prices.append({'priceQTY': price_qty, 'price': price})

            # Print the results for debugging
            print("Get information for a specific product by its OPN (Orderable Part Number) status_code:  ")
            print(response.status_code)
            print("Get information for a specific product by its OPN (Orderable Part Number) response:  ")
            print(response_info)
            print("\n------------------------------------------------\n")

            subject = 'Hello from My Django Site'
#            message = 'quantity of ' + str(mpn_ti) + ':____' + str(quantity)
            message = 'my message from django'
            sender = 'pavel87.test@gmail.com'
            recipient_list = ['dolliner.pavel@gmail.com']

            send_mail(subject=subject, message=message, from_email=sender, recipient_list=recipient_list)
#            send_mail(subject, message, sender, recipient_list)

            context = {
                'mpn': mpn_ti,
                'generic_part_number': generic_part_number,
                'buy_now_url': buy_now_url,
                'quantity': quantity,
                'description': description,
                'minimum_order_quantity': minimum_order_quantity,
                'standard_pack_quantity': standard_pack_quantity,
                'export_control_classification_number': exp_ctr_class_num,
                'hts_code': hts_code,
                'pin_count': pin_count,
                'package_type': package_type,
                'package_carrier': package_carrier,
                'custom_reel': custom_reel,
                'life_cycle': life_cycle,
                'currency': currency,
                'prices': prices
            }

            return render(request, 'search/details_handler.html', context)
        else:
            context = {
                'id': '',
                'error': 'Wrong form data'
            }
    return render(request, 'search/new_search.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'search/new_search_dyn.html'
    context_object_name = 'server_response'


def details_handler(request):
    return render(request, 'search/details_handler.html')
