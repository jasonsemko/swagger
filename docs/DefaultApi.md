# swagger_client.DefaultApi

All URIs are relative to *https://development.avalara.net/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_tax**](DefaultApi.md#cancel_tax) | **POST** /tax/cancel | Void a Document
[**estimate_tax**](DefaultApi.md#estimate_tax) | **GET** /tax/{latitude},{longitude}/get | Estimate Tax
[**get_tax**](DefaultApi.md#get_tax) | **POST** /tax/get | Calculate Tax and Record a Document
[**validate_address**](DefaultApi.md#validate_address) | **GET** /address/validate | Validate an Address


# **cancel_tax**
> CancelTaxResponse cancel_tax(cancel_tax_request)

Void a Document

Voids or deletes and existing transaction record from the AvaTax system. To use the XML for this operation specify the request `Content-Type: text/xml`. No modification needs to be made to the URL.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
cancel_tax_request = swagger_client.CancelTaxRequest() # CancelTaxRequest | 

try: 
    # Void a Document
    api_response = api_instance.cancel_tax(cancel_tax_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_tax_request** | [**CancelTaxRequest**](CancelTaxRequest.md)|  | 

### Return type

[**CancelTaxResponse**](CancelTaxResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/json, text/xml
 - **Accept**: text/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_tax**
> EstimateTaxResult estimate_tax(latitude, longitude, saleamount)

Estimate Tax

Retrieves tax rate details for the supplied geographic coordinates and sale amount. Since the REST API does not provide an explicit ping function, this method can also be used to test connectivity to the service. If you would like an XML response, use the URL `/1.0/tax/{latitude},{longitude}/get.xml` and specify the request header `Content-Type: text/xml`.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
latitude = '47.6205' # str | The latitude of the geographic coordinates to get tax for based on the sale amount
longitude = '-122.3493' # str | The longitude of the geographic coordinates to get tax for based on the sale amount
saleamount = '1249.99' # str | The amount of sale requiring tax calculation, in decimal format

try: 
    # Estimate Tax
    api_response = api_instance.estimate_tax(latitude, longitude, saleamount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->estimate_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **str**| The latitude of the geographic coordinates to get tax for based on the sale amount | 
 **longitude** | **str**| The longitude of the geographic coordinates to get tax for based on the sale amount | 
 **saleamount** | **str**| The amount of sale requiring tax calculation, in decimal format | 

### Return type

[**EstimateTaxResult**](EstimateTaxResult.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/json, text/xml
 - **Accept**: text/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax**
> GetTaxResult get_tax(get_tax_request)

Calculate Tax and Record a Document

Calculates taxes on a document such as a sales order, sales invoice, purchase order, purchase invoice, or credit memo. To use an XML request/response, use the URL `/1.0/tax/get.xml`

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
get_tax_request = swagger_client.GetTaxRequest() # GetTaxRequest | 

try: 
    # Calculate Tax and Record a Document
    api_response = api_instance.get_tax(get_tax_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_tax_request** | [**GetTaxRequest**](GetTaxRequest.md)|  | 

### Return type

[**GetTaxResult**](GetTaxResult.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/json, text/xml
 - **Accept**: text/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> ValidateResult validate_address(line1, country, line2=line2, line3=line3, city=city, region=region, postal_code=postal_code)

Validate an Address

Normalizes a single US or Canadian address, providing a non-ambiguous USPS address match. To recieve an XML response, use the URL `/1.0/address/validate.xml` and set the request header `Content-Type: text/xml`

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
line1 = '400 Broad St' # str | Address line 1
country = 'country_example' # str | 
line2 = 'line2_example' # str | Address line 2 (optional)
line3 = 'line3_example' # str | Address line 3 (optional)
city = 'Seattle' # str | City name: optional unless `PostalCode` is not specified. (optional)
region = 'WA' # str |  (optional)
postal_code = '98109' # str |  (optional)

try: 
    # Validate an Address
    api_response = api_instance.validate_address(line1, country, line2=line2, line3=line3, city=city, region=region, postal_code=postal_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **line1** | **str**| Address line 1 | 
 **country** | **str**|  | 
 **line2** | **str**| Address line 2 | [optional] 
 **line3** | **str**| Address line 3 | [optional] 
 **city** | **str**| City name: optional unless &#x60;PostalCode&#x60; is not specified. | [optional] 
 **region** | **str**|  | [optional] 
 **postal_code** | **str**|  | [optional] 

### Return type

[**ValidateResult**](ValidateResult.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: text/json, text/xml
 - **Accept**: text/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

