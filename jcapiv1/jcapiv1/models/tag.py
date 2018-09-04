# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Tag(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'id': 'str',
        'name': 'str',
        'systems': 'list[str]',
        'systemusers': 'list[str]',
        'regular_expressions': 'list[str]',
        'externally_managed': 'bool',
        'external_dn': 'str',
        'external_source_type': 'str',
        'send_to_ldap': 'bool',
        'expired': 'bool',
        'group_gid': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'id': '_id',
        'name': 'name',
        'systems': 'systems',
        'systemusers': 'systemusers',
        'regular_expressions': 'regularExpressions',
        'externally_managed': 'externallyManaged',
        'external_dn': 'externalDN',
        'external_source_type': 'externalSourceType',
        'send_to_ldap': 'sendToLDAP',
        'expired': 'expired',
        'group_gid': 'groupGid',
        'group_name': 'groupName'
    }

    def __init__(self, id=None, name=None, systems=None, systemusers=None, regular_expressions=None, externally_managed=None, external_dn=None, external_source_type=None, send_to_ldap=None, expired=None, group_gid=None, group_name=None):
        """
        Tag - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._systems = None
        self._systemusers = None
        self._regular_expressions = None
        self._externally_managed = None
        self._external_dn = None
        self._external_source_type = None
        self._send_to_ldap = None
        self._expired = None
        self._group_gid = None
        self._group_name = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if systems is not None:
          self.systems = systems
        if systemusers is not None:
          self.systemusers = systemusers
        if regular_expressions is not None:
          self.regular_expressions = regular_expressions
        if externally_managed is not None:
          self.externally_managed = externally_managed
        if external_dn is not None:
          self.external_dn = external_dn
        if external_source_type is not None:
          self.external_source_type = external_source_type
        if send_to_ldap is not None:
          self.send_to_ldap = send_to_ldap
        if expired is not None:
          self.expired = expired
        if group_gid is not None:
          self.group_gid = group_gid
        if group_name is not None:
          self.group_name = group_name

    @property
    def id(self):
        """
        Gets the id of this Tag.

        :return: The id of this Tag.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tag.

        :param id: The id of this Tag.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Tag.
        A unique name for the Tag.

        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tag.
        A unique name for the Tag.

        :param name: The name of this Tag.
        :type: str
        """

        self._name = name

    @property
    def systems(self):
        """
        Gets the systems of this Tag.
        An array of system ids that are associated to the Tag.

        :return: The systems of this Tag.
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """
        Sets the systems of this Tag.
        An array of system ids that are associated to the Tag.

        :param systems: The systems of this Tag.
        :type: list[str]
        """

        self._systems = systems

    @property
    def systemusers(self):
        """
        Gets the systemusers of this Tag.
        An array of system user ids that are associated to the Tag.

        :return: The systemusers of this Tag.
        :rtype: list[str]
        """
        return self._systemusers

    @systemusers.setter
    def systemusers(self, systemusers):
        """
        Sets the systemusers of this Tag.
        An array of system user ids that are associated to the Tag.

        :param systemusers: The systemusers of this Tag.
        :type: list[str]
        """

        self._systemusers = systemusers

    @property
    def regular_expressions(self):
        """
        Gets the regular_expressions of this Tag.

        :return: The regular_expressions of this Tag.
        :rtype: list[str]
        """
        return self._regular_expressions

    @regular_expressions.setter
    def regular_expressions(self, regular_expressions):
        """
        Sets the regular_expressions of this Tag.

        :param regular_expressions: The regular_expressions of this Tag.
        :type: list[str]
        """

        self._regular_expressions = regular_expressions

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this Tag.

        :return: The externally_managed of this Tag.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this Tag.

        :param externally_managed: The externally_managed of this Tag.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def external_dn(self):
        """
        Gets the external_dn of this Tag.

        :return: The external_dn of this Tag.
        :rtype: str
        """
        return self._external_dn

    @external_dn.setter
    def external_dn(self, external_dn):
        """
        Sets the external_dn of this Tag.

        :param external_dn: The external_dn of this Tag.
        :type: str
        """

        self._external_dn = external_dn

    @property
    def external_source_type(self):
        """
        Gets the external_source_type of this Tag.

        :return: The external_source_type of this Tag.
        :rtype: str
        """
        return self._external_source_type

    @external_source_type.setter
    def external_source_type(self, external_source_type):
        """
        Sets the external_source_type of this Tag.

        :param external_source_type: The external_source_type of this Tag.
        :type: str
        """

        self._external_source_type = external_source_type

    @property
    def send_to_ldap(self):
        """
        Gets the send_to_ldap of this Tag.

        :return: The send_to_ldap of this Tag.
        :rtype: bool
        """
        return self._send_to_ldap

    @send_to_ldap.setter
    def send_to_ldap(self, send_to_ldap):
        """
        Sets the send_to_ldap of this Tag.

        :param send_to_ldap: The send_to_ldap of this Tag.
        :type: bool
        """

        self._send_to_ldap = send_to_ldap

    @property
    def expired(self):
        """
        Gets the expired of this Tag.

        :return: The expired of this Tag.
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """
        Sets the expired of this Tag.

        :param expired: The expired of this Tag.
        :type: bool
        """

        self._expired = expired

    @property
    def group_gid(self):
        """
        Gets the group_gid of this Tag.

        :return: The group_gid of this Tag.
        :rtype: str
        """
        return self._group_gid

    @group_gid.setter
    def group_gid(self, group_gid):
        """
        Sets the group_gid of this Tag.

        :param group_gid: The group_gid of this Tag.
        :type: str
        """

        self._group_gid = group_gid

    @property
    def group_name(self):
        """
        Gets the group_name of this Tag.

        :return: The group_name of this Tag.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this Tag.

        :param group_name: The group_name of this Tag.
        :type: str
        """

        self._group_name = group_name

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
        if not isinstance(other, Tag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
