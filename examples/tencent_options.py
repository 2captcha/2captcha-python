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
    result = solver.tencent(app_id="197325555",
                            url="https://your.site/result-receiver",
                            # proxy={
                            #     'type': 'HTTPS',
                            #     'uri': 'ub6900fef552505bc-zone-custom-session-JcIHpmDKv-sessTime-1:ub6900fef552505bc@43.152.113.55:2333'
                            # }
                            )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
