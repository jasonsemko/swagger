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


class TaxOverride(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, reason=None, tax_override_type=None, tax_date=None, tax_amount=None):
        """
        TaxOverride - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'reason': 'str',
            'tax_override_type': 'str',
            'tax_date': 'str',
            'tax_amount': 'str'
        }

        self.attribute_map = {
            'reason': 'Reason',
            'tax_override_type': 'TaxOverrideType',
            'tax_date': 'TaxDate',
            'tax_amount': 'TaxAmount'
        }

        self._reason = reason
        self._tax_override_type = tax_override_type
        self._tax_date = tax_date
        self._tax_amount = tax_amount

    @property
    def reason(self):
        """
        Gets the reason of this TaxOverride.
        This provides the reason for a tax override for audit purposes. Typical reasons include: 'Return', 'Layaway', 'Imported'.

        :return: The reason of this TaxOverride.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this TaxOverride.
        This provides the reason for a tax override for audit purposes. Typical reasons include: 'Return', 'Layaway', 'Imported'.

        :param reason: The reason of this TaxOverride.
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")
        if reason is not None and len(reason) > 255:
            raise ValueError("Invalid value for `reason`, length must be less than or equal to `255`")

        self._reason = reason

    @property
    def tax_override_type(self):
        """
        Gets the tax_override_type of this TaxOverride.
        Must be one of the following: None: Default TaxAmount: The TaxAmount overrides the total tax for the document. This is used for imported documents, returns, and layaways where the tax has already been calculated either by AvaTax or another means. Exemption: Exemption certificates are overridden making the document taxable. This may be used for situations where a normally exempt entity needs to be treated as not exempt. TaxDate: The TaxDate overrides the DocDate as the effective date used for tax calculation. This may effect rates, rules and other factors.

        :return: The tax_override_type of this TaxOverride.
        :rtype: str
        """
        return self._tax_override_type

    @tax_override_type.setter
    def tax_override_type(self, tax_override_type):
        """
        Sets the tax_override_type of this TaxOverride.
        Must be one of the following: None: Default TaxAmount: The TaxAmount overrides the total tax for the document. This is used for imported documents, returns, and layaways where the tax has already been calculated either by AvaTax or another means. Exemption: Exemption certificates are overridden making the document taxable. This may be used for situations where a normally exempt entity needs to be treated as not exempt. TaxDate: The TaxDate overrides the DocDate as the effective date used for tax calculation. This may effect rates, rules and other factors.

        :param tax_override_type: The tax_override_type of this TaxOverride.
        :type: str
        """
        if tax_override_type is None:
            raise ValueError("Invalid value for `tax_override_type`, must not be `None`")

        self._tax_override_type = tax_override_type

    @property
    def tax_date(self):
        """
        Gets the tax_date of this TaxOverride.
        Must be valid date, required if `TaxOverrideType` is `TaxDate`, the override tax date to use. This is used when the tax has been previously calculated as in the case of a layaway, return or other reason indicated by the `Reason` element. If the date is not overridden, then it should be set to the same as the `DocDate`.

        :return: The tax_date of this TaxOverride.
        :rtype: str
        """
        return self._tax_date

    @tax_date.setter
    def tax_date(self, tax_date):
        """
        Sets the tax_date of this TaxOverride.
        Must be valid date, required if `TaxOverrideType` is `TaxDate`, the override tax date to use. This is used when the tax has been previously calculated as in the case of a layaway, return or other reason indicated by the `Reason` element. If the date is not overridden, then it should be set to the same as the `DocDate`.

        :param tax_date: The tax_date of this TaxOverride.
        :type: str
        """

        self._tax_date = tax_date

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this TaxOverride.
        Must be numeric, required if `TaxOverrideType` is `TaxAmount`. The overriding amount of tax to apply. If at the document level, this is distributed across all taxable rows.

        :return: The tax_amount of this TaxOverride.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this TaxOverride.
        Must be numeric, required if `TaxOverrideType` is `TaxAmount`. The overriding amount of tax to apply. If at the document level, this is distributed across all taxable rows.

        :param tax_amount: The tax_amount of this TaxOverride.
        :type: str
        """

        self._tax_amount = tax_amount

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
        if not isinstance(other, TaxOverride):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
