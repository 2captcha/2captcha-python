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
    result = solver.lemin(captcha_id='CROPPED_3dfdd5c_d1872b526b794d83ba3b365eb15a200b',
                                div_id='lemin-cropped-captcha', 
                                url='https://2captcha.com/demo/lemin')


except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
