import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.datadome(
        captcha_url="https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAZirHgKBVrxwAsVuKlQ%3D%3D&c...",
        pageurl="https://mysite.com/page/with/datadome",
        userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        proxy={
            'type': 'HTTP',
            'uri': 'login:password@IP_address:PORT'
        }
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))