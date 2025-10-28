#!/usr/bin/env python3
import asyncio
import os
import sys
import unittest
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import AsyncTwoCaptcha

captcha_id = '123'
code = 'abcd'


class AsyncApiClient():
    async def in_(self, files={}, **kwargs):
        self.incomings = kwargs
        self.incoming_files = files

        return 'OK|' + captcha_id

    async def res(self, **kwargs):
        return 'OK|' + code  # {'code': code}


class AsyncAbstractTest(unittest.TestCase):
    def setUp(self):
        self.solver = AsyncTwoCaptcha('API_KEY', pollingInterval=1)
        self.solver.api_client = AsyncApiClient()

    def send_return(self, for_send, method, **kwargs):
        asyncio.run(self._async_send_return(for_send, method, **kwargs))

    async def _async_send_return(self, for_send, method, **kwargs):
        file = kwargs.pop('file', {})
        file = kwargs.pop('files', file)

        result = await method(file, **kwargs) if file else await method(**kwargs)

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
        asyncio.run(self._async_invalid_file(method, **kwargs))

    async def _async_invalid_file(self, method, **kwargs):
        with self.assertRaises(self.solver.exceptions):
            await method('lost_file', **kwargs)

    def too_many_files(self, method, **kwargs):
        asyncio.run(self._async_too_many_files(method, **kwargs))

    async def _async_too_many_files(self, method, **kwargs):
        images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
        files = [str(images_path / 'rotate.jpg')] * (self.solver.max_files + 1)
        with self.assertRaises(self.solver.exceptions):
            await method(files, **kwargs)


if __name__ == '__main__':
    unittest.main()
