# TaxOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | This provides the reason for a tax override for audit purposes. Typical reasons include: &#39;Return&#39;, &#39;Layaway&#39;, &#39;Imported&#39;. | 
**tax_override_type** | **str** | Must be one of the following: None: Default TaxAmount: The TaxAmount overrides the total tax for the document. This is used for imported documents, returns, and layaways where the tax has already been calculated either by AvaTax or another means. Exemption: Exemption certificates are overridden making the document taxable. This may be used for situations where a normally exempt entity needs to be treated as not exempt. TaxDate: The TaxDate overrides the DocDate as the effective date used for tax calculation. This may effect rates, rules and other factors. | 
**tax_date** | **str** | Must be valid date, required if &#x60;TaxOverrideType&#x60; is &#x60;TaxDate&#x60;, the override tax date to use. This is used when the tax has been previously calculated as in the case of a layaway, return or other reason indicated by the &#x60;Reason&#x60; element. If the date is not overridden, then it should be set to the same as the &#x60;DocDate&#x60;. | [optional] 
**tax_amount** | **str** | Must be numeric, required if &#x60;TaxOverrideType&#x60; is &#x60;TaxAmount&#x60;. The overriding amount of tax to apply. If at the document level, this is distributed across all taxable rows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


