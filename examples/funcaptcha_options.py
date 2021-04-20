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

solver = TwoCaptcha(api_key, defaultTimeout=180, pollingInterval=15)

try:
    result = solver.funcaptcha(
        sitekey='FB18D9DB-BAFF-DDAC-A33B-6CF22267BC0A',
        url='https://mysite.com/page/with/funcaptcha',
        surl='https://client-api.arkoselabs.com',
        userAgent=
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        **{'data[key]': 'value'},  #optional data param used by some websites
        proxy={
            'type': 'HTTP',
            'uri': 'login:password@123.123.123.123:8080'
        })

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
