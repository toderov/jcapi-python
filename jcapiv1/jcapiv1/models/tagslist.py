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

from jcapiv1.models.tag import Tag  # noqa: F401,E501


class Tagslist(object):
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
        'total_count': 'int',
        'results': 'list[Tag]'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'results': 'results'
    }

    def __init__(self, total_count=None, results=None):  # noqa: E501
        """Tagslist - a model defined in Swagger"""  # noqa: E501

        self._total_count = None
        self._results = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if results is not None:
            self.results = results

    @property
    def total_count(self):
        """Gets the total_count of this Tagslist.  # noqa: E501

        The total number of tags.  # noqa: E501

        :return: The total_count of this Tagslist.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Tagslist.

        The total number of tags.  # noqa: E501

        :param total_count: The total_count of this Tagslist.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def results(self):
        """Gets the results of this Tagslist.  # noqa: E501

        The list of tags.  # noqa: E501

        :return: The results of this Tagslist.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this Tagslist.

        The list of tags.  # noqa: E501

        :param results: The results of this Tagslist.  # noqa: E501
        :type: list[Tag]
        """

        self._results = results

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
        if not isinstance(other, Tagslist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
