# GetTaxRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_identification_no** | **str** | The buyer’s VAT ID. Using this value will force VAT rules to be considered for the transaction. This may be set on the document or the line. Note that this should be a valid VAT number, and this field should not be used for any other purpose. | [optional] 
**commit** | **bool** | Default is false. Setting this value to true will put the document in a Committed status, preventing further document status changes, except voiding with CancelTax. | [optional] 
**client** | **str** | An identifier of software client generating the API call. | [optional] 
**company_code** | **str** | The case-sensitive code that identifies the company in the AvaTax account in which the document should be posted. This code is declared during the company setup in the AvaTax Admin Console. If no value is passed, the document will be assigned to the default company. If a value is passed that does not match any company on on the account, an error is returned. | [optional] 
**customer_code** | **str** | The case-sensitive client application customer reference code. This is required since it is the key to the Exemption Certificate Management Service in the Admin Console. | 
**currency_code** | **str** | 3 character ISO 4217 compliant currency code. If unspecified, a default of USD will be used. | [optional] 
**customer_usage_type** | **str** | The client application customer or usage type. More information about this value is available in the [Avalara Help Center](https://help.avalara.com/kb/001/What_are_the_Entity_Use_Codes_used_for_Avalara_AvaTax%3F). | [optional] 
**detail_level** | **str** | Specifies the level of detail to return. Summary - summarizes document and jurisdiction detail with no line breakout Document - only document detail Line - document and line detail Tax - document, line and jurisdiction detail | [optional] 
**discount** | **float** | The discount amount to apply to the document. This may be used along with the line attribute &#x60;Discounted&#x60; in order to distribute a set discount amount proportionally across the applicable document lines. This should be an amount, not a percent. | [optional] 
**doc_code** | **str** | While this is an optional field, serious consideration should be given to using it. If no value is sent, AvaTax assigns a GUID value to keep the document unique. This can make reconciliation a challenge. | [optional] 
**doc_type** | **str** | The document type specifies the category of the document and affects how the document is treated after a tax calculation. If no DocType is specified in the request, SalesOrder will be used. SalesOrder: This is a temporary document type and is not saved in tax history. GetTaxResult will return with a DocStatus of Temporary. SalesInvoice: The document is a permanent invoice; document and tax calculation results are saved in the tax history. GetTaxResult will return with a DocStatus of Saved. PurchaseOrder: This is a temporary document type and is not saved in tax history. GetTaxResult will return with a DocStatus of Temporary. PurchaseInvoice : The document is a permanent invoice; document and tax calculation results are saved in the tax history. GetTaxResult will return with a DocStatus of Saved. ReturnOrder: This is a temporary document type and is not saved in tax history. GetTaxResult will return with a DocStatus of Temporary. ReturnInvoice: The document is a permanent sales return invoice; document and tax calculation results are saved in the tax history GetTaxResult will return with a DocStatus of Saved. | [optional] 
**doc_date** | **date** | The date on the invoice, purchase order, etc. Format YYYY-MM-DD. If omitted, this will default to the current date. | [optional] 
**exemption_no** | **str** | Any string value will cause the sale to be exempt. This should only be used if your finance team is manually verifying and tracking exemption certificates. | [optional] 
**location_code** | **str** | Also referred to as a Store Location, Outlet Id, or Outlet code. Location code is a value assigned by some state jurisdictions that identifies a particular store location. These states may require tax liabilities to be broken out separately for each store location. | [optional] 
**pos_lane_code** | **str** | Permits a point of sale application to record the unique code / ID / number associated with the terminal processing a sale. | [optional] 
**purchase_order_no** | **str** | Your customer’s purchase order number. | [optional] 
**reference_code** | **str** | Additional information used for reporting. For returns, this can refer to the DocCode of the original invoice. | [optional] 
**tax_override** | [**TaxOverride**](TaxOverride.md) |  | [optional] 
**addresses** | [**list[Address]**](Address.md) |  | 
**lines** | [**list[Line]**](Line.md) | Document line array. There is a limit of 15000 lines per document. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


