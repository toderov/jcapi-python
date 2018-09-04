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


class Command(object):
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
        'name': 'str',
        'command': 'str',
        'command_type': 'str',
        'command_runners': 'list[str]',
        'user': 'str',
        'sudo': 'bool',
        'systems': 'list[str]',
        'launch_type': 'str',
        'listens_to': 'str',
        'schedule_repeat_type': 'str',
        'schedule': 'str',
        'files': 'list[str]',
        'timeout': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'name': 'name',
        'command': 'command',
        'command_type': 'commandType',
        'command_runners': 'commandRunners',
        'user': 'user',
        'sudo': 'sudo',
        'systems': 'systems',
        'launch_type': 'launchType',
        'listens_to': 'listensTo',
        'schedule_repeat_type': 'scheduleRepeatType',
        'schedule': 'schedule',
        'files': 'files',
        'timeout': 'timeout',
        'organization': 'organization'
    }

    def __init__(self, name=None, command=None, command_type=None, command_runners=None, user=None, sudo=None, systems=None, launch_type=None, listens_to=None, schedule_repeat_type=None, schedule=None, files=None, timeout=None, organization=None):
        """
        Command - a model defined in Swagger
        """

        self._name = None
        self._command = None
        self._command_type = None
        self._command_runners = None
        self._user = None
        self._sudo = None
        self._systems = None
        self._launch_type = None
        self._listens_to = None
        self._schedule_repeat_type = None
        self._schedule = None
        self._files = None
        self._timeout = None
        self._organization = None

        if name is not None:
          self.name = name
        self.command = command
        if command_type is not None:
          self.command_type = command_type
        if command_runners is not None:
          self.command_runners = command_runners
        self.user = user
        if sudo is not None:
          self.sudo = sudo
        if systems is not None:
          self.systems = systems
        if launch_type is not None:
          self.launch_type = launch_type
        if listens_to is not None:
          self.listens_to = listens_to
        if schedule_repeat_type is not None:
          self.schedule_repeat_type = schedule_repeat_type
        if schedule is not None:
          self.schedule = schedule
        if files is not None:
          self.files = files
        if timeout is not None:
          self.timeout = timeout
        if organization is not None:
          self.organization = organization

    @property
    def name(self):
        """
        Gets the name of this Command.

        :return: The name of this Command.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Command.

        :param name: The name of this Command.
        :type: str
        """

        self._name = name

    @property
    def command(self):
        """
        Gets the command of this Command.
        The command to execute on the server.

        :return: The command of this Command.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this Command.
        The command to execute on the server.

        :param command: The command of this Command.
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")

        self._command = command

    @property
    def command_type(self):
        """
        Gets the command_type of this Command.
        The Command OS

        :return: The command_type of this Command.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Sets the command_type of this Command.
        The Command OS

        :param command_type: The command_type of this Command.
        :type: str
        """

        self._command_type = command_type

    @property
    def command_runners(self):
        """
        Gets the command_runners of this Command.
        an array of IDs of the Command Runner Users that can execute this command.

        :return: The command_runners of this Command.
        :rtype: list[str]
        """
        return self._command_runners

    @command_runners.setter
    def command_runners(self, command_runners):
        """
        Sets the command_runners of this Command.
        an array of IDs of the Command Runner Users that can execute this command.

        :param command_runners: The command_runners of this Command.
        :type: list[str]
        """

        self._command_runners = command_runners

    @property
    def user(self):
        """
        Gets the user of this Command.
        The ID of the system user to run the command as.

        :return: The user of this Command.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Command.
        The ID of the system user to run the command as.

        :param user: The user of this Command.
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

    @property
    def sudo(self):
        """
        Gets the sudo of this Command.
        

        :return: The sudo of this Command.
        :rtype: bool
        """
        return self._sudo

    @sudo.setter
    def sudo(self, sudo):
        """
        Sets the sudo of this Command.
        

        :param sudo: The sudo of this Command.
        :type: bool
        """

        self._sudo = sudo

    @property
    def systems(self):
        """
        Gets the systems of this Command.
        An array of system IDs to run the command on. Not available if you are using Groups.

        :return: The systems of this Command.
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """
        Sets the systems of this Command.
        An array of system IDs to run the command on. Not available if you are using Groups.

        :param systems: The systems of this Command.
        :type: list[str]
        """

        self._systems = systems

    @property
    def launch_type(self):
        """
        Gets the launch_type of this Command.
        How the command will execute.

        :return: The launch_type of this Command.
        :rtype: str
        """
        return self._launch_type

    @launch_type.setter
    def launch_type(self, launch_type):
        """
        Sets the launch_type of this Command.
        How the command will execute.

        :param launch_type: The launch_type of this Command.
        :type: str
        """

        self._launch_type = launch_type

    @property
    def listens_to(self):
        """
        Gets the listens_to of this Command.
        

        :return: The listens_to of this Command.
        :rtype: str
        """
        return self._listens_to

    @listens_to.setter
    def listens_to(self, listens_to):
        """
        Sets the listens_to of this Command.
        

        :param listens_to: The listens_to of this Command.
        :type: str
        """

        self._listens_to = listens_to

    @property
    def schedule_repeat_type(self):
        """
        Gets the schedule_repeat_type of this Command.
        When the command will repeat.

        :return: The schedule_repeat_type of this Command.
        :rtype: str
        """
        return self._schedule_repeat_type

    @schedule_repeat_type.setter
    def schedule_repeat_type(self, schedule_repeat_type):
        """
        Sets the schedule_repeat_type of this Command.
        When the command will repeat.

        :param schedule_repeat_type: The schedule_repeat_type of this Command.
        :type: str
        """

        self._schedule_repeat_type = schedule_repeat_type

    @property
    def schedule(self):
        """
        Gets the schedule of this Command.
        A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately. 

        :return: The schedule of this Command.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this Command.
        A crontab that consists of: [ (seconds) (minutes) (hours) (days of month) (months) (weekdays) ] or [ immediate ]. If you send this as an empty string, it will run immediately. 

        :param schedule: The schedule of this Command.
        :type: str
        """

        self._schedule = schedule

    @property
    def files(self):
        """
        Gets the files of this Command.
        An array of file IDs to include with the command.

        :return: The files of this Command.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this Command.
        An array of file IDs to include with the command.

        :param files: The files of this Command.
        :type: list[str]
        """

        self._files = files

    @property
    def timeout(self):
        """
        Gets the timeout of this Command.
        The time in seconds to allow the command to run for.

        :return: The timeout of this Command.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this Command.
        The time in seconds to allow the command to run for.

        :param timeout: The timeout of this Command.
        :type: str
        """

        self._timeout = timeout

    @property
    def organization(self):
        """
        Gets the organization of this Command.
        The ID of the organization.

        :return: The organization of this Command.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Command.
        The ID of the organization.

        :param organization: The organization of this Command.
        :type: str
        """

        self._organization = organization

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
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
