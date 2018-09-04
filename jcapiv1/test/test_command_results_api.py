# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv1
from jcapiv1.rest import ApiException
from jcapiv1.apis.command_results_api import CommandResultsApi


class TestCommandResultsApi(unittest.TestCase):
    """ CommandResultsApi unit test stubs """

    def setUp(self):
        self.api = jcapiv1.apis.command_results_api.CommandResultsApi()

    def tearDown(self):
        pass

    def test_command_results_delete(self):
        """
        Test case for command_results_delete

        Delete a Command result
        """
        pass

    def test_command_results_get(self):
        """
        Test case for command_results_get

        List an individual Command result
        """
        pass

    def test_command_results_list(self):
        """
        Test case for command_results_list

        List all Command Results
        """
        pass


if __name__ == '__main__':
    unittest.main()
