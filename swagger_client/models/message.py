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


class Message(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, summary=None, details=None, refers_to=None, source=None, severity=None):
        """
        Message - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'summary': 'str',
            'details': 'str',
            'refers_to': 'str',
            'source': 'str',
            'severity': 'str'
        }

        self.attribute_map = {
            'summary': 'Summary',
            'details': 'Details',
            'refers_to': 'RefersTo',
            'source': 'Source',
            'severity': 'Severity'
        }

        self._summary = summary
        self._details = details
        self._refers_to = refers_to
        self._source = source
        self._severity = severity

    @property
    def summary(self):
        """
        Gets the summary of this Message.
        The message summary in short form.

        :return: The summary of this Message.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this Message.
        The message summary in short form.

        :param summary: The summary of this Message.
        :type: str
        """
        if summary is not None and len(summary) > 255:
            raise ValueError("Invalid value for `summary`, length must be less than or equal to `255`")

        self._summary = summary

    @property
    def details(self):
        """
        Gets the details of this Message.
        Description of the error or warning.

        :return: The details of this Message.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Message.
        Description of the error or warning.

        :param details: The details of this Message.
        :type: str
        """
        if details is not None and len(details) > 255:
            raise ValueError("Invalid value for `details`, length must be less than or equal to `255`")

        self._details = details

    @property
    def refers_to(self):
        """
        Gets the refers_to of this Message.
        The data used during the request that caused the message to be generated.

        :return: The refers_to of this Message.
        :rtype: str
        """
        return self._refers_to

    @refers_to.setter
    def refers_to(self, refers_to):
        """
        Sets the refers_to of this Message.
        The data used during the request that caused the message to be generated.

        :param refers_to: The refers_to of this Message.
        :type: str
        """
        if refers_to is not None and len(refers_to) > 255:
            raise ValueError("Invalid value for `refers_to`, length must be less than or equal to `255`")

        self._refers_to = refers_to

    @property
    def source(self):
        """
        Gets the source of this Message.
        The internal location that generated the message.

        :return: The source of this Message.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Message.
        The internal location that generated the message.

        :param source: The source of this Message.
        :type: str
        """
        if source is not None and len(source) > 255:
            raise ValueError("Invalid value for `source`, length must be less than or equal to `255`")

        self._source = source

    @property
    def severity(self):
        """
        Gets the severity of this Message.
        Classifies the severity of the message. One of: Success, Warning, Error, Exception.

        :return: The severity of this Message.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Message.
        Classifies the severity of the message. One of: Success, Warning, Error, Exception.

        :param severity: The severity of this Message.
        :type: str
        """

        self._severity = severity

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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
