# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemuserputAddresses(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'po_box': 'str',
        'extended_address': 'str',
        'street_address': 'str',
        'locality': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'type': 'type',
        'po_box': 'poBox',
        'extended_address': 'extendedAddress',
        'street_address': 'streetAddress',
        'locality': 'locality',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, type=None, po_box=None, extended_address=None, street_address=None, locality=None, region=None, postal_code=None, country=None):  # noqa: E501
        """SystemuserputAddresses - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._po_box = None
        self._extended_address = None
        self._street_address = None
        self._locality = None
        self._region = None
        self._postal_code = None
        self._country = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if po_box is not None:
            self.po_box = po_box
        if extended_address is not None:
            self.extended_address = extended_address
        if street_address is not None:
            self.street_address = street_address
        if locality is not None:
            self.locality = locality
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country

    @property
    def type(self):
        """Gets the type of this SystemuserputAddresses.  # noqa: E501


        :return: The type of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemuserputAddresses.


        :param type: The type of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 1024:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `1024`")  # noqa: E501

        self._type = type

    @property
    def po_box(self):
        """Gets the po_box of this SystemuserputAddresses.  # noqa: E501


        :return: The po_box of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._po_box

    @po_box.setter
    def po_box(self, po_box):
        """Sets the po_box of this SystemuserputAddresses.


        :param po_box: The po_box of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if po_box is not None and len(po_box) > 1024:
            raise ValueError("Invalid value for `po_box`, length must be less than or equal to `1024`")  # noqa: E501

        self._po_box = po_box

    @property
    def extended_address(self):
        """Gets the extended_address of this SystemuserputAddresses.  # noqa: E501


        :return: The extended_address of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._extended_address

    @extended_address.setter
    def extended_address(self, extended_address):
        """Sets the extended_address of this SystemuserputAddresses.


        :param extended_address: The extended_address of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if extended_address is not None and len(extended_address) > 1024:
            raise ValueError("Invalid value for `extended_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._extended_address = extended_address

    @property
    def street_address(self):
        """Gets the street_address of this SystemuserputAddresses.  # noqa: E501


        :return: The street_address of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this SystemuserputAddresses.


        :param street_address: The street_address of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if street_address is not None and len(street_address) > 1024:
            raise ValueError("Invalid value for `street_address`, length must be less than or equal to `1024`")  # noqa: E501

        self._street_address = street_address

    @property
    def locality(self):
        """Gets the locality of this SystemuserputAddresses.  # noqa: E501


        :return: The locality of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this SystemuserputAddresses.


        :param locality: The locality of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if locality is not None and len(locality) > 1024:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `1024`")  # noqa: E501

        self._locality = locality

    @property
    def region(self):
        """Gets the region of this SystemuserputAddresses.  # noqa: E501


        :return: The region of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SystemuserputAddresses.


        :param region: The region of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if region is not None and len(region) > 1024:
            raise ValueError("Invalid value for `region`, length must be less than or equal to `1024`")  # noqa: E501

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this SystemuserputAddresses.  # noqa: E501


        :return: The postal_code of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SystemuserputAddresses.


        :param postal_code: The postal_code of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 1024:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `1024`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this SystemuserputAddresses.  # noqa: E501


        :return: The country of this SystemuserputAddresses.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SystemuserputAddresses.


        :param country: The country of this SystemuserputAddresses.  # noqa: E501
        :type: str
        """
        if country is not None and len(country) > 1024:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `1024`")  # noqa: E501

        self._country = country

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, SystemuserputAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
