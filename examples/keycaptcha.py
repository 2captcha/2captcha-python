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
!!!!
try:
    result = solver.keycaptcha(
        s_s_c_user_id=15,
        s_s_c_session_id='faa8cc1697c962ad4b859aa472f5d992',
        s_s_c_web_server_sign='4f84e4fe41cf688d8d94361489ecd75c-pz-',
        s_s_c_web_server_sign2='a9af97bb0a645eec495f2527e431a21b',
        url='https://www.keycaptcha.com/products/')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
