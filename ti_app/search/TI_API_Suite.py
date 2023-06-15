# Copyright (C) 2022 Texas Instruments Incorporated
#
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions 
# are met:
#
#   Redistributions of source code must retain the above copyright 
#   notice, this list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the 
#   documentation and/or other materials provided with the   
#   distribution.
#
#   Neither the name of Texas Instruments Incorporated nor the names of
#   its contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT 
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT 
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT 
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .API_Accessor import API_Accessor

class TI_AdvancedShippingNotifications:

    """
    API to retrieve ASN information for orders.
    """

    def retrieve_asn(self, orderNumber, waybillNumber,
        requestCommercialInvoicePDF=False, requestWaybillPDF=False, headers = {}, verify=True
        ):

        """
        Retrieve Advanced Shipping Notifications (ASN) and related document information.
        """

        # URL from which to retrieve ASN.
        url = "{}/v2/store/orders/{}/advanced-shipment-notices/{}".format(self.server, orderNumber, waybillNumber)

        # Append parameters onto URL.
        url += "?requestCommercialInvoicePDF={}".format(requestCommercialInvoicePDF)
        url += "&requestWaybillPDF={}".format(requestWaybillPDF)
        
        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def retrieve_asn_test(
        self, requestCommercialInvoicePDF=False, requestWaybillPDF=False, headers = {}, verify=True
        ):

        """
        Retrieve test Advanced Shipping Notifications (ASN) and related document information.
        """

        # URL from which to retrieve ASN.
        url = "{}/v2/store/orders/{}/advanced-shipment-notices/{}/test".format(self.server, 'T10999999', '499999999')

        # Append parameters onto URL.
        url += "?requestCommercialInvoicePDF={}".format(requestCommercialInvoicePDF)
        url += "&requestWaybillPDF={}".format(requestWaybillPDF)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)
        
    def __init__(self, client_id, client_secret, server, verify=True):

        """
        Creates object through which to interact with TI ASN retrieve API.
        """

        # Store API server. It should be formatted as "https://example.server.com".
        self.server = server

        # Get API access object based on given information: url, client ID, and client secret.
        self.api = API_Accessor(server=server, client_id=client_id, client_secret=client_secret, verify=verify)

class TI_FinancialDocuments:

    """
    API to retrieve financial documents for orders.
    """

    def retrieve_financial_document(self, orderNumber, documentNumber, requestPDF=False, headers = {}, verify=True):

        """
        Retrieve financial invoice and other related document information.
        """

        # URL from which to retrieve financial document.
        url = "{}/v2/store/orders/{}/financial-documents/{}".format(self.server, orderNumber, documentNumber)
        url += "?requestPDF={}".format(requestPDF)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify, status_code=200)

    def retrieve_financial_document_test(self, requestPDF=False, headers = {}, verify=True):

        """
        Retrieve test financial invoice and other related document information.
        """

        # URL from which to retrieve financial document.
        url = "{}/v2/store/orders/{}/financial-documents/{}/test".format(self.server, 'T10999999', '5999999999')
        url += "?requestPDF={}".format(requestPDF)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify, status_code=200)
        
    def __init__(self, client_id, client_secret, server, verify=True):

        """
        Creates object through which to interact with TI financial document retrieve API.
        """

        # Store API server. It should be formatted as "https://example.server.com".
        self.server = server

        # Get API access object based on given information: url, client ID, and client secret.
        self.api = API_Accessor(server=server, client_id=client_id, client_secret=client_secret, verify=verify)

class TI_Orders:

    """
    API to place orders on the TI store.
    """

    def get_orders(self, startDate = "", endDate = "", headers = {}, verify=True):

        """
        List TI Store orders.
        """

        # URL from which to get orders, and add parameters (without default values).
        url = "{}/v2/store/orders/".format(self.server)
        url += "?startDate={}".format(startDate) if startDate else ""
        url += "{}endDate={}".format("&" if startDate else "?", endDate) if endDate else ""

        # Make request from the Apigee access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def post_order(self, json, headers = {}, verify=True):

        """
        Create a TI Store order. Passes data as a JSON object.
        """

        # URL onto which to post an order.
        url = "{}/v2/store/orders/".format(self.server)

        # Make request from the Apigee access object.
        return self.api.post(url=url, json=json, headers=headers, verify=verify)

    def post_order_test(self, json, headers = {}, verify=True):

        """
        Create a TI Store order. Passes data through a JSON object.
        """

        # URL onto which to post an order.
        url = "{}/v2/store/orders/test".format(self.server)

        # Make request from the Apigee access object.
        return self.api.post(url=url, json=json, headers=headers, verify=verify, status_code=201)

    def get_delivery_cost(self, country, currency, quantity, headers = {}, verify=True):

        """
        Get approximate delivery costs for orders.
        """

        # URL from which to retrieve delivery costs.
        url = "{}/v2/store/orders/deliveryCost".format(self.server)
        url += "?regionCode={}".format(country)
        url += "&currencyCode={}".format(currency)
        url == "&quantity={}".format(quantity)

        # Make request from the Apigee access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def get_order_details(self, orderNumber, headers = {}, verify=True):

        """
        Get details about a specific order.
        """
        # URL from which to retrieve order details.
        # The orderNumber parameter is passed as a webpage rather than a URL parameter.
        url = "{}/v2/store/orders/{}".format(self.server, orderNumber)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def __init__(self, client_id, client_secret, server, verify=True):

        """
        Creates object through which to interact with TI Store orders API.
        """

        # Store API server. It should be formatted as "https://example.server.com".
        self.server = server

        # Get API access object based on given information: url, client ID, and client secret.
        self.api = API_Accessor(server=server, client_id=client_id, client_secret=client_secret, verify=verify)

class TI_Inventory:

    """
    API to browse the TI store inventory and view individual product information.
    """

    def get_products(self, gpn, page, size, currency="USD", excludeEVMs=True, headers = {}, verify=True):

        """
        Function which returns a pageable list of TI Store products.
        """

        # URL from which to get the data.
        url = "{}/v2/store/products".format(self.server)

        # Append parameters onto URL.
        url += "?gpn={}".format(gpn)
        url += "&page={}".format(page)
        url += "&size={}".format(size)
        url += "&currency={}".format(currency)
        url += "&exclude-evms={}".format(excludeEVMs)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def get_products_catalog(self, currency="USD", excludeEVMs=True, headers = {}, verify=True):

        """
        Function which returns a full catalog of parts available to purchase from the TI Store.
        """

        # URL from which to get the data.
        url = "{}/v2/store/products/catalog".format(self.server)

        # Append parameters onto URL.        
        url += "?currency={}".format(currency)
        url += "&exclude-evms={}".format(excludeEVMs)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def get_product_info(self, opn, currency="USD", excludeEVMs=True, headers = {}, verify=True):

        """
        Function which returns information about a specific product by its Orderable Part Number (OPN).
        """

        # URL from which to get the data.
        # OPN points to a specific webpage rather than serving as a URL parameter.
        url = "{}/v2/store/products/{}".format(self.server, opn)
        url += "?currency={}".format(currency)
        url += "&exclude-evms={}".format(excludeEVMs)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def __init__(self, client_id, client_secret, server, verify=True):

        """
        Creates object through which to interact with TI Store inventory API.
        """

        # Store API server. It should be formatted as "https://example.server.com".
        self.server = server

        # Get API access object based on given information: url, client ID, and client secret.
        self.api = API_Accessor(server=server, client_id=client_id, client_secret=client_secret, verify=verify)

class TI_Subscriptions:

    """
    API to subscribe to parts on the TI store.
    """

    def get_subscriptions(self, headers={}, verify=True):

        """
        Get all active subscriptions.
        """

        # URL from which to retrieve active subscriptions.
        url = "{}/v2/store/subscriptions/inventory/".format(self.server)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def _get_subscription_by_part(self, opn, headers={}, verify=True):
        
        """
        Get a single active inventory subscription for the part number.
        """

        # URL where we will subscribe to the part number.
        # OPN is passed as a webpage rather than as a URL parameter.
        url = "{}/v2/store/subscriptions/inventory/{}".format(self.server, opn)

        # Make request from the API access object.
        return self.api.get(url=url, headers=headers, verify=verify)

    def subscribe(self, opn, quantity, currency, autoSubscribe, expiration, headers={}, verify=True):

        """
        Create or update a subscription. Data is passed through a JSON object.
        """

        # URL through which subscriptions are made.
        url = "{}/v2/store/subscriptions/inventory/".format(self.server)

        # Create JSON object to pass.
        json = {"tiPartNumber" : opn, "requestedQty" : quantity, "currency" : currency, "autoSubscribe" : autoSubscribe, "expiration" : expiration}

        # Make request from the API access object.
        return self.api.post(url=url, json=json, headers=headers, verify=verify)

    def unsubscribe_from_all(self, headers={}, verify=True):

        """
        Delete all TI Store subscriptions.
        """

        # URL for subscriptions.
        url = "{}/v2/store/subscriptions/inventory/".format(self.server)

        # Make request from the API access object.
        # We will expect a status code of 204, rather than the typical 200.
        return self.api.delete(url=url, headers=headers, verify=verify, status_code=204)

    def unsubscribe_from_part(self, opn, headers={}, verify=True):

        """
        Delete TI Store subscription for a specific part.
        """

        # URL for subscription.
        # OPN is passed as a webpage rather than as a URL parameter.
        url = "{}/v2/store/subscriptions/inventory/{}".format(self.server, opn)

        # Make request from the API access object.
        # We will expect a status code of 204, rather than the typical 200.
        return self.api.delete(url=url, headers=headers, verify=verify, status_code=204)

    def generate_test_notification(self, headers={}, verify=True):

        """
        Generates test notification.
        """

        # URL for test subscription.
        url = "{}/v2/store/subscriptions/inventory/test/".format(self.server)

        # Make request onto API access object.
        return self.api.post(url=url, json={}, headers=headers, verify=verify)


    def __init__(self, client_id, client_secret, server, verify=True):

        """
        Creates object through which to interact with TI Store subscriptions API.
        """

        # Store API server. It should be formatted as "https://example.server.com".
        self.server = server

        # Get API access object based on given information: url, client ID, and client secret.
        self.api = API_Accessor(server=server, client_id=client_id, client_secret=client_secret, verify=verify)
