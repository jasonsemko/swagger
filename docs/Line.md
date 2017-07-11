# Line

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_no** | **str** | Line item identifier. LineId uniquely identifies the line item row. | 
**destination_code** | **str** | Destination (ship-to) address code. &#x60;DestinationCode&#x60; references an address from the &#x60;Addresses&#x60; collection. | 
**origin_code** | **str** | Origination (ship-from) address code. &#x60;OriginCode&#x60; references an address from the &#x60;Addresses&#x60; collection. | 
**item_code** | **str** | Your item identifier, SKU, or UPC. Strongly recommended. | [optional] 
**tax_code** | **str** | Product taxability code of the line item. Can be an AvaTax system tax code, or a custom-defined tax code. | [optional] 
**customer_usage_type** | **str** | The client application customer or usage type. &#x60;CustomerUsageType&#x60; determines the exempt status of the transaction based on the exemption tax rules for the jurisdictions involved. Can also be referred to as Entity/Use Code. More information about this value is available in the Avalara Help Center. | [optional] 
**business_identification_no** | **str** | The buyer’s VAT id. Using this value will force VAT rules to be considered for the transaction. This may be set on the document or the line. | [optional] 
**description** | **str** | Item description. Required for customers using our filing service. | [optional] 
**qty** | **float** | Item quantity. The tax engine does NOT use this as a multiplier with price to get the &#x60;Amount&#x60;. | [optional] 
**amount** | **float** | Total amount of item (extended amount, qty * unit price). If omitted, this value will default to &#x60;0&#x60; | [optional] 
**discounted** | **bool** | Should be set to true if the document level discount is applied to this line item. Defaults to &#x60;false&#x60;. | [optional] 
**tax_included** | **bool** | Should be set to &#x60;true&#x60; if the tax is already included, and sale amount and tax should be back-calculated from the provided &#x60;Line.Amount&#x60;. Defaults to &#x60;false&#x60;. | [optional] 
**ref1** | **str** | Value stored on a line item. Does not affect tax calclulation. | [optional] 
**ref2** | **str** | Value stored on a line item. Does not affect tax calclulation. | [optional] 
**tax_override** | [**TaxOverride**](TaxOverride.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


