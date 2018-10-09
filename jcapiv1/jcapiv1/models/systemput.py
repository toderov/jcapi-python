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

from jcapiv1.models.systemput_agent_bound_messages import SystemputAgentBoundMessages  # noqa: F401,E501


class Systemput(object):
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
        'display_name': 'str',
        'allow_ssh_password_authentication': 'bool',
        'allow_ssh_root_login': 'bool',
        'allow_multi_factor_authentication': 'bool',
        'allow_public_key_authentication': 'bool',
        'agent_bound_messages': 'list[SystemputAgentBoundMessages]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'allow_ssh_password_authentication': 'allowSshPasswordAuthentication',
        'allow_ssh_root_login': 'allowSshRootLogin',
        'allow_multi_factor_authentication': 'allowMultiFactorAuthentication',
        'allow_public_key_authentication': 'allowPublicKeyAuthentication',
        'agent_bound_messages': 'agentBoundMessages',
        'tags': 'tags'
    }

    def __init__(self, display_name=None, allow_ssh_password_authentication=None, allow_ssh_root_login=None, allow_multi_factor_authentication=None, allow_public_key_authentication=None, agent_bound_messages=None, tags=None):  # noqa: E501
        """Systemput - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._allow_ssh_password_authentication = None
        self._allow_ssh_root_login = None
        self._allow_multi_factor_authentication = None
        self._allow_public_key_authentication = None
        self._agent_bound_messages = None
        self._tags = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if allow_ssh_password_authentication is not None:
            self.allow_ssh_password_authentication = allow_ssh_password_authentication
        if allow_ssh_root_login is not None:
            self.allow_ssh_root_login = allow_ssh_root_login
        if allow_multi_factor_authentication is not None:
            self.allow_multi_factor_authentication = allow_multi_factor_authentication
        if allow_public_key_authentication is not None:
            self.allow_public_key_authentication = allow_public_key_authentication
        if agent_bound_messages is not None:
            self.agent_bound_messages = agent_bound_messages
        if tags is not None:
            self.tags = tags

    @property
    def display_name(self):
        """Gets the display_name of this Systemput.  # noqa: E501


        :return: The display_name of this Systemput.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Systemput.


        :param display_name: The display_name of this Systemput.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def allow_ssh_password_authentication(self):
        """Gets the allow_ssh_password_authentication of this Systemput.  # noqa: E501


        :return: The allow_ssh_password_authentication of this Systemput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_password_authentication

    @allow_ssh_password_authentication.setter
    def allow_ssh_password_authentication(self, allow_ssh_password_authentication):
        """Sets the allow_ssh_password_authentication of this Systemput.


        :param allow_ssh_password_authentication: The allow_ssh_password_authentication of this Systemput.  # noqa: E501
        :type: bool
        """

        self._allow_ssh_password_authentication = allow_ssh_password_authentication

    @property
    def allow_ssh_root_login(self):
        """Gets the allow_ssh_root_login of this Systemput.  # noqa: E501


        :return: The allow_ssh_root_login of this Systemput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ssh_root_login

    @allow_ssh_root_login.setter
    def allow_ssh_root_login(self, allow_ssh_root_login):
        """Sets the allow_ssh_root_login of this Systemput.


        :param allow_ssh_root_login: The allow_ssh_root_login of this Systemput.  # noqa: E501
        :type: bool
        """

        self._allow_ssh_root_login = allow_ssh_root_login

    @property
    def allow_multi_factor_authentication(self):
        """Gets the allow_multi_factor_authentication of this Systemput.  # noqa: E501


        :return: The allow_multi_factor_authentication of this Systemput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_multi_factor_authentication

    @allow_multi_factor_authentication.setter
    def allow_multi_factor_authentication(self, allow_multi_factor_authentication):
        """Sets the allow_multi_factor_authentication of this Systemput.


        :param allow_multi_factor_authentication: The allow_multi_factor_authentication of this Systemput.  # noqa: E501
        :type: bool
        """

        self._allow_multi_factor_authentication = allow_multi_factor_authentication

    @property
    def allow_public_key_authentication(self):
        """Gets the allow_public_key_authentication of this Systemput.  # noqa: E501


        :return: The allow_public_key_authentication of this Systemput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_public_key_authentication

    @allow_public_key_authentication.setter
    def allow_public_key_authentication(self, allow_public_key_authentication):
        """Sets the allow_public_key_authentication of this Systemput.


        :param allow_public_key_authentication: The allow_public_key_authentication of this Systemput.  # noqa: E501
        :type: bool
        """

        self._allow_public_key_authentication = allow_public_key_authentication

    @property
    def agent_bound_messages(self):
        """Gets the agent_bound_messages of this Systemput.  # noqa: E501


        :return: The agent_bound_messages of this Systemput.  # noqa: E501
        :rtype: list[SystemputAgentBoundMessages]
        """
        return self._agent_bound_messages

    @agent_bound_messages.setter
    def agent_bound_messages(self, agent_bound_messages):
        """Sets the agent_bound_messages of this Systemput.


        :param agent_bound_messages: The agent_bound_messages of this Systemput.  # noqa: E501
        :type: list[SystemputAgentBoundMessages]
        """

        self._agent_bound_messages = agent_bound_messages

    @property
    def tags(self):
        """Gets the tags of this Systemput.  # noqa: E501


        :return: The tags of this Systemput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Systemput.


        :param tags: The tags of this Systemput.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Systemput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
