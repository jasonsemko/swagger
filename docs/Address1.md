# Address1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Address line 1 | [optional] 
**line2** | **str** | Address line 2 | [optional] 
**line3** | **str** | Address line 3 | [optional] 
**city** | **str** | City name | [optional] 
**region** | **str** | State, province, or region name. | [optional] 
**country** | **str** | Country code. | [optional] 
**postal_code** | **str** | Postal or ZIP code | [optional] 
**address_type** | **str** | Address type code. One of: * F - Firm or company address * G - General Delivery address * H - High-rise or business complex * P - PO Box address * R - Rural route address * S - Street or residential address | [optional] 
**fips_code** | **str** | FIPSCode is a unique 10-digit code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. Returned for US addresses only. Digits represent jurisdiction codes: * 1-2 State code * 3-5 County code * 6-10 City code | [optional] 
**carrier_route** | **str** | CarrierRoute is a four-character string representing a US postal carrier route. The first character of this property, the term, is always alphabetic, and the last three numeric. For example, “R001” or “C027” would be typical carrier routes. The alphabetic letter indicates the type of delivery associated with this address. Returned for US addresses only. * B - PO Box * C - City delivery * G - General delivery * H - Highway contract * R - Rural route | [optional] 
**post_net** | **str** | POSTNet is a 12-digit barcode containing the ZIP Code, ZIP+4 Code, and the delivery point code, used by the USPS to direct mail. Returned for US addresses only digits represent delivery information: * 1-5 ZIP code * 6-9 Plus4 code * 10-11 Delivery point * 12 Check digit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


