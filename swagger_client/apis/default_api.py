# coding: utf-8

"""
    AvaTax REST API

    The AvaTax REST API exposes the most commonly used available for interacting with the AvaTax service, allowing calculation of tax, modification of documents, and validation of addresses. If you're unsure of which API to use, a full comparison of the differences between the functionality provided by our REST and SOAP interfaces is documented [here](http://developer.avalara.com/avatax/soap-or-rest/). The [SOAP API reference](http://developer.avalara.com/avatax/api-reference/tax/soap) is also available.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cancel_tax(self, cancel_tax_request, **kwargs):
        """
        Void a Document
        Voids or deletes and existing transaction record from the AvaTax system. To use the XML for this operation specify the request `Content-Type: text/xml`. No modification needs to be made to the URL.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_tax(cancel_tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CancelTaxRequest cancel_tax_request: (required)
        :return: CancelTaxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cancel_tax_with_http_info(cancel_tax_request, **kwargs)
        else:
            (data) = self.cancel_tax_with_http_info(cancel_tax_request, **kwargs)
            return data

    def cancel_tax_with_http_info(self, cancel_tax_request, **kwargs):
        """
        Void a Document
        Voids or deletes and existing transaction record from the AvaTax system. To use the XML for this operation specify the request `Content-Type: text/xml`. No modification needs to be made to the URL.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cancel_tax_with_http_info(cancel_tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CancelTaxRequest cancel_tax_request: (required)
        :return: CancelTaxResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_tax_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cancel_tax_request' is set
        if ('cancel_tax_request' not in params) or (params['cancel_tax_request'] is None):
            raise ValueError("Missing the required parameter `cancel_tax_request` when calling `cancel_tax`")


        collection_formats = {}

        resource_path = '/tax/cancel'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancel_tax_request' in params:
            body_params = params['cancel_tax_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/json', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/json', 'text/xml'])

        # Authentication setting
        auth_settings = ['basic_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CancelTaxResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def estimate_tax(self, latitude, longitude, saleamount, **kwargs):
        """
        Estimate Tax
        Retrieves tax rate details for the supplied geographic coordinates and sale amount. Since the REST API does not provide an explicit ping function, this method can also be used to test connectivity to the service. If you would like an XML response, use the URL `/1.0/tax/{latitude},{longitude}/get.xml` and specify the request header `Content-Type: text/xml`.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.estimate_tax(latitude, longitude, saleamount, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str latitude: The latitude of the geographic coordinates to get tax for based on the sale amount (required)
        :param str longitude: The longitude of the geographic coordinates to get tax for based on the sale amount (required)
        :param str saleamount: The amount of sale requiring tax calculation, in decimal format (required)
        :return: EstimateTaxResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.estimate_tax_with_http_info(latitude, longitude, saleamount, **kwargs)
        else:
            (data) = self.estimate_tax_with_http_info(latitude, longitude, saleamount, **kwargs)
            return data

    def estimate_tax_with_http_info(self, latitude, longitude, saleamount, **kwargs):
        """
        Estimate Tax
        Retrieves tax rate details for the supplied geographic coordinates and sale amount. Since the REST API does not provide an explicit ping function, this method can also be used to test connectivity to the service. If you would like an XML response, use the URL `/1.0/tax/{latitude},{longitude}/get.xml` and specify the request header `Content-Type: text/xml`.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.estimate_tax_with_http_info(latitude, longitude, saleamount, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str latitude: The latitude of the geographic coordinates to get tax for based on the sale amount (required)
        :param str longitude: The longitude of the geographic coordinates to get tax for based on the sale amount (required)
        :param str saleamount: The amount of sale requiring tax calculation, in decimal format (required)
        :return: EstimateTaxResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['latitude', 'longitude', 'saleamount']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method estimate_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'latitude' is set
        if ('latitude' not in params) or (params['latitude'] is None):
            raise ValueError("Missing the required parameter `latitude` when calling `estimate_tax`")
        # verify the required parameter 'longitude' is set
        if ('longitude' not in params) or (params['longitude'] is None):
            raise ValueError("Missing the required parameter `longitude` when calling `estimate_tax`")
        # verify the required parameter 'saleamount' is set
        if ('saleamount' not in params) or (params['saleamount'] is None):
            raise ValueError("Missing the required parameter `saleamount` when calling `estimate_tax`")


        collection_formats = {}

        resource_path = '/tax/{latitude},{longitude}/get'.replace('{format}', 'json')
        path_params = {}
        if 'latitude' in params:
            path_params['latitude'] = params['latitude']
        if 'longitude' in params:
            path_params['longitude'] = params['longitude']

        query_params = {}
        if 'saleamount' in params:
            query_params['saleamount'] = params['saleamount']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/json', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/json', 'text/xml'])

        # Authentication setting
        auth_settings = ['basic_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EstimateTaxResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tax(self, get_tax_request, **kwargs):
        """
        Calculate Tax and Record a Document
        Calculates taxes on a document such as a sales order, sales invoice, purchase order, purchase invoice, or credit memo. To use an XML request/response, use the URL `/1.0/tax/get.xml`
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tax(get_tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param GetTaxRequest get_tax_request: (required)
        :return: GetTaxResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tax_with_http_info(get_tax_request, **kwargs)
        else:
            (data) = self.get_tax_with_http_info(get_tax_request, **kwargs)
            return data

    def get_tax_with_http_info(self, get_tax_request, **kwargs):
        """
        Calculate Tax and Record a Document
        Calculates taxes on a document such as a sales order, sales invoice, purchase order, purchase invoice, or credit memo. To use an XML request/response, use the URL `/1.0/tax/get.xml`
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tax_with_http_info(get_tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param GetTaxRequest get_tax_request: (required)
        :return: GetTaxResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_tax_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_tax_request' is set
        if ('get_tax_request' not in params) or (params['get_tax_request'] is None):
            raise ValueError("Missing the required parameter `get_tax_request` when calling `get_tax`")


        collection_formats = {}

        resource_path = '/tax/get'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_tax_request' in params:
            body_params = params['get_tax_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/json', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/json', 'text/xml'])

        # Authentication setting
        auth_settings = ['basic_auth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='GetTaxResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def validate_address(self, line1, country, **kwargs):
        """
        Validate an Address
        Normalizes a single US or Canadian address, providing a non-ambiguous USPS address match. To recieve an XML response, use the URL `/1.0/address/validate.xml` and set the request header `Content-Type: text/xml`
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_address(line1, country, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str line1: Address line 1 (required)
        :param str country: (required)
        :param str line2: Address line 2
        :param str line3: Address line 3
        :param str city: City name: optional unless `PostalCode` is not specified.
        :param str region:
        :param str postal_code:
        :return: ValidateResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_address_with_http_info(line1, country, **kwargs)
        else:
            (data) = self.validate_address_with_http_info(line1, country, **kwargs)
            return data

    def validate_address_with_http_info(self, line1, country, **kwargs):
        """
        Validate an Address
        Normalizes a single US or Canadian address, providing a non-ambiguous USPS address match. To recieve an XML response, use the URL `/1.0/address/validate.xml` and set the request header `Content-Type: text/xml`
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_address_with_http_info(line1, country, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str line1: Address line 1 (required)
        :param str country: (required)
        :param str line2: Address line 2
        :param str line3: Address line 3
        :param str city: City name: optional unless `PostalCode` is not specified.
        :param str region:
        :param str postal_code:
        :return: ValidateResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['line1', 'country', 'line2', 'line3', 'city', 'region', 'postal_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'line1' is set
        if ('line1' not in params) or (params['line1'] is None):
            raise ValueError("Missing the required parameter `line1` when calling `validate_address`")
        # verify the required parameter 'country' is set
        if ('country' not in params) or (params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `validate_address`")

        if 'line1' in params and len(params['line1']) > 50:
            raise ValueError("Invalid value for parameter `line1` when calling `validate_address`, length must be less than or equal to `50`")
        if 'country' in params and len(params['country']) > 2:
            raise ValueError("Invalid value for parameter `country` when calling `validate_address`, length must be less than or equal to `2`")
        if 'line2' in params and len(params['line2']) > 50:
            raise ValueError("Invalid value for parameter `line2` when calling `validate_address`, length must be less than or equal to `50`")
        if 'line3' in params and len(params['line3']) > 50:
            raise ValueError("Invalid value for parameter `line3` when calling `validate_address`, length must be less than or equal to `50`")
        if 'city' in params and len(params['city']) > 50:
            raise ValueError("Invalid value for parameter `city` when calling `validate_address`, length must be less than or equal to `50`")
        if 'region' in params and len(params['region']) > 3:
            raise ValueError("Invalid value for parameter `region` when calling `validate_address`, length must be less than or equal to `3`")
        if 'postal_code' in params and len(params['postal_code']) > 11:
            raise ValueError("Invalid value for parameter `postal_code` when calling `validate_address`, length must be less than or equal to `11`")

        collection_formats = {}

        resource_path = '/address/validate'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'line1' in params:
            query_params['Line1'] = params['line1']
        if 'line2' in params:
            query_params['Line2'] = params['line2']
        if 'line3' in params:
            query_params['Line3'] = params['line3']
        if 'city' in params:
            query_params['City'] = params['city']
        if 'region' in params:
            query_params['Region'] = params['region']
        if 'country' in params:
            query_params['Country'] = params['country']
        if 'postal_code' in params:
            query_params['PostalCode'] = params['postal_code']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/json', 'text/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/json', 'text/xml'])

        # Authentication setting
        auth_settings = ['basic_auth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ValidateResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
