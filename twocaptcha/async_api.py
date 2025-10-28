#!/usr/bin/env python3

from contextlib import AsyncExitStack

import aiofiles
import httpx

try:
    from .exceptions.api import NetworkException, ApiException
except ImportError:
    from twocaptcha.exceptions.api import NetworkException, ApiException


class AsyncApiClient():
    def __init__(self, post_url='2captcha.com'):
        self.post_url = post_url

    async def in_(self, files={}, **kwargs):
        '''
        
        sends POST-request (files and/or params) to solve captcha

        Parameters
        ----------
        files : TYPE, optional
            DESCRIPTION. The default is {}.
        **kwargs : TYPE
            DESCRIPTION.

        Raises
        ------
        NetworkException
            DESCRIPTION.
        ApiException
            DESCRIPTION.

        Returns
        -------
        resp : TYPE
            DESCRIPTION.

        '''

        try:
            current_url = 'https://' + self.post_url + '/in.php'

            async with httpx.AsyncClient(follow_redirects=True) as client:
                if files:
                    async with AsyncExitStack() as stack:
                        file_objects = {}
                        for key, path in files.items():
                            file_handle = await stack.enter_async_context(aiofiles.open(path, 'rb'))
                            content = await file_handle.read()
                            file_objects[key] = content

                        resp = await client.post(current_url,
                                                 data=kwargs,
                                                 files=file_objects)

                elif 'file' in kwargs:
                    file_path = kwargs.pop('file')
                    async with aiofiles.open(file_path, 'rb') as file_handle:
                        content = await file_handle.read()
                        resp = await client.post(current_url,
                                                 data=kwargs,
                                                 files={'file': content})
                else:
                    resp = await client.post(current_url,
                                             data=kwargs)

        except httpx.RequestError as e:
            raise NetworkException(e)

        if resp.status_code != 200:
            raise NetworkException(f'bad response: {resp.status_code}')

        resp = resp.content.decode('utf-8')

        if 'ERROR' in resp:
            raise ApiException(resp)

        return resp

    async def res(self, **kwargs):
        '''
        sends additional GET-requests (solved captcha, balance, report etc.)

        Parameters
        ----------
        **kwargs : TYPE
            DESCRIPTION.

        Raises
        ------
        NetworkException
            DESCRIPTION.
        ApiException
            DESCRIPTION.

        Returns
        -------
        resp : TYPE
            DESCRIPTION.

        '''

        try:
            current_url_out = 'https://' + self.post_url + '/res.php'

            async with httpx.AsyncClient(follow_redirects=True) as client:
                resp = await client.get(current_url_out, params=kwargs)

                if resp.status_code != 200:
                    raise NetworkException(f'bad response: {resp.status_code}')

                resp = resp.content.decode('utf-8')

                if 'ERROR' in resp:
                    raise ApiException(resp)

        except httpx.RequestError as e:
            raise NetworkException(e)

        return resp
