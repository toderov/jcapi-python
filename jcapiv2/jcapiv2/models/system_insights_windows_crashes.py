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


class SystemInsightsWindowsCrashes(object):
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
        'build_number': 'int',
        'command_line': 'str',
        'crash_path': 'str',
        'current_directory': 'str',
        '_datetime': 'str',
        'exception_address': 'str',
        'exception_code': 'str',
        'exception_message': 'str',
        'machine_name': 'str',
        'major_version': 'int',
        'minor_version': 'int',
        'module': 'str',
        'path': 'str',
        'pid': 'str',
        'process_uptime': 'str',
        'registers': 'str',
        'stack_trace': 'str',
        'tid': 'str',
        'type': 'str',
        'username': 'str',
        'version': 'str'
    }

    attribute_map = {
        'build_number': 'build_number',
        'command_line': 'command_line',
        'crash_path': 'crash_path',
        'current_directory': 'current_directory',
        '_datetime': 'datetime',
        'exception_address': 'exception_address',
        'exception_code': 'exception_code',
        'exception_message': 'exception_message',
        'machine_name': 'machine_name',
        'major_version': 'major_version',
        'minor_version': 'minor_version',
        'module': 'module',
        'path': 'path',
        'pid': 'pid',
        'process_uptime': 'process_uptime',
        'registers': 'registers',
        'stack_trace': 'stack_trace',
        'tid': 'tid',
        'type': 'type',
        'username': 'username',
        'version': 'version'
    }

    def __init__(self, build_number=None, command_line=None, crash_path=None, current_directory=None, _datetime=None, exception_address=None, exception_code=None, exception_message=None, machine_name=None, major_version=None, minor_version=None, module=None, path=None, pid=None, process_uptime=None, registers=None, stack_trace=None, tid=None, type=None, username=None, version=None):  # noqa: E501
        """SystemInsightsWindowsCrashes - a model defined in Swagger"""  # noqa: E501

        self._build_number = None
        self._command_line = None
        self._crash_path = None
        self._current_directory = None
        self.__datetime = None
        self._exception_address = None
        self._exception_code = None
        self._exception_message = None
        self._machine_name = None
        self._major_version = None
        self._minor_version = None
        self._module = None
        self._path = None
        self._pid = None
        self._process_uptime = None
        self._registers = None
        self._stack_trace = None
        self._tid = None
        self._type = None
        self._username = None
        self._version = None
        self.discriminator = None

        if build_number is not None:
            self.build_number = build_number
        if command_line is not None:
            self.command_line = command_line
        if crash_path is not None:
            self.crash_path = crash_path
        if current_directory is not None:
            self.current_directory = current_directory
        if _datetime is not None:
            self._datetime = _datetime
        if exception_address is not None:
            self.exception_address = exception_address
        if exception_code is not None:
            self.exception_code = exception_code
        if exception_message is not None:
            self.exception_message = exception_message
        if machine_name is not None:
            self.machine_name = machine_name
        if major_version is not None:
            self.major_version = major_version
        if minor_version is not None:
            self.minor_version = minor_version
        if module is not None:
            self.module = module
        if path is not None:
            self.path = path
        if pid is not None:
            self.pid = pid
        if process_uptime is not None:
            self.process_uptime = process_uptime
        if registers is not None:
            self.registers = registers
        if stack_trace is not None:
            self.stack_trace = stack_trace
        if tid is not None:
            self.tid = tid
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if version is not None:
            self.version = version

    @property
    def build_number(self):
        """Gets the build_number of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The build_number of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this SystemInsightsWindowsCrashes.


        :param build_number: The build_number of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: int
        """

        self._build_number = build_number

    @property
    def command_line(self):
        """Gets the command_line of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The command_line of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._command_line

    @command_line.setter
    def command_line(self, command_line):
        """Sets the command_line of this SystemInsightsWindowsCrashes.


        :param command_line: The command_line of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._command_line = command_line

    @property
    def crash_path(self):
        """Gets the crash_path of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The crash_path of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._crash_path

    @crash_path.setter
    def crash_path(self, crash_path):
        """Sets the crash_path of this SystemInsightsWindowsCrashes.


        :param crash_path: The crash_path of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._crash_path = crash_path

    @property
    def current_directory(self):
        """Gets the current_directory of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The current_directory of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._current_directory

    @current_directory.setter
    def current_directory(self, current_directory):
        """Sets the current_directory of this SystemInsightsWindowsCrashes.


        :param current_directory: The current_directory of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._current_directory = current_directory

    @property
    def _datetime(self):
        """Gets the _datetime of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The _datetime of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this SystemInsightsWindowsCrashes.


        :param _datetime: The _datetime of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self.__datetime = _datetime

    @property
    def exception_address(self):
        """Gets the exception_address of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The exception_address of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._exception_address

    @exception_address.setter
    def exception_address(self, exception_address):
        """Sets the exception_address of this SystemInsightsWindowsCrashes.


        :param exception_address: The exception_address of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._exception_address = exception_address

    @property
    def exception_code(self):
        """Gets the exception_code of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The exception_code of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._exception_code

    @exception_code.setter
    def exception_code(self, exception_code):
        """Sets the exception_code of this SystemInsightsWindowsCrashes.


        :param exception_code: The exception_code of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._exception_code = exception_code

    @property
    def exception_message(self):
        """Gets the exception_message of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The exception_message of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """Sets the exception_message of this SystemInsightsWindowsCrashes.


        :param exception_message: The exception_message of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._exception_message = exception_message

    @property
    def machine_name(self):
        """Gets the machine_name of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The machine_name of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this SystemInsightsWindowsCrashes.


        :param machine_name: The machine_name of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._machine_name = machine_name

    @property
    def major_version(self):
        """Gets the major_version of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The major_version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this SystemInsightsWindowsCrashes.


        :param major_version: The major_version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: int
        """

        self._major_version = major_version

    @property
    def minor_version(self):
        """Gets the minor_version of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The minor_version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """Sets the minor_version of this SystemInsightsWindowsCrashes.


        :param minor_version: The minor_version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: int
        """

        self._minor_version = minor_version

    @property
    def module(self):
        """Gets the module of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The module of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this SystemInsightsWindowsCrashes.


        :param module: The module of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._module = module

    @property
    def path(self):
        """Gets the path of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The path of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SystemInsightsWindowsCrashes.


        :param path: The path of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def pid(self):
        """Gets the pid of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The pid of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this SystemInsightsWindowsCrashes.


        :param pid: The pid of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._pid = pid

    @property
    def process_uptime(self):
        """Gets the process_uptime of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The process_uptime of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._process_uptime

    @process_uptime.setter
    def process_uptime(self, process_uptime):
        """Sets the process_uptime of this SystemInsightsWindowsCrashes.


        :param process_uptime: The process_uptime of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._process_uptime = process_uptime

    @property
    def registers(self):
        """Gets the registers of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The registers of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._registers

    @registers.setter
    def registers(self, registers):
        """Sets the registers of this SystemInsightsWindowsCrashes.


        :param registers: The registers of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._registers = registers

    @property
    def stack_trace(self):
        """Gets the stack_trace of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The stack_trace of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this SystemInsightsWindowsCrashes.


        :param stack_trace: The stack_trace of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

    @property
    def tid(self):
        """Gets the tid of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The tid of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._tid

    @tid.setter
    def tid(self, tid):
        """Sets the tid of this SystemInsightsWindowsCrashes.


        :param tid: The tid of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._tid = tid

    @property
    def type(self):
        """Gets the type of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The type of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsWindowsCrashes.


        :param type: The type of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def username(self):
        """Gets the username of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The username of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SystemInsightsWindowsCrashes.


        :param username: The username of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def version(self):
        """Gets the version of this SystemInsightsWindowsCrashes.  # noqa: E501


        :return: The version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SystemInsightsWindowsCrashes.


        :param version: The version of this SystemInsightsWindowsCrashes.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(SystemInsightsWindowsCrashes, dict):
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
        if not isinstance(other, SystemInsightsWindowsCrashes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
