# CancelTaxRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_code** | **str** | The reason for cancelling the tax record. One of: Unspecified, PostFailed, DocDeleted, DocVoided, AdjustmentCancelled | 
**company_code** | **str** | Client application company reference code. Not required if the document is identified by DocId. | 
**doc_code** | **str** | Client application identifier describing this tax transaction (i.e. invoice number, sales order number, etc.). Not required if the document is identified by DocId. | 
**doc_type** | **str** | Value describing what type of tax document is being cancelled. One of: SalesInvoice, ReturnInvoice, PurchaseInvoice. Not required if the document is identified by DocId. | 
**doc_id** | **str** | Avatax-assigned unique Document Id, can be used in place of DocCode, DocType, and CompanyCode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


