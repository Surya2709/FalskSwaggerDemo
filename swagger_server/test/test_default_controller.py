# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alert import Alert  # noqa: E501
from swagger_server.models.alert_array import AlertArray  # noqa: E501
from swagger_server.models.updatealert import Updatealert  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_alert_delete(self):
        """Test case for alert_delete

        delete alert
        """
        query_string = [('alert_id', 'alert_id_example')]
        response = self.client.open(
            '/Surya_Ramachandran/userAlert/1.0.0/Alert',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alert_get(self):
        """Test case for alert_get

        obtain alert  list
        """
        query_string = [('alert_id', 'alert_id_example')]
        response = self.client.open(
            '/Surya_Ramachandran/userAlert/1.0.0/Alert',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alert_post(self):
        """Test case for alert_post

        add alerts
        """
        body = [Alert()]
        response = self.client.open(
            '/Surya_Ramachandran/userAlert/1.0.0/Alert',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_alert_put(self):
        """Test case for alert_put

        update the  alerts
        """
        body = Updatealert()
        response = self.client.open(
            '/Surya_Ramachandran/userAlert/1.0.0/Alert',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
