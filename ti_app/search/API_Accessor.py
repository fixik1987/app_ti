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

import requests
from datetime import datetime


class API_Accessor:

    def is_token_valid(self):

        """
        Returns true if the token has not yet expired.
        """

        # Compare current datetime to expiration datetime.
        return datetime.now() < self.expiration

    def get(self, url, headers = {}, verify=True, status_code=200):

        """
        Makes an API get request at the given URL.
        The API access token is appended onto any given `headers` dictionary.
        If `verify` is true, the server's TSL connection is verified before sending the API request
        """

        # Append access token if valid so we can access the URL.
        if(self.is_token_valid()):
            headers['Authorization'] = "Bearer {}".format(self.token)
    
        # If token has expired, tell the user and end the program.
        else:
            print("ERROR: API access token has expired at {}.", self.expiration.strftime("%m/%d/%Y %H:%M:%S"))
            exit(1)

        # Make get request.
        response = requests.get(url=url, headers=headers, verify=verify)

        # If we did not get expected HTTP status code, warn the user.
        if(response.status_code != status_code):
            print("WARNING: Unexpected HTTP status code {}.".format(response.status_code))

        # Return response.
        return response

    def post(self, url, json, headers = {}, verify=True, status_code=200):

        """
        Makes an API post request at the given URL.
        The API access token is appended onto any given `headers` dictionary.
        If `verify` is true, the server's TSL connection is verified before sending the API request.
        """

        # Append access token if valid so we can access the URL.
        if(self.is_token_valid()):
            headers['Authorization'] = "Bearer {}".format(self.token)
    
        # If token has expired, tell the user and end the program.
        else:
            print("ERROR: API access token has expired at {}.", self.expiration.strftime("%m%d%Y %H:%M:%S"))
            exit(1)

        # Make post request.
        response = requests.post(url=url, headers=headers, verify=verify, json=json)

        # If we did not get expected HTTP status code, warn the user.
        if(response.status_code != status_code):
            print("WARNING: Unexpected HTTP status code {}.".format(response.status_code))

        # Return response.
        return response

    def delete(self, url, headers = {}, verify=True, status_code=200):

        """
        Makes an API delete request at the given URL.
        The API access token is appended onto any given `headers` dictionary.
        If `verify` is true, the server's TSL connection is verified before sending the API request.
        """

        # Append access token if valid so we can access the URL.
        if(self.is_token_valid()):
            headers['Authorization'] = "Bearer {}".format(self.token)
    
        # If token has expired, tell the user and end the program.
        else:
            print("ERROR: API access token has expired at {}.", self.expiration.strftime("%m%d%Y %H:%M:%S"))
            exit(1)

        # Make delete request.
        response = requests.delete(url=url, headers=headers, verify=verify)

        # If we did not get the expected HTTP status code, warn the user.
        if(response.status_code != status_code):
            print("WARNING: Unexpected HTTP status code {}.".format(response.status_code))

        # Return response.
        return response

    def __attempt_access_request(self, server, client_id, client_secret, verify):

        """
        Attempts to make an API post request at the given API to request an API access token.
        This will set the object's token, createdAt, and duration attributes.
        """

        # Create an object which contains info with which to access API.
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }

        # Append specific address onto URL.
        url = "{}/v1/oauth".format(server)

        # API post request.
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=url, data=data, headers=headers, verify=verify)

        # Check if request was successful, on status code 200.
        if response.status_code == 200:

            # If yes, get token data and return access information.
            return response.json()

        # Else, the request has failed.
        return None

    def __init__(self, server, client_id, client_secret, verify=True):

        """
        Creates API access object.
        """

        # Attempt to request an API access token.
        # We are storing the information for posterity.
        self.info = self.__attempt_access_request(server=server, client_id=client_id, client_secret=client_secret, verify=verify)

        # If the request succeeds, retrieve all relevant attributes (access token and expiration time):
        if(self.info is not None):
            
            # Get access token.
            self.token = self.info['access_token']

            # Get timestamp for expiration time (issue time plus duration).
            expiration_timestamp = float(self.info['expires_in']) + float(self.info['issued_at']) / 1000

            # Set expiration time (divide by 1000 to convert from milliseconds to seconds).
            self.expiration = datetime.fromtimestamp(expiration_timestamp)

        # Otherwise, tell the user that the access request has failed and exit the program.
        else:
            print("ERROR: Failed to acquire API access token.")
            exit(1)