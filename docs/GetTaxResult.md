# GetTaxResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_code** | [**DocCode**](DocCode.md) |  | [optional] 
**doc_date** | **str** | Date of invoice, sales order, purchase order, etc. | [optional] 
**time_stamp** | **datetime** | Server timestamp of request. | [optional] 
**total_amount** | **float** | Sum of all line &#x60;Amount&#x60; values. | [optional] 
**total_discount** | **float** | Sum of all &#x60;TaxLine&#x60; discount amounts. | [optional] 
**total_exemption** | **float** | Total exemption amount. | [optional] 
**total_taxable** | **float** | Total taxable amount. | [optional] 
**total_tax** | **float** | Sum of all &#x60;TaxLine&#x60; tax amounts. | [optional] 
**total_tax_calculated** | **float** | Indicates the total tax calculated by AvaTax. This is usually the same as the &#x60;TotalTax&#x60;, except when a tax override amount is specified. This is for informational purposes. The &#x60;TotalTax&#x60; will still be used for reporting. | [optional] 
**tax_date** | **date** | Date used to assess tax rates and jurisdictions. | [optional] 
**tax_lines** | [**list[TaxLine]**](TaxLine.md) |  | [optional] 
**tax_summary** | [**list[TaxDetail]**](TaxDetail.md) |  | [optional] 
**tax_addresses** | [**list[TaxAddress]**](TaxAddress.md) |  | [optional] 
**result_code** | [**ResultCode**](ResultCode.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


