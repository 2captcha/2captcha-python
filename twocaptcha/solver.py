#!/usr/bin/env python3

import os, sys
import time
import requests
from base64 import b64encode


try:
    from .api import ApiClient

except ImportError:
    from api import ApiClient


class SolverExceptions(Exception):
    pass


class ValidationException(SolverExceptions):
    pass


class NetworkException(SolverExceptions):
    pass


class ApiException(SolverExceptions):
    pass


class TimeoutException(SolverExceptions):
    pass


class TwoCaptcha():
    def __init__(self,
                 apiKey,
                 softId=None,
                 callback=None,
                 defaultTimeout=120,
                 recaptchaTimeout=600,
                 pollingInterval=10,
                 server = '2captcha.com'):

        self.API_KEY = apiKey
        self.soft_id = softId
        self.callback = callback
        self.default_timeout = defaultTimeout
        self.recaptcha_timeout = recaptchaTimeout
        self.polling_interval = pollingInterval
        self.api_client = ApiClient(post_url = str(server))
        self.max_files = 9
        self.exceptions = SolverExceptions

    def normal(self, file, **kwargs):
        '''
        Wrapper for solving normal captcha (image)
        
        Required:
            file                (image, base64, or url)

        Optional params:

            phrase
            numeric
            minLen 
            maxLen 
            phrase 
            caseSensitive
            calc   
            lang
            hintText
            hintImg
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        method = self.get_method(file)
        result = self.solve(**method, **kwargs)
        return result

    def audio(self, file, lang, **kwargs):
        '''
        Wrapper for solving audio captcha
        
        Required:
            file (base64, or url to mp3 file)
            lang ("en", "ru", "de", "el", "pt")

        Optional params:
        '''
        method = "audio"

        if not file:
            raise ValidationException('File is none')
        elif not '.' in file and len(file) > 50:
            body = file
        elif file.endswith(".mp3") and file.startswith("http"):
            response = requests.get(file)
            if response.status_code != 200:
                raise ValidationException(f'File could not be downloaded from url: {file}')
            body = b64encode(response.content).decode('utf-8')
        elif file.endswith(".mp3"):
            with open(file, "rb") as media:
                body = b64encode(media.read()).decode('utf-8')                
        else:
            raise ValidationException('File extension is not .mp3 or it is not a base64 string.')

        if not lang or lang not in ("en", "ru", "de", "el", "pt"):
            raise ValidationException(f'Lang not in "en", "ru", "de", "el", "pt". You send {lang}')

        result = self.solve(body=body, method=method, **kwargs)
        return result

    def text(self, text, **kwargs):
        '''
        Wrapper for solving text captcha 

        Required:
            text
            
        Optional params:
            
            lang
            softId
            callback
        '''

        result = self.solve(text=text, method='post', **kwargs)
        return result

    def recaptcha(self, sitekey, url, version='v2', enterprise=0, **kwargs):
        '''
        Wrapper for solving recaptcha (v2, v3)

        Required:
            sitekey
            url

        Optional params:
            
            invisible
            version
            enterprise
            action
            score
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        params = {
            'googlekey': sitekey,
            'url': url,
            'method': 'userrecaptcha',
            'version': version,
            'enterprise': enterprise,
            **kwargs,
        }

        result = self.solve(timeout=self.recaptcha_timeout, **params)
        return result

    def funcaptcha(self, sitekey, url, **kwargs):
        '''
        Wrapper for solving funcaptcha

        Required:
            sitekey
            url

        Optional params:
            
            surl
            userAgent
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
            **{'data[key]': 'anyStringValue'}
        '''

        result = self.solve(publickey=sitekey,
                            url=url,
                            method='funcaptcha',
                            **kwargs)
        return result

    def geetest(self, gt, challenge, url, **kwargs):
        '''
        Wrapper for solving geetest captcha

        Required:
            gt
            challenge
            url
                        
        Optional params:
            
            apiServer
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        result = self.solve(gt=gt,
                            challenge=challenge,
                            url=url,
                            method='geetest',
                            **kwargs)
        return result

    def hcaptcha(self, sitekey, url, **kwargs):
        '''
        Wrapper for solving hcaptcha

        Required:
            sitekey
            url

        Optional params:

            invisible
            data
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        result = self.solve(sitekey=sitekey,
                            url=url,
                            method='hcaptcha',
                            **kwargs)
        return result

    def keycaptcha(self, s_s_c_user_id, s_s_c_session_id,
                   s_s_c_web_server_sign, s_s_c_web_server_sign2, url,
                   **kwargs):
        '''
        Wrapper for solving 

        Required:
            s_s_c_user_id
            s_s_c_session_id
            s_s_c_web_server_sign
            s_s_c_web_server_sign2
            url

        Optional params:
            
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        params = {
            's_s_c_user_id': s_s_c_user_id,
            's_s_c_session_id': s_s_c_session_id,
            's_s_c_web_server_sign': s_s_c_web_server_sign,
            's_s_c_web_server_sign2': s_s_c_web_server_sign2,
            'url': url,
            'method': 'keycaptcha',
            **kwargs,
        }

        result = self.solve(**params)
        return result

    def capy(self, sitekey, url, **kwargs):
        '''
        Wrapper for solving capy

        Required:
            sitekey
            url

        Optional params:
            
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        result = self.solve(captchakey=sitekey,
                            url=url,
                            method='capy',
                            **kwargs)
        return result

    def grid(self, file, **kwargs):
        '''
        Wrapper for solving grid captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            rows      
            cols      
            previousId
            canSkip   
            lang      
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        method = self.get_method(file)

        params = {
            'recaptcha': 1,
            **method,
            **kwargs,
        }

        result = self.solve(**params)
        return result

    def canvas(self, file, **kwargs):
        '''
        Wrapper for solving canvas captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            previousId
            canSkip   
            lang      
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        if not ('hintText' in kwargs or 'hintImg' in kwargs):
            raise ValidationException(
                'parameters required: hintText and/or hintImg')

        method = self.get_method(file)

        params = {
            'recaptcha': 1,
            'canvas': 1,
            **method,
            **kwargs,
        }

        result = self.solve(**params)
        return result

    def coordinates(self, file, **kwargs):
        '''
        Wrapper for solving coordinates captcha (image)
        
        Required:
            file                (image or base64)

        Optional params:
            
            hintImg   
            hintText  
            lang
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        method = self.get_method(file)

        params = {
            'coordinatescaptcha': 1,
            **method,
            **kwargs,
        }

        result = self.solve(**params)
        return result

    def rotate(self, files, **kwargs):
        '''
        Wrapper for solving rotate captcha (image)
        
        Required:
            files               (images)

        Optional params:
            
            angle
            lang
            hintImg   
            hintText  
            softId
            callback
            proxy           =  {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'})
        '''

        if isinstance(files, str):

            file = self.get_method(files)['file']

            result = self.solve(file=file, method='rotatecaptcha', **kwargs)
            return result

        elif isinstance(files, dict):
            files = list(files.values())

        files = self.extract_files(files)

        result = self.solve(files=files, method='rotatecaptcha', **kwargs)
        return result
    

    def geetest_v4(self, captcha_id, url, **kwargs):
        '''
        Wrapper for solving geetest_v4 captcha

        Required:
            captcha_id
            url
                        
        Optional params:
            

        '''

        result = self.solve(captcha_id=captcha_id,
                            url=url,
                            method='geetest_v4',
                            **kwargs)
        return result
    

    def lemin(self, captcha_id, div_id, url, **kwargs):
        '''
        Wrapper for solving Lemin Cropped Captcha

        Required:
            captcha_id
            div_id
            url
                        
        Optional params:
            

        '''

        result = self.solve(captcha_id=captcha_id,
                            div_id=div_id,
                            url=url,
                            method='lemin',
                            **kwargs)
        return result
    

    def turnstile(self, sitekey, url, **kwargs):
        '''
        Wrapper for solving Cloudflare Turnstile

        Required:
            sitekey
            url
                        
        Optional params:
            action
            data

        '''

        result = self.solve(sitekey=sitekey,
                            url=url,
                            method='turnstile',
                            **kwargs)
        return result
    

    def amazon_waf(self, sitekey, iv, context, url, **kwargs):
        '''
        Wrapper for solving Amazon WAF

        Required:
            sitekey
            iv
            context
            url
                        
        Optional params:

        '''

        result = self.solve(sitekey=sitekey,
                            iv=iv, 
                            context=context,
                            url=url,
                            method='amazon_waf',
                            **kwargs)
        
        return result



    def solve(self, timeout=0, polling_interval=0, **kwargs):
        '''
        sends captcha, receives result


        Parameters
        ----------
        timeout : float
        polling_interval : int

        **kwargs : all captcha params

        Returns
        -------
        result : string
        '''

        id_ = self.send(**kwargs)
        result = {'captchaId': id_}

        if self.callback is None:

            timeout = float(timeout or self.default_timeout)
            sleep = int(polling_interval or self.polling_interval)

            code = self.wait_result(id_, timeout, sleep)
            result.update({'code': code})

        return result

    def wait_result(self, id_, timeout, polling_interval):

        max_wait = time.time() + timeout

        while time.time() < max_wait:

            try:
                return self.get_result(id_)

            except NetworkException:

                time.sleep(polling_interval)

        raise TimeoutException(f'timeout {timeout} exceeded')

    def get_method(self, file):

        if not file:
            raise ValidationException('File required')

        if not '.' in file and len(file) > 50:
            return {'method': 'base64', 'body': file}

        if file.startswith('http'):
            img_resp = requests.get(file)
            if img_resp.status_code != 200:
                raise ValidationException(f'File could not be downloaded from url: {file}')
            return {'method': 'base64', 'body': b64encode(img_resp.content).decode('utf-8')}

        if not os.path.exists(file):
            raise ValidationException(f'File not found: {file}')

        return {'method': 'post', 'file': file}

    def send(self, **kwargs):

        params = self.default_params(kwargs)
        params = self.rename_params(params)

        params, files = self.check_hint_img(params)

        response = self.api_client.in_(files=files, **params)

        if not response.startswith('OK|'):
            raise ApiException(f'cannot recognize response {response}')

        return response[3:]

    def get_result(self, id_):

        response = self.api_client.res(key=self.API_KEY, action='get', id=id_)

        if response == 'CAPCHA_NOT_READY':
            raise NetworkException

        if not response.startswith('OK|'):
            raise ApiException(f'cannot recognize response {response}')

        return response[3:]

    def balance(self):
        '''
        get my balance

        Returns
        -------
        balance : float

        '''

        response = self.api_client.res(key=self.API_KEY, action='getbalance')
        return float(response)

    def report(self, id_, correct):
        '''
        report of solved captcha: good/bad

        Parameters
        ----------
        id_ : captcha ID
        correct : True/False

        Returns
        -------
        None.

        '''

        rep = 'reportgood' if correct else 'reportbad'
        self.api_client.res(key=self.API_KEY, action=rep, id=id_)

        return

    def rename_params(self, params):

        replace = {
            'caseSensitive': 'regsense',
            'minLen': 'min_len',
            'maxLen': 'max_len',
            'minLength': 'min_len',
            'maxLength': 'max_len',
            'hintText': 'textinstructions',
            'hintImg': 'imginstructions',
            'url': 'pageurl',
            'score': 'min_score',
            'text': 'textcaptcha',
            'rows': 'recaptcharows',
            'cols': 'recaptchacols',
            'previousId': 'previousID',
            'canSkip': 'can_no_answer',
            'apiServer': 'api_server',
            'softId': 'soft_id',
            'callback': 'pingback',
            'datas': 'data-s',
        }

        new_params = {
            v: params.pop(k)
            for k, v in replace.items() if k in params
        }

        proxy = params.pop('proxy', '')
        proxy and new_params.update({
            'proxy': proxy['uri'],
            'proxytype': proxy['type']
        })

        new_params.update(params)

        return new_params

    def default_params(self, params):

        params.update({'key': self.API_KEY})

        callback = params.pop('callback', self.callback)
        soft_id = params.pop('softId', self.soft_id)

        if callback: params.update({'callback': callback})
        if soft_id: params.update({'softId': soft_id})

        self.has_callback = bool(callback)

        return params

    def extract_files(self, files):

        if len(files) > self.max_files:
            raise ValidationException(
                f'Too many files (max: {self.max_files})')

        not_exists = [f for f in files if not (os.path.exists(f))]

        if not_exists:
            raise ValidationException(f'File not found: {not_exists}')

        files = {f'file_{e+1}': f for e, f in enumerate(files)}
        return files

    def check_hint_img(self, params):

        hint = params.pop('imginstructions', None)
        files = params.pop('files', {})

        if not hint:
            return params, files

        if not '.' in hint and len(hint) > 50:
            return params, files

        if not os.path.exists(hint):
            raise ValidationException(f'File not found: {hint}')

        if not files:
            files = {'file': params.pop('file', {})}

        files.update({'imginstructions': hint})

        return params, files


if __name__ == '__main__':

    key = sys.argv[1]
    sol = TwoCaptcha(key)
