#!/usr/bin/env python3
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

captcha_id = '123'
code = 'abcd'


class ApiClient():
    def in_(self, files={}, **kwargs):

        self.incomings = kwargs
        self.incoming_files = files

        return 'OK|' + captcha_id

    def res(self, **kwargs):

        return 'OK|' + code  # {'code': code}


class AbstractTest(unittest.TestCase):
    def setUp(self):

        self.solver = TwoCaptcha('API_KEY', pollingInterval=1)
        self.solver.api_client = ApiClient()

    def send_return(self, for_send, method, **kwargs):

        file = kwargs.pop('file', {})
        file = kwargs.pop('files', file)

        result = method(file, **kwargs) if file else method(**kwargs)

        incomings = self.solver.api_client.incomings
        for_send.update({'key': 'API_KEY'})
        for_send.update({'soft_id': 4580})

        files = for_send.pop('files', {})
        self.assertEqual(incomings, for_send)

        incoming_files = self.solver.api_client.incoming_files
        incoming_files and self.assertEqual(incoming_files, files)

        self.assertIsInstance(result, dict)
        self.assertIn('code', result)
        self.assertEqual(result['code'], code)

    def invalid_file(self, method, **kwargs):

        self.assertRaises(self.solver.exceptions, method, 'lost_file',
                          **kwargs)

    def too_many_files(self, method, **kwargs):

        files = ['../examples/images/rotate.jpg'] * (self.solver.max_files + 1)
        self.assertRaises(self.solver.exceptions, method, files, **kwargs)


if __name__ == '__main__':

    unittest.main()
