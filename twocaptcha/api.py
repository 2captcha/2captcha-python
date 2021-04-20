#!/usr/bin/env python3

import requests


class NetworkException(Exception):
    pass


class ApiException(Exception):
    pass


class ApiClient():
    def __init__(self, post_url = '2captcha.com'):
        self.post_url = post_url
        
        
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
            current_url = 'https://'+self.post_url+'/in.php'
            if files:

                files = {key: open(path, 'rb') for key, path in files.items()}
                resp = requests.post(current_url,
                                     data=kwargs,
                                     files=files)

                [f.close() for f in files.values()]

            elif 'file' in kwargs:

                with open(kwargs.pop('file'), 'rb') as f:
                    resp = requests.post(current_url,
                                         data=kwargs,
                                         files={'file': f})

            else:
                resp = requests.post(current_url,
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
            current_url_out = 'https://'+self.post_url+'/res.php'
            resp = requests.get(current_url_out, params=kwargs)

            if resp.status_code != 200:
                raise NetworkException(f'bad response: {resp.status_code}')

            resp = resp.content.decode('utf-8')

            if 'ERROR' in resp:
                raise ApiException(resp)

        except requests.RequestException as e:
            raise NetworkException(e)

        return resp
