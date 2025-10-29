import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from twocaptcha import AsyncTwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

config = {
            'server':           '2captcha.com', # can be also set to 'rucaptcha.com'
    		'apiKey':           api_key,
    		'softId':            123,
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = AsyncTwoCaptcha(**config)

async def solve_captcha():
    try:
        return await solver.captchafox(
            sitekey='sk_ILKWNruBBVKDOM7dZs59KHnDLEWiH',
            pageurl='https://mysite.com/page/with/captchafox',
            userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            proxy={'type': 'HTTPS',
                   'uri': 'login:password@IP_address:PORT'}
        )
    except Exception as e:
        sys.exit(e)

if __name__ == '__main__':
    result = asyncio.run(solve_captcha())
    sys.exit('result: ' + str(result))