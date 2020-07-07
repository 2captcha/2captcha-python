#!/usr/bin/env python3

import requests


class NetworkException(Exception):
    pass


class ApiException(Exception):
    pass


class ApiClient():
    def in_(self, files={}, **kwargs):
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
            if files:

                files = {key: open(path, 'rb') for key, path in files.items()}
                resp = requests.post('https://2captcha.com/in.php',
                                     data=kwargs,
                                     files=files)

                [f.close() for f in files.values()]

            elif 'file' in kwargs:

                with open(kwargs.pop('file'), 'rb') as f:
                    resp = requests.post('https://2captcha.com/in.php',
                                         data=kwargs,
                                         files={'file': f})

            else:
                resp = requests.post('https://2captcha.com/in.php',
                                     data=kwargs)

        except requests.RequestException as e:
            raise NetworkException(e)

        if resp.status_code != 200:
            raise NetworkException(f'bad response: {resp.status_code}')

        resp = resp.content.decode('utf-8')

        if 'ERROR' in resp:
            raise ApiException(resp)

        return resp

    def res(self, **kwargs):
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
            resp = requests.get('https://2captcha.com/res.php', params=kwargs)

            if resp.status_code != 200:
                raise NetworkException(f'bad response: {resp.status_code}')

            resp = resp.content.decode('utf-8')

            if 'ERROR' in resp:
                raise ApiException(resp)

        except requests.RequestException as e:
            raise NetworkException(e)

        return resp
