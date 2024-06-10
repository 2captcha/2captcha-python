import sys
import os
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

"""
Important: the value of the 'challenge' parameter is dynamic, for each request to our API you need to get a new value.
"""

resp = requests.get("https://2captcha.com/api/v1/captcha-demo/gee-test/init-params")
challenge = resp.json()['challenge']

try:
    result = solver.geetest(gt='81388ea1fc187e0c335c0a8907ff2625',
                            apiServer='http://api.geetest.com',
                            challenge=challenge,
                            url='https://2captcha.com/demo/geetest')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))