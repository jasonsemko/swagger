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


class CancelTaxResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, transaction_id=None, doc_id=None, result_code=None, messages=None):
        """
        CancelTaxResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'transaction_id': 'str',
            'doc_id': 'str',
            'result_code': 'ResultCode',
            'messages': 'list[Message]'
        }

        self.attribute_map = {
            'transaction_id': 'TransactionId',
            'doc_id': 'DocId',
            'result_code': 'ResultCode',
            'messages': 'Messages'
        }

        self._transaction_id = transaction_id
        self._doc_id = doc_id
        self._result_code = result_code
        self._messages = messages

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this CancelTaxResult.
        The unique numeric identifier of the API operation assigned by the AvaTax service.

        :return: The transaction_id of this CancelTaxResult.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this CancelTaxResult.
        The unique numeric identifier of the API operation assigned by the AvaTax service.

        :param transaction_id: The transaction_id of this CancelTaxResult.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def doc_id(self):
        """
        Gets the doc_id of this CancelTaxResult.
        The unique numeric identifier (Document ID) assigned to the tax document in question by the AvaTax Service.

        :return: The doc_id of this CancelTaxResult.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """
        Sets the doc_id of this CancelTaxResult.
        The unique numeric identifier (Document ID) assigned to the tax document in question by the AvaTax Service.

        :param doc_id: The doc_id of this CancelTaxResult.
        :type: str
        """

        self._doc_id = doc_id

    @property
    def result_code(self):
        """
        Gets the result_code of this CancelTaxResult.

        :return: The result_code of this CancelTaxResult.
        :rtype: ResultCode
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """
        Sets the result_code of this CancelTaxResult.

        :param result_code: The result_code of this CancelTaxResult.
        :type: ResultCode
        """

        self._result_code = result_code

    @property
    def messages(self):
        """
        Gets the messages of this CancelTaxResult.

        :return: The messages of this CancelTaxResult.
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this CancelTaxResult.

        :param messages: The messages of this CancelTaxResult.
        :type: list[Message]
        """

        self._messages = messages

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
        if not isinstance(other, CancelTaxResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other