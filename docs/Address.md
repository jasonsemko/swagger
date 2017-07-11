# Address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_code** | **str** | Reference code uniquely identifying this address instance. | 
**line1** | **str** | Address line 1, recommended if latitude and longitude are not provided. | 
**line2** | **str** | Address line 2 | [optional] 
**line3** | **str** | Address line 3 | [optional] 
**city** | **str** | City name, required unless &#x60;PostalCode&#x60; is specified and/or latitude and longitude are provided. | 
**region** | **str** | State, province, or region name. Required unless Ccity is specified and/or latitude and longitude are provided. | 
**country** | **str** | Two-character ISO country code. If not provided, will default to &#39;US&#39;. | [optional] 
**postal_code** | **str** | Postal or ZIP code, Required unless city and region are specified, and/or latitude and longitude are provided. | 
**latitude** | **float** | Geographic latitude. If &#x60;Latitude&#x60; is defined, it is expected that the longitude field will also be provided. Failure to do so will result in operation error. Calculation by latitude/longitude is available for the United States only. If a latitude/longitude value outside of the US is provided, the service will return an error. | [optional] 
**longitude** | **float** | Geographic longitude. If &#x60;Longitude&#x60; is defined, it is expected that the latitude field will also be provided. Fail to do so will result in operation error. Calculation by latitude/longitude is available for the United States only. If a latitude/longitude value outside of the US is provided, the service will return an error. | [optional] 
**tax_region_id** | **float** | AvaTax tax region identifier. If a non-zero value is entered into &#x60;TaxRegionId&#x60;, other fields will be ignored. Not recommended. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


