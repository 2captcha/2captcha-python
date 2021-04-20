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

resp = requests.get("https://www.mysite.com/distil_r_captcha_challenge")
challenge = resp.content.decode('utf-8').split(';')[0]

try:
    result = solver.geetest(gt='f3bf6dbdcf7886856696502e1d55e00c',
                            apiServer='api-na.geetest.com',
                            challenge=challenge,
                            url='https://www.mysite.com/distil_r_captcha.html')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
