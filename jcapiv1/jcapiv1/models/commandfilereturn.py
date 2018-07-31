# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Commandfilereturn(object):
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
        'total_count': 'int',
        'results': 'CommandfilereturnResults'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'results': 'results'
    }

    def __init__(self, total_count=None, results=None):
        """
        Commandfilereturn - a model defined in Swagger
        """

        self._total_count = None
        self._results = None

        if total_count is not None:
          self.total_count = total_count
        if results is not None:
          self.results = results

    @property
    def total_count(self):
        """
        Gets the total_count of this Commandfilereturn.
        The total number of commands files

        :return: The total_count of this Commandfilereturn.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this Commandfilereturn.
        The total number of commands files

        :param total_count: The total_count of this Commandfilereturn.
        :type: int
        """

        self._total_count = total_count

    @property
    def results(self):
        """
        Gets the results of this Commandfilereturn.

        :return: The results of this Commandfilereturn.
        :rtype: CommandfilereturnResults
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this Commandfilereturn.

        :param results: The results of this Commandfilereturn.
        :type: CommandfilereturnResults
        """

        self._results = results

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
        if not isinstance(other, Commandfilereturn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
