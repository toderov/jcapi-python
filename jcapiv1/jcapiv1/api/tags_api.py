# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jcapiv1.api_client import ApiClient


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tags_delete(self, name, content_type, accept, **kwargs):  # noqa: E501
        """Delete a Tag  # noqa: E501

        Hidden as Tags is deprecated  Delete a Tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_delete(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tags_delete_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_delete_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
            return data

    def tags_delete_with_http_info(self, name, content_type, accept, **kwargs):  # noqa: E501
        """Delete a Tag  # noqa: E501

        Hidden as Tags is deprecated  Delete a Tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_delete_with_http_info(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'content_type', 'accept']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `tags_delete`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `tags_delete`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `tags_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/tags/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_get(self, name, content_type, accept, **kwargs):  # noqa: E501
        """List a Tag  # noqa: E501

        Hidden as Tags is deprecated  Returns a specific tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_get(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tags_get_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_get_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
            return data

    def tags_get_with_http_info(self, name, content_type, accept, **kwargs):  # noqa: E501
        """List a Tag  # noqa: E501

        Hidden as Tags is deprecated  Returns a specific tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_get_with_http_info(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'content_type', 'accept', 'fields', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `tags_get`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `tags_get`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `tags_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/Tags/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_list(self, content_type, accept, **kwargs):  # noqa: E501
        """List All Tags  # noqa: E501

        Hidden as Tags is deprecated  Returns all Tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_list(content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :return: Tagslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tags_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def tags_list_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """List All Tags  # noqa: E501

        Hidden as Tags is deprecated  Returns all Tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_list_with_http_info(content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :return: Tagslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'fields', 'limit', 'skip', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `tags_list`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `tags_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tagslist',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_post(self, content_type, accept, **kwargs):  # noqa: E501
        """Create a Tag  # noqa: E501

        Hidden as Tags is deprecated  Create a tag.  ### Examples #### Create a new Tag  ``` curl \\   -d '{\"name\" : \"Developers\"}' \\   -X 'POST' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' \\   -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\   \"https://console.jumpcloud.com/api/tags\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_post(content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Tagpost body:
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tags_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def tags_post_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """Create a Tag  # noqa: E501

        Hidden as Tags is deprecated  Create a tag.  ### Examples #### Create a new Tag  ``` curl \\   -d '{\"name\" : \"Developers\"}' \\   -X 'POST' \\   -H 'Content-Type: application/json' \\   -H 'Accept: application/json' \\   -H \"x-api-key: [YOUR_API_KEY_HERE]\" \\   \"https://console.jumpcloud.com/api/tags\" ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_post_with_http_info(content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Tagpost body:
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `tags_post`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `tags_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/tags', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_put(self, name, content_type, accept, **kwargs):  # noqa: E501
        """Update a Tag  # noqa: E501

        Hidden as Tags is deprecated  Update a specific tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_put(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Tagput body:
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tags_put_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_put_with_http_info(name, content_type, accept, **kwargs)  # noqa: E501
            return data

    def tags_put_with_http_info(self, name, content_type, accept, **kwargs):  # noqa: E501
        """Update a Tag  # noqa: E501

        Hidden as Tags is deprecated  Update a specific tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tags_put_with_http_info(name, content_type, accept, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Tagput body:
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'content_type', 'accept', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `tags_put`")  # noqa: E501
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `tags_put`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `tags_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/Tag/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Tag',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
