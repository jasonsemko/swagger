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


class TaxDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country=None, juris_name=None, juris_code=None, juris_type=None, rate=None, region=None, tax=None, tax_name=None):
        """
        TaxDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country': 'Country',
            'juris_name': 'str',
            'juris_code': 'str',
            'juris_type': 'str',
            'rate': 'float',
            'region': 'str',
            'tax': 'float',
            'tax_name': 'str'
        }

        self.attribute_map = {
            'country': 'Country',
            'juris_name': 'JurisName',
            'juris_code': 'JurisCode',
            'juris_type': 'JurisType',
            'rate': 'Rate',
            'region': 'Region',
            'tax': 'Tax',
            'tax_name': 'TaxName'
        }

        self._country = country
        self._juris_name = juris_name
        self._juris_code = juris_code
        self._juris_type = juris_type
        self._rate = rate
        self._region = region
        self._tax = tax
        self._tax_name = tax_name

    @property
    def country(self):
        """
        Gets the country of this TaxDetail.

        :return: The country of this TaxDetail.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this TaxDetail.

        :param country: The country of this TaxDetail.
        :type: Country
        """

        self._country = country

    @property
    def juris_name(self):
        """
        Gets the juris_name of this TaxDetail.
        Name of a tax jurisdiction.

        :return: The juris_name of this TaxDetail.
        :rtype: str
        """
        return self._juris_name

    @juris_name.setter
    def juris_name(self, juris_name):
        """
        Sets the juris_name of this TaxDetail.
        Name of a tax jurisdiction.

        :param juris_name: The juris_name of this TaxDetail.
        :type: str
        """
        if juris_name is not None and len(juris_name) > 200:
            raise ValueError("Invalid value for `juris_name`, length must be less than or equal to `200`")

        self._juris_name = juris_name

    @property
    def juris_code(self):
        """
        Gets the juris_code of this TaxDetail.
        State assigned code identifying the jurisdiction. Note that this is not necessarily a unique identifier of the jurisdiction.

        :return: The juris_code of this TaxDetail.
        :rtype: str
        """
        return self._juris_code

    @juris_code.setter
    def juris_code(self, juris_code):
        """
        Sets the juris_code of this TaxDetail.
        State assigned code identifying the jurisdiction. Note that this is not necessarily a unique identifier of the jurisdiction.

        :param juris_code: The juris_code of this TaxDetail.
        :type: str
        """
        if juris_code is not None and len(juris_code) > 200:
            raise ValueError("Invalid value for `juris_code`, length must be less than or equal to `200`")

        self._juris_code = juris_code

    @property
    def juris_type(self):
        """
        Gets the juris_type of this TaxDetail.

        :return: The juris_type of this TaxDetail.
        :rtype: str
        """
        return self._juris_type

    @juris_type.setter
    def juris_type(self, juris_type):
        """
        Sets the juris_type of this TaxDetail.

        :param juris_type: The juris_type of this TaxDetail.
        :type: str
        """
        allowed_values = ["State", "County", "City", "Country", "Special Tax Jurisdiction"]
        if juris_type not in allowed_values:
            raise ValueError(
                "Invalid value for `juris_type` ({0}), must be one of {1}"
                .format(juris_type, allowed_values)
            )

        self._juris_type = juris_type

    @property
    def rate(self):
        """
        Gets the rate of this TaxDetail.
        Effective tax rate for tax jurisdiction.

        :return: The rate of this TaxDetail.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this TaxDetail.
        Effective tax rate for tax jurisdiction.

        :param rate: The rate of this TaxDetail.
        :type: float
        """

        self._rate = rate

    @property
    def region(self):
        """
        Gets the region of this TaxDetail.
        Region of tax jurisdiction.

        :return: The region of this TaxDetail.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this TaxDetail.
        Region of tax jurisdiction.

        :param region: The region of this TaxDetail.
        :type: str
        """
        if region is not None and len(region) > 3:
            raise ValueError("Invalid value for `region`, length must be less than or equal to `3`")

        self._region = region

    @property
    def tax(self):
        """
        Gets the tax of this TaxDetail.
        Tax amount

        :return: The tax of this TaxDetail.
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """
        Sets the tax of this TaxDetail.
        Tax amount

        :param tax: The tax of this TaxDetail.
        :type: float
        """

        self._tax = tax

    @property
    def tax_name(self):
        """
        Gets the tax_name of this TaxDetail.
        Tax name

        :return: The tax_name of this TaxDetail.
        :rtype: str
        """
        return self._tax_name

    @tax_name.setter
    def tax_name(self, tax_name):
        """
        Sets the tax_name of this TaxDetail.
        Tax name

        :param tax_name: The tax_name of this TaxDetail.
        :type: str
        """
        if tax_name is not None and len(tax_name) > 75:
            raise ValueError("Invalid value for `tax_name`, length must be less than or equal to `75`")

        self._tax_name = tax_name

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
        if not isinstance(other, TaxDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
