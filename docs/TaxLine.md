# TaxLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_no** | **str** | Line item identifier. | [optional] 
**tax_code** | **str** | The tax code used in calculating tax. | [optional] 
**taxability** | **bool** | Flag indicating item was taxable. | [optional] 
**taxable** | **float** | The amount that is taxable. | [optional] 
**rate** | **float** | Effective tax rate. | [optional] 
**tax** | **float** | Tax amount. | [optional] 
**discount** | **float** | Discount amount. | [optional] 
**tax_calculated** | **float** | Amount of tax calculated. | [optional] 
**exemption** | **float** | Exempt amount. | [optional] 
**boundary_level** | **str** | The boundary level used to calculate tax: determined by the quality of provided addresses. | [optional] 
**tax_details** | [**list[TaxDetail]**](TaxDetail.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


