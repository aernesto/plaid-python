# coding: utf-8

"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.0.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from plaid.generated_plaid.configuration import Configuration


class PaymentInitiationRecipientGetResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'recipient_id': 'str',
        'name': 'str',
        'address': 'PaymentInitiationAddress',
        'iban': 'str',
        'bacs': 'PaymentInitiationRecipientGetResponseBacs',
        'request_id': 'str'
    }

    attribute_map = {
        'recipient_id': 'recipient_id',
        'name': 'name',
        'address': 'address',
        'iban': 'iban',
        'bacs': 'bacs',
        'request_id': 'request_id'
    }

    def __init__(self, recipient_id=None, name=None, address=None, iban=None, bacs=None, request_id=None, local_vars_configuration=None):  # noqa: E501
        """PaymentInitiationRecipientGetResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recipient_id = None
        self._name = None
        self._address = None
        self._iban = None
        self._bacs = None
        self._request_id = None
        self.discriminator = None

        if recipient_id is not None:
            self.recipient_id = recipient_id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if iban is not None:
            self.iban = iban
        if bacs is not None:
            self.bacs = bacs
        if request_id is not None:
            self.request_id = request_id

    @property
    def recipient_id(self):
        """Gets the recipient_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501

        The ID of the recipient.  # noqa: E501

        :return: The recipient_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """Sets the recipient_id of this PaymentInitiationRecipientGetResponse.

        The ID of the recipient.  # noqa: E501

        :param recipient_id: The recipient_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type recipient_id: str
        """

        self._recipient_id = recipient_id

    @property
    def name(self):
        """Gets the name of this PaymentInitiationRecipientGetResponse.  # noqa: E501

        The name of the recipient.  # noqa: E501

        :return: The name of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentInitiationRecipientGetResponse.

        The name of the recipient.  # noqa: E501

        :param name: The name of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this PaymentInitiationRecipientGetResponse.  # noqa: E501


        :return: The address of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: PaymentInitiationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PaymentInitiationRecipientGetResponse.


        :param address: The address of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type address: PaymentInitiationAddress
        """

        self._address = address

    @property
    def iban(self):
        """Gets the iban of this PaymentInitiationRecipientGetResponse.  # noqa: E501

        The International Bank Account Number (IBAN) for the recipient.  # noqa: E501

        :return: The iban of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PaymentInitiationRecipientGetResponse.

        The International Bank Account Number (IBAN) for the recipient.  # noqa: E501

        :param iban: The iban of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type iban: str
        """

        self._iban = iban

    @property
    def bacs(self):
        """Gets the bacs of this PaymentInitiationRecipientGetResponse.  # noqa: E501


        :return: The bacs of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: PaymentInitiationRecipientGetResponseBacs
        """
        return self._bacs

    @bacs.setter
    def bacs(self, bacs):
        """Sets the bacs of this PaymentInitiationRecipientGetResponse.


        :param bacs: The bacs of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type bacs: PaymentInitiationRecipientGetResponseBacs
        """

        self._bacs = bacs

    @property
    def request_id(self):
        """Gets the request_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :return: The request_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PaymentInitiationRecipientGetResponse.

        A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.  # noqa: E501

        :param request_id: The request_id of this PaymentInitiationRecipientGetResponse.  # noqa: E501
        :type request_id: str
        """

        self._request_id = request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentInitiationRecipientGetResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentInitiationRecipientGetResponse):
            return True

        return self.to_dict() != other.to_dict()