import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

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
            'extendedResponse': True
	    }

solver = TwoCaptcha(**config)

try:
    result = solver.vkcaptcha(redirect_uri='https://id.vk.ru/not_robot_captcha?domain=vk.com&session_token=eyJhbGciOiJBMjU2R0NN....',
                              userAgent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4348.100 Yandex/23.6.1.1107 Yowser/2.5 Safari/537.36',
                              proxy={'type': 'HTTPS',
                                     'uri': 'login:password@IP_address:PORT'}
                              )


except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
