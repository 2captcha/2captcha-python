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

solver = TwoCaptcha(api_key)

try:
    result = solver.tspd(
        pageurl='https://example.com/login',
        tspd_cookie='TS386a400d029=082670...010245; TS386a400d078=082670...dbb3b0c',
        html_page_base64='PCFET0NUWVBFIGh0bWw+...',
        proxy={'type': 'HTTP', 'uri': 'login:password@IP_address:PORT'},
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
