# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ActiveDirectoryAgentListOutput(object):
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
        'id': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state'
    }

    def __init__(self, id=None, state=None):  # noqa: E501
        """ActiveDirectoryAgentListOutput - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this ActiveDirectoryAgentListOutput.  # noqa: E501

        ObjectID of this Active Directory Agent.  # noqa: E501

        :return: The id of this ActiveDirectoryAgentListOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActiveDirectoryAgentListOutput.

        ObjectID of this Active Directory Agent.  # noqa: E501

        :param id: The id of this ActiveDirectoryAgentListOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ActiveDirectoryAgentListOutput.  # noqa: E501


        :return: The state of this ActiveDirectoryAgentListOutput.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ActiveDirectoryAgentListOutput.


        :param state: The state of this ActiveDirectoryAgentListOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["unsealed", "active", "inactive"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if issubclass(ActiveDirectoryAgentListOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActiveDirectoryAgentListOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
