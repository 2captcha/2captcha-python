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
    		# 'callback':         'https://your.site/result-receiver', # if set, sovler with just return captchaId, not polling API for the answer
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = TwoCaptcha(**config)

try:
    result = solver.turnstile(sitekey='0x4AAAAAAAVrOwQWPlm3Bnr5',
                              url='https://2captcha.com/demo/turnstile',
                              # data="str",
                              # pagedata="str",
                              # action="str",
                              # useragent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
                              # proxy={
                              #     'type': 'HTTPS',
                              #     'uri': 'login:password@IP_address:PORT'
                              # }
                            )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
