# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import jcapiv1
from jcapiv1.api.applications_api import ApplicationsApi  # noqa: E501
from jcapiv1.rest import ApiException


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = jcapiv1.api.applications_api.ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_applications_list(self):
        """Test case for applications_list

        Applications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
