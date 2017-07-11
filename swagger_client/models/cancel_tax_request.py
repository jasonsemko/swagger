# coding: utf-8

"""
    AvaTax REST API

    The AvaTax REST API exposes the most commonly used available for interacting with the AvaTax service, allowing calculation of tax, modification of documents, and validation of addresses. If you're unsure of which API to use, a full comparison of the differences between the functionality provided by our REST and SOAP interfaces is documented [here](http://developer.avalara.com/avatax/soap-or-rest/). The [SOAP API reference](http://developer.avalara.com/avatax/api-reference/tax/soap) is also available.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CancelTaxRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cancel_code=None, company_code=None, doc_code=None, doc_type=None, doc_id=None):
        """
        CancelTaxRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cancel_code': 'str',
            'company_code': 'str',
            'doc_code': 'str',
            'doc_type': 'str',
            'doc_id': 'str'
        }

        self.attribute_map = {
            'cancel_code': 'CancelCode',
            'company_code': 'CompanyCode',
            'doc_code': 'DocCode',
            'doc_type': 'DocType',
            'doc_id': 'DocId'
        }

        self._cancel_code = cancel_code
        self._company_code = company_code
        self._doc_code = doc_code
        self._doc_type = doc_type
        self._doc_id = doc_id

    @property
    def cancel_code(self):
        """
        Gets the cancel_code of this CancelTaxRequest.
        The reason for cancelling the tax record. One of: Unspecified, PostFailed, DocDeleted, DocVoided, AdjustmentCancelled

        :return: The cancel_code of this CancelTaxRequest.
        :rtype: str
        """
        return self._cancel_code

    @cancel_code.setter
    def cancel_code(self, cancel_code):
        """
        Sets the cancel_code of this CancelTaxRequest.
        The reason for cancelling the tax record. One of: Unspecified, PostFailed, DocDeleted, DocVoided, AdjustmentCancelled

        :param cancel_code: The cancel_code of this CancelTaxRequest.
        :type: str
        """
        if cancel_code is None:
            raise ValueError("Invalid value for `cancel_code`, must not be `None`")

        self._cancel_code = cancel_code

    @property
    def company_code(self):
        """
        Gets the company_code of this CancelTaxRequest.
        Client application company reference code. Not required if the document is identified by DocId.

        :return: The company_code of this CancelTaxRequest.
        :rtype: str
        """
        return self._company_code

    @company_code.setter
    def company_code(self, company_code):
        """
        Sets the company_code of this CancelTaxRequest.
        Client application company reference code. Not required if the document is identified by DocId.

        :param company_code: The company_code of this CancelTaxRequest.
        :type: str
        """
        if company_code is None:
            raise ValueError("Invalid value for `company_code`, must not be `None`")
        if company_code is not None and len(company_code) > 25:
            raise ValueError("Invalid value for `company_code`, length must be less than or equal to `25`")

        self._company_code = company_code

    @property
    def doc_code(self):
        """
        Gets the doc_code of this CancelTaxRequest.
        Client application identifier describing this tax transaction (i.e. invoice number, sales order number, etc.). Not required if the document is identified by DocId.

        :return: The doc_code of this CancelTaxRequest.
        :rtype: str
        """
        return self._doc_code

    @doc_code.setter
    def doc_code(self, doc_code):
        """
        Sets the doc_code of this CancelTaxRequest.
        Client application identifier describing this tax transaction (i.e. invoice number, sales order number, etc.). Not required if the document is identified by DocId.

        :param doc_code: The doc_code of this CancelTaxRequest.
        :type: str
        """
        if doc_code is None:
            raise ValueError("Invalid value for `doc_code`, must not be `None`")
        if doc_code is not None and len(doc_code) > 50:
            raise ValueError("Invalid value for `doc_code`, length must be less than or equal to `50`")

        self._doc_code = doc_code

    @property
    def doc_type(self):
        """
        Gets the doc_type of this CancelTaxRequest.
        Value describing what type of tax document is being cancelled. One of: SalesInvoice, ReturnInvoice, PurchaseInvoice. Not required if the document is identified by DocId.

        :return: The doc_type of this CancelTaxRequest.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """
        Sets the doc_type of this CancelTaxRequest.
        Value describing what type of tax document is being cancelled. One of: SalesInvoice, ReturnInvoice, PurchaseInvoice. Not required if the document is identified by DocId.

        :param doc_type: The doc_type of this CancelTaxRequest.
        :type: str
        """
        if doc_type is None:
            raise ValueError("Invalid value for `doc_type`, must not be `None`")

        self._doc_type = doc_type

    @property
    def doc_id(self):
        """
        Gets the doc_id of this CancelTaxRequest.
        Avatax-assigned unique Document Id, can be used in place of DocCode, DocType, and CompanyCode.

        :return: The doc_id of this CancelTaxRequest.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """
        Sets the doc_id of this CancelTaxRequest.
        Avatax-assigned unique Document Id, can be used in place of DocCode, DocType, and CompanyCode.

        :param doc_id: The doc_id of this CancelTaxRequest.
        :type: str
        """

        self._doc_id = doc_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CancelTaxRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
