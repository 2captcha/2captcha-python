#!/usr/bin/env python3

import asyncio
import os
import sys
import time
from base64 import b64encode

import aiofiles
import httpx

try:
    from .async_api import AsyncApiClient
    from .exceptions.solver import ValidationException, NetworkException, TimeoutException, ApiException, \
        SolverExceptions
except ImportError:
    from async_api import AsyncApiClient
    from twocaptcha.exceptions.solver import ValidationException, NetworkException, TimeoutException, ApiException, \
        SolverExceptions


class AsyncTwoCaptcha():
    def __init__(self,
                 apiKey,
                 softId=4580,
                 callback=None,
                 defaultTimeout=120,
                 recaptchaTimeout=600,
                 pollingInterval=10,
                 server='2captcha.com',
                 extendedResponse=None):

        self.API_KEY = apiKey
        self.soft_id = softId
        self.callback = callback
        self.default_timeout = defaultTimeout
        self.recaptcha_timeout = recaptchaTimeout
        self.polling_interval = pollingInterval
        self.api_client = AsyncApiClient(post_url=str(server))
        self.max_files = 9
        self.exceptions = SolverExceptions
        self.extendedResponse = extendedResponse

    async def normal(self, file, **kwargs):
        '''Wrapper for solving a normal captcha (image).

        Parameters
        __________
        file : file
            Captcha image file. * required if you submit image as a file (method=post).
        body : str
            Base64-encoded captcha image. * required if you submit image as Base64-encoded string (method=base64).
        phrase : int, optional
            0 - captcha contains one word. 1 - captcha contains two or more words.
            Default: 0.
        numeric : int, optional
            0 - not specified. 1 - captcha contains only numbers. 2 - captcha contains only letters. 3 - captcha
            contains only numbers OR only letters. 4 - captcha MUST contain both numbers AND letters.
            Default: 0
        minLen : int, optional
            0 - not specified. 1..20 - minimal number of symbols in captcha.
            Default: 0.
        maxLen : int, optional
            0 - not specified. 1..20 - maximal number of symbols in captcha.
            Default: 0.
        caseSensitive : int, optional
            0 - captcha in not case sensitive. 1 - captcha is case sensitive.
            Default: 0.
        calc : int, optional
            0 - not specified. 1 - captcha requires calculation (e.g. type the result 4 + 8 = ).
            Default: 0.
        lang : str, optional
            Language code. See the list of supported languages https://2captcha.com/2captcha-api#language.
        hintText : str, optional
            Max 140 characters. Endcoding: UTF-8. Text will be shown to worker to help him to solve the captcha correctly.
            For example: type red symbols only.
        hintImg : img, optional
            Max 400x150px, 100 kB. Image with instruction for solving reCAPTCHA. Not required if you're sending
            instruction as text with textinstructions.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        '''

        method = await self.get_method(file)
        result = await self.solve(**method, **kwargs)
        return result

    async def audio(self, file, lang, **kwargs):
        '''Wrapper for solving audio captcha.

        Parameters
        __________
        body : str
            Base64 encoded audio file in mp3 format. Max file size: 1 MB.
        lang : str
          The language of audio record. Supported languages are: "en", "ru", "de", "el", "pt", "fr".
        '''

        method = "audio"

        if not file:
            raise ValidationException('File is none')
        elif not '.' in file and len(file) > 50:
            body = file
        elif file.endswith(".mp3") and file.startswith("http"):
            async with httpx.AsyncClient(follow_redirects=True) as client:
                response = await client.get(file)
                if response.status_code != 200:
                    raise ValidationException(f'File could not be downloaded from url: {file}')
                body = b64encode(response.content).decode('utf-8')
        elif file.endswith(".mp3"):
            async with aiofiles.open(file, "rb") as media:
                file_content = await media.read()
                body = b64encode(file_content).decode('utf-8')
        else:
            raise ValidationException('File extension is not .mp3 or it is not a base64 string.')

        if not lang or lang not in ("en", "ru", "de", "el", "pt", "fr"):
            raise ValidationException(f'Lang not in "en", "ru", "de", "el", "pt", "fr". You send {lang}')

        result = await self.solve(body=body, method=method, lang=lang, **kwargs)
        return result

    async def text(self, text, **kwargs):
        '''Wrapper for solving text captcha.

        Parameters
        __________
        text : str
            Max 140 characters. Endcoding: UTF-8. Text will be shown to worker to help him to solve the captcha correctly.
            For example: type red symbols only.
        lang: str, optional
            Language code. See the list of supported languages https://2captcha.com/2captcha-api#language.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        '''

        result = await self.solve(text=text, method='post', **kwargs)
        return result

    async def recaptcha(self, sitekey, url, version='v2', enterprise=0, **kwargs):
        '''Wrapper for solving recaptcha (v2, v3).

        Parameters
        _______________
        sitekey : str
            Value of sitekey parameter you found on page.
        url : str
            Full URL of the page where you see the reCAPTCHA.
        domain : str, optional
            Domain used to load the captcha: google.com or recaptcha.net. Default: google.com.
        invisible : int, optional
            1 - means that reCAPTCHA is invisible. 0 - normal reCAPTCHA. Default: 0.
        version : str, optional
            v3 — defines that you're sending a reCAPTCHA V3. Default: v2.
        enterprise : str, optional
            1 - defines that you're sending reCAPTCHA Enterpise. Default: 0.
        action : str, optional
            Value of action parameter you found on page. Default: verify.
        score : str, only for v3, optional
            The score needed for resolution. Currently, it's almost impossible to get token with score higher than 0.3.
            Default: 0.4.
        data-s : str, only for v2, optional
            Value of data-s parameter you found on page. Curenttly applicable for Google Search and other Google services.
        cookies : str, only for v2, optional
            Your cookies that will be passed to our worker who solve the captha. We also return worker's cookies in the
            response if you use json=1. Format: KEY:Value, separator: semicolon, example: KEY1:Value1;KEY2:Value2;
        userAgent : str, only for v2, optional
            Your userAgent that will be passed to our worker and used to solve the captcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        params = {
            'googlekey': sitekey,
            'url': url,
            'method': 'userrecaptcha',
            'version': version,
            'enterprise': enterprise,
            **kwargs,
        }

        result = await self.solve(timeout=self.recaptcha_timeout, **params)
        return result

    async def funcaptcha(self, sitekey, url, **kwargs):
        '''Wrapper for solving funcaptcha.

        Parameters
        __________
        sitekey : str
            Value of pk or data-pkey parameter you found on page.
        url : str
            Full URL of the page where you see the FunCaptcha.
        surl : str, optional
            Value of surl parameter you found on page.
        userAgent: str, optional
            Tells us to use your user-agent value.
        data[key] : str, optional
            Custom data to pass to FunCaptcha. For example: data[blob]=stringValue.
        softId : str, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(publickey=sitekey,
                                  url=url,
                                  method='funcaptcha',
                                  **kwargs)
        return result

    async def geetest(self, gt, challenge, url, **kwargs):
        '''Wrapper for solving geetest captcha.

        Parameters:
        __________
        gt : str
            Value of gt parameter you found on target website.
        challenge : str
            Value of challenge parameter you found on target website.
        url : str
            Full URL of the page where you see Geetest captcha.
        offline : num, optional
            In rare cases initGeetest can be called with offline parameter. If the call uses offline: true, set the
            value to 1. Default: 0.
        new_captcha : num, optional
            In rare cases initGeetest can be called with new_captcha parameter. If the call uses new_captcha: true, set
            the value to 1. Mostly used with offline parameter.
        userAgent : str, optional
            Your userAgent that will be passed to our worker and used to solve the captcha.
        apiServer : str, optional
            Value of api_server parameter you found on target website.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(gt=gt,
                                  challenge=challenge,
                                  url=url,
                                  method='geetest',
                                  **kwargs)
        return result

    async def hcaptcha(self, sitekey, url, **kwargs):
        '''Wrapper for solving hcaptcha.

        Parameters
        __________
        sitekey : str
            Value of data-sitekey parameter you found on page.
        url : str
            Full URL of the page where you bypass the captcha.
        invisible : num, optional
            Use 1 for invisible version of hcaptcha. Currently it is a very rare case.
            Default: 0.
        data : str, optional
            Custom data that is used in some implementations of hCaptcha, mostly with invisible=1. In most cases you see
            it as rqdata inside network requests. Format: "data": "rqDataValue".
        domain : str, optional
            Domain used to load the captcha: hcaptcha.com or js.hcaptcha.com. Default: hcaptcha.com.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(sitekey=sitekey,
                                  url=url,
                                  method='hcaptcha',
                                  **kwargs)
        return result

    async def keycaptcha(self, s_s_c_user_id, s_s_c_session_id,
                         s_s_c_web_server_sign, s_s_c_web_server_sign2, url,
                         **kwargs):
        '''Wrapper for solving.

        Parameters
        __________
        s_s_c_user_id : str
            Value of s_s_c_user_id parameter you found on page.
        s_s_c_session_id : str
            Value of s_s_c_session_id parameter you found on page.
        s_s_c_web_server_sign : str
            Value of s_s_c_web_server_sign parameter you found on page.
        s_s_c_web_server_sign2 : str
            Value of s_s_c_web_server_sign2 parameter you found on page.
        url : str
            Full URL of the page where you see the KeyCaptcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
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

        result = await self.solve(**params)
        return result

    async def capy(self, sitekey, url, **kwargs):
        '''Wrapper for solving capy.

        Parameters
        __________
        sitekey : str
            The domain part of script URL you found on page. Default value: https://jp.api.capy.me/.
        url : str
            Full URL of the page where you see the captcha.
        api_server : str, optional
            The domain part of script URL you found on page. Default value: https://jp.api.capy.me/.
        version : str, optional
            The version of captcha task: "puzzle" (assemble a puzzle) or "avatar" (drag an object). Default: puzzle.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(captchakey=sitekey,
                                  url=url,
                                  method='capy',
                                  **kwargs)
        return result

    async def grid(self, file, **kwargs):
        '''Wrapper for solving grid captcha (image).

        Required:
        file : file
            Captcha image file. * required if you submit image as a file (method=post).
        body : str
            Base64-encoded captcha image. * required if you submit image as Base64-encoded string (method=base64).
        hintText : str
            Max 140 characters. Endcoding: UTF-8. Text with instruction for solving reCAPTCHA. For example: select images
            with trees. Not required if you're sending instruction as an image with imginstructions.
        hintImg : img
            Max 400x150px, 100 kB. Image with instruction for solving reCAPTCHA. Not required if you're sending
            instruction as text with textinstructions.
        rows : int, optional
            Number of rows in reCAPTCHA grid.
        cols : itn, optional
            Number of columns in reCAPTCHA grid.
        previousId : str, optional
            Id of your previous request with the same captcha challenge.
        canSkip : int, optional
            0 - not specified. 1 - possibly there's no images that fit the instruction. Set the value to 1 only if it's
            possible that there's no images matching to the instruction. We'll provide a button "No matching images" to
            worker, and you will receive No_matching_images as answer.
            Default: 0.
        lang: str, optional
            Language code. See the list of supported languages https://2captcha.com/2captcha-api#language.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        method = await self.get_method(file)

        params = {
            'recaptcha': 1,
            **method,
            **kwargs,
        }

        result = await self.solve(**params)
        return result

    async def canvas(self, file, **kwargs):
        '''Wrapper for solving canvas captcha (image).

        Parameters
        __________
        file : file
            Captcha image file. * required if you submit image as a file (method=post).
        body : str
            Base64-encoded captcha image. * required if you submit image as Base64-encoded string (method=base64).
        hintText : str
            Max 140 characters. Endcoding: UTF-8. Text with instruction for solving reCAPTCHA. For example: select
            images with trees. Not required if you're sending instruction as an image with imginstructions.
        hintImg : img
            Max 400x150px, 100 kB. Image with instruction for solving reCAPTCHA. Not required if you're sending
            instruction as text with textinstructions.
        canSkip : int, optional
            0 - not specified. 1 - possibly there's no images that fit the instruction. Set the value to 1 only if it's
            possible that there's no images matching to the instruction. We'll provide a button "No matching images" to
            worker, and you will receive No_matching_images as answer.
            Default: 0.
        lang : int, optional
            0 - not specified. 1 - Cyrillic captcha. 2 - Latin captcha.
            Default: 0.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        '''

        if not ('hintText' in kwargs or 'hintImg' in kwargs):
            raise ValidationException(
                'parameters required: hintText and/or hintImg')

        method = await self.get_method(file)

        params = {
            'recaptcha': 1,
            'canvas': 1,
            **method,
            **kwargs,
        }

        result = await self.solve(**params)
        return result

    async def coordinates(self, file, **kwargs):
        '''Wrapper for solving coordinates captcha (image).

        Parameters
        __________
        file : file
            Captcha image file. * required if you submit image as a file (method=post).
        body : str
            Base64-encoded captcha image. * required if you submit image as Base64-encoded string (method=base64).
        hintText : str
            Max 140 characters. Endcoding: UTF-8. Text with instruction for solving the captcha. For example: click on
            images with ghosts. Not required if the image already contains the instruction.
        hintImg : img
             Max 400x150px, 100 kB. Image with instruction for solving reCAPTCHA. Not required if you're sending
             instruction as text with textinstructions.
        lang : str, optional
            Language code. See the list of supported languages https://2captcha.com/2captcha-api#language.
        min_clicks : int, optional
            The minimum number of clicks that need to be done.
        max_clicks : int, optional
            The maximum number of clicks that can be done.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        '''

        method = await self.get_method(file)

        params = {
            'coordinatescaptcha': 1,
            **method,
            **kwargs,
        }

        result = await self.solve(**params)
        return result

    async def rotate(self, files, **kwargs):
        '''Wrapper for solving rotate captcha (image).

        Parameters
        __________
        files : file
            Captcha image file. * required if you submit image as a file (method=post).
        body : str
            Base64-encoded captcha image. * required if you submit image as Base64-encoded string (method=base64).
        angle : int, optional
            Angle for one rotation step in degrees. If not defined we'll use the default value for FunCaptcha: 40 degrees.
            Default: 40.
        lang : str, optional
            Language code. See the list of supported languages https://2captcha.com/2captcha-api#language.
        hintImg : str, optional
            Image with instruction for worker to help him to solve captcha correctly.
        hintText : str, optional
            Text will be shown to worker to help him to to solve captcha correctly.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        if isinstance(files, str):
            file = await self.get_method(files)
            file = file.get('file')

            result = await self.solve(file=file, method='rotatecaptcha', **kwargs)
            return result

        elif isinstance(files, dict):
            files = list(files.values())

        files = self.extract_files(files)

        result = await self.solve(files=files, method='rotatecaptcha', **kwargs)
        return result

    async def geetest_v4(self, captcha_id, url, **kwargs):
        '''Wrapper for solving geetest_v4 captcha.

        Parameters
        __________
        captcha_id : str
            Value of captcha_id parameter you found on target website.
        url: str
            Full URL of the page where you see Geetest captcha.
        risk_type: str, optional
            Value of risk_type parameter is contained in the captcha loading request.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(captcha_id=captcha_id,
                                  url=url,
                                  method='geetest_v4',
                                  **kwargs)
        return result

    async def lemin(self, captcha_id, div_id, url, **kwargs):
        '''Wrapper for solving Lemin Cropped Captcha.

        Parameters
        __________
        captcha_id : str
            Value of captcha_id parameter you found on page.
        div_id : str
            The id of captcha parent div element.
        url : str
            Full URL of the page where you see the captcha.
        api_server : str, optional
            The domain part of script URL you found on page. Default value: https://api.leminnow.com/.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(captcha_id=captcha_id,
                                  div_id=div_id,
                                  url=url,
                                  method='lemin',
                                  **kwargs)
        return result

    async def atb_captcha(self, app_id, api_server, url, **kwargs):
        '''Wrapper for solving atbCAPTCHA.

        Parameters
        __________
        app_id : str
            The value of appId parameter in the website source code.
        api_server : str
            The value of apiServer parameter in the website source code.
        url : str
            The full URL of target web page where the captcha is loaded. We do not open the page, not a problem if it is
            available only for authenticated users.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.

        '''

        result = await self.solve(app_id=app_id,
                                  api_server=api_server,
                                  url=url,
                                  method='atb_captcha',
                                  **kwargs)
        return result

    async def turnstile(self, sitekey, url, **kwargs):
        '''Wrapper for solving Cloudflare Turnstile.

        Parameters
        __________
        sitekey : str
            Value of sitekey parameter you found on page.
        url : str
            Full URL of the page where you see the captcha.
        useragent : str
            User-Agent of your browser. Must match the User-Agent you use to access the site.
            Use only modern browsers released within the last 6 months.
        action : str. optional
            Value of optional action parameter you found on page, can be defined in data-action attribute or passed
            to turnstile.render call.
        data : str, optional
            The value of cData passed to turnstile.render call. Also can be defined in data-cdata attribute.
        pagedata : str, optional
            The value of the chlPageData parameter when calling turnstile.render.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(sitekey=sitekey,
                                  url=url,
                                  method='turnstile',
                                  **kwargs)
        return result

    async def amazon_waf(self, sitekey, iv, context, url, **kwargs):
        '''Wrapper for solving Amazon WAF.

        Parameters
        __________
        sitekey : str
            Value of key parameter you found on the page.
        iv : str
            Value of iv parameter you found on the page.
        context : str
            Value of optional context parameter you found on page.
        url : str
            Full URL of the page where you see the captcha.
        challenge_script : str, optional
            The source URL of challenge.js script on the page.
        captcha_script : str, optional
            The source URL of captcha.js script on the page.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(sitekey=sitekey,
                                  iv=iv,
                                  context=context,
                                  url=url,
                                  method='amazon_waf',
                                  **kwargs)

        return result

    async def mtcaptcha(self, sitekey, url, **kwargs):
        '''Wrapper for solving MTCaptcha.

        Parameters
        __________
        sitekey : str
            The value of sitekey parameter found on the page.
        url : str
            Full URL of the page where you solve the captcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(sitekey=sitekey,
                                  url=url,
                                  method='mt_captcha',
                                  **kwargs)
        return result

    async def friendly_captcha(self, sitekey, url, **kwargs):
        '''Wrapper for solving Friendly Captcha.

        Parameters
        __________
        sitekey : str
            The value of data-sitekey attribute of captcha's div element on page.
        url : str
            Full URL of the page where you solve the captcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(sitekey=sitekey,
                                  url=url,
                                  method='friendly_captcha',
                                  **kwargs)
        return result

    async def tencent(self, app_id, url, **kwargs):
        '''Wrapper for solving Tencent captcha.

        Parameters
        __________
        app_id : str
            The value of appId parameter in the website source code.
        url : str
            The full URL of target web page where the captcha is loaded. We do not open the page, not a problem if it is
            available only for authenticated users.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(app_id=app_id,
                                  url=url,
                                  method="tencent",
                                  **kwargs)
        return result

    async def cutcaptcha(self, misery_key, apikey, url, **kwargs):
        '''Wrapper for solving Friendly Captcha.

        Parameters
        __________
        misery_key : str
            The value of CUTCAPTCHA_MISERY_KEY variable defined on page.
        apikey : str
            The value of data-apikey attribute of iframe's body. Also, the name of javascript file included on the page.
        url : str
            Full URL of the page where you solve the captcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        result = await self.solve(misery_key=misery_key,
                                  api_key=apikey,
                                  url=url,
                                  method='cutcaptcha',
                                  **kwargs)
        return result

    async def vkimage(self, files, steps, **kwargs):
        '''Wrapper for solving vkimage captcha.

        Parameters
        __________
        file : str
            Captcha image as a file or base64.
        steps: str
            Array of steps.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''

        if isinstance(files, str):

            payload = await self.get_method(files)
            payload.pop('method', None)

            result = await self.solve(method='vkimage', steps=steps, **payload, **kwargs)
            return result

        elif isinstance(files, dict):
            files = list(files.values())

        files = self.extract_files(files)

        result = await self.solve(method='vkimage',
                            files=files,
                            steps=steps,
                            **kwargs)
        return result

    async def vkcaptcha(self, redirect_uri, userAgent, proxy, **kwargs):
        '''Wrapper for solving VK captcha using tokens.

        Parameters
        __________
        redirect_uri : str
            The URL that is returned for requests to the captchas API.
        userAgent : str
            User-Agent of the browser that will be used by the employee when loading the captcha.
        proxy : dict
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''


        result = await self.solve(method='vkcaptcha',
                            redirect_uri=redirect_uri,
                            useragent=userAgent,
                            proxy=proxy,
                            **kwargs)
        return result

    async def captchafox(self, sitekey, pageurl, userAgent, proxy, **kwargs):
        '''Wrapper for solving CaptchaFox using tokens.

        Parameters
        __________
        sitekey : str
            The sitekey parameter value found on the page or in network requests.
        pageurl : str
            Full URL of the page with captcha.
        userAgent : str
            User-Agent of the browser that will be used by the employee when loading the captcha.
        proxy : dict
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''


        result = await self.solve(method='captchafox',
                            sitekey=sitekey,
                            pageurl=pageurl,
                            useragent=userAgent,
                            proxy=proxy,
                            **kwargs)
        return result

    async def prosopo(self, sitekey, pageurl, **kwargs):
        '''Wrapper for solving Prosopo captcha using tokens.

        Parameters
        __________
        sitekey : str
            The sitekey parameter value found on the page or in network requests.
        pageurl : str
            Full URL of the page with captcha.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''


        result = await self.solve(method='prosopo',
                            sitekey=sitekey,
                            pageurl=pageurl,
                            **kwargs)
        return result

    async def temu(self, body, part1, part2, part3, **kwargs):
        '''Wrapper for solving Temu captcha .

        Parameters
        __________
        body : str
            Main captcha image as a base64 string.
        part1 : str
            Tile element as a base64 string.
        part2 : str
            Tile element as a base64 string.
        part3 : str
            Tile element as a base64 string.
        '''

        result = await self.solve(method='temuimage',
                            body=body,
                            part1=part1,
                            part2=part2,
                            part3=part3,
                            **kwargs)
        return result

    async def datadome(self, captcha_url, pageurl, userAgent, proxy, **kwargs):
        """Wrapper for solving DataDome Captcha.

        Parameters
        __________
        captcha_url: str
            The value of the 'src' parameter for the 'iframe' element containing the captcha on the page.
        pageurl: str
            Full URL of the page that triggers the captcha when you go to it.
        userAgent: str
            User-Agent of the browser that will be used by the employee when loading the captcha.
        proxy : dict
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        """

        result = await self.solve(method='datadome',
                                  captcha_url=captcha_url,
                                  pageurl=pageurl,
                                  userAgent=userAgent,
                                  proxy=proxy,
                                  **kwargs)
        return result

    async def cybersiara(self, master_url_id, pageurl, userAgent, **kwargs):
        '''Wrapper for solving CyberSiARA captcha.

        Parameters
        __________
        master_url_id : str
            The value of the MasterUrlId parameter from the request to API/CyberSiara/GetCyberSiara.
        pageurl : str
            Full URL of the page with captcha.
        userAgent : str
            User-Agent of your browser.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        '''
        result = await self.solve(method='cybersiara',
                                  master_url_id=master_url_id,
                                  pageurl=pageurl,
                                  userAgent=userAgent,
                                  **kwargs)
        return result

    async def yandex_smart(self, sitekey, url, **kwargs):
        '''Wrapper for solving Yandex Smart.

        Parameters
        __________
        sitekey : str
            The value of data-sitekey attribute of captcha's div element on page.
        url : str
            Full URL of the page where you solve the captcha.
        softId : int, optional
            ID of software developer. Developers who integrated their software with 2Captcha get reward: 10% of
            spendings of their software users.
        callback : str, optional
            URL for pingback (callback) response that will be sent when captcha is solved. URL should be registered on
            the server. More info here https://2captcha.com/2captcha-api#pingback.
        proxy : dict, optional
            {'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'}.
        userAgent: str, optional
            User-Agent of the browser that will be used by the employee when loading the captcha.
        '''

        result = await self.solve(sitekey=sitekey,
                                  url=url,
                                  method='yandex',
                                  **kwargs)
        return result

    async def solve(self, timeout=0, polling_interval=0, **kwargs):
        '''Sends captcha, receives result.

        Parameters
        __________
        timeout : float

        polling_interval : int

        **kwargs : dict
            all captcha params

        Returns

        result : string
        '''

        id_ = await self.send(**kwargs)
        result = {'captchaId': id_}

        if self.callback is None:
            timeout = float(timeout or self.default_timeout)
            sleep = int(polling_interval or self.polling_interval)

            code = await self.wait_result(id_, timeout, sleep)

            if self.extendedResponse == True:
                new_code = {
                    key if key != 'request' else 'code': value
                    for key, value in code.items()
                    if key != 'status'
                }
                result.update(new_code)
            else:
                result.update({'code': code})

            return result

    async def wait_result(self, id_, timeout, polling_interval):
        max_wait = time.time() + timeout

        while time.time() < max_wait:
            try:
                return await self.get_result(id_)
            except NetworkException:
                await asyncio.sleep(polling_interval)

        raise TimeoutException(f'timeout {timeout} exceeded')

    async def get_method(self, file):
        if not file:
            raise ValidationException('File required')

        if not '.' in file and len(file) > 50:
            return {'method': 'base64', 'body': file}

        if file.startswith('http'):
            async with httpx.AsyncClient(follow_redirects=True) as client:
                img_resp = await client.get(file)
                if img_resp.status_code != 200:
                    raise ValidationException(f'File could not be downloaded from url: {file}')
                return {'method': 'base64', 'body': b64encode(img_resp.content).decode('utf-8')}

        if not os.path.exists(file):
            raise ValidationException(f'File not found: {file}')

        return {'method': 'post', 'file': file}

    async def send(self, **kwargs):
        """This method can be used for manual captcha submission

        Parameters
        _________
        method : str
            The name of the method must be found in the documentation https://2captcha.com/2captcha-api
        kwargs: dict
            All captcha params
        Returns

        """
        params = self.default_params(kwargs)
        params = self.rename_params(params)

        params, files = self.check_hint_img(params)

        response = await self.api_client.in_(files=files, **params)

        if not response.startswith('OK|'):
            raise ApiException(f'cannot recognize response {response}')

        return response[3:]

    async def get_result(self, id_):
        import json
        """This method can be used for manual captcha answer polling.

        Parameters
        __________
        id_ : str
            ID of the captcha sent for solution
        Returns

        answer : text
        """
        if self.extendedResponse == True:
            response = await self.api_client.res(key=self.API_KEY, action='get', id=id_, json=1)
            response_data = json.loads(response)

            if response_data.get("status") == 0:
                raise NetworkException

            if not response_data.get("status") == 1:
                raise ApiException(f'Unexpected status in response: {response_data}')

            return response_data
        else:
            response = await self.api_client.res(key=self.API_KEY, action='get', id=id_)

            if response == 'CAPCHA_NOT_READY':
                raise NetworkException

            if not response.startswith('OK|'):
                raise ApiException(f'cannot recognize response {response}')

            return response[3:]

    async def balance(self):
        '''Get my balance

        Returns

        balance : float
        '''
        response = await self.api_client.res(key=self.API_KEY, action='getbalance')
        return float(response)

    async def report(self, id_, correct):
        '''Report of solved captcha: good/bad.

        Parameters
        __________
        id_ : str
            captcha ID

        correct : bool
            True/False

        Returns
            None.

        '''
        rep = 'reportgood' if correct else 'reportbad'
        await self.api_client.res(key=self.API_KEY, action=rep, id=id_)
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

        files = {f'file_{e + 1}': f for e, f in enumerate(files)}
        return files

    def check_hint_img(self, params):
        hint = params.pop('imginstructions', None)
        files = params.pop('files', {})

        if not hint:
            return params, files

        if not '.' in hint and len(hint) > 50:
            params.update({'imginstructions': hint})
            return params, files

        if not os.path.exists(hint):
            raise ValidationException(f'File not found: {hint}')

        if not files:
            files = {'file': params.pop('file', {})}

        files.update({'imginstructions': hint})

        return params, files


if __name__ == '__main__':
    async def main():
        key = sys.argv[1]
        sol = AsyncTwoCaptcha(key)


    asyncio.run(main())
