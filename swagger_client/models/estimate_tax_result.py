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


class EstimateTaxResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rate=None, tax=None, tax_details=None, result_code=None):
        """
        EstimateTaxResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rate': 'float',
            'tax': 'float',
            'tax_details': 'list[TaxDetail]',
            'result_code': 'ResultCode'
        }

        self.attribute_map = {
            'rate': 'Rate',
            'tax': 'Tax',
            'tax_details': 'TaxDetails',
            'result_code': 'ResultCode'
        }

        self._rate = rate
        self._tax = tax
        self._tax_details = tax_details
        self._result_code = result_code

    @property
    def rate(self):
        """
        Gets the rate of this EstimateTaxResult.
        Total effective tax rate.

        :return: The rate of this EstimateTaxResult.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this EstimateTaxResult.
        Total effective tax rate.

        :param rate: The rate of this EstimateTaxResult.
        :type: float
        """

        self._rate = rate

    @property
    def tax(self):
        """
        Gets the tax of this EstimateTaxResult.
        Total calculated tax amount.

        :return: The tax of this EstimateTaxResult.
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this EstimateTaxResult.
        Total calculated tax amount.

        :param tax: The tax of this EstimateTaxResult.
        :type: float
        """

        self._tax = tax

    @property
    def tax_details(self):
        """
        Gets the tax_details of this EstimateTaxResult.

        :return: The tax_details of this EstimateTaxResult.
        :rtype: list[TaxDetail]
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """
        Sets the tax_details of this EstimateTaxResult.

        :param tax_details: The tax_details of this EstimateTaxResult.
        :type: list[TaxDetail]
        """

        self._tax_details = tax_details

    @property
    def result_code(self):
        """
        Gets the result_code of this EstimateTaxResult.

        :return: The result_code of this EstimateTaxResult.
        :rtype: ResultCode
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """
        Sets the result_code of this EstimateTaxResult.

        :param result_code: The result_code of this EstimateTaxResult.
        :type: ResultCode
        """

        self._result_code = result_code

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
        if not isinstance(other, EstimateTaxResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other