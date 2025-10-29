import sys
import os
import requests
from base64 import b64encode
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

with open('../images/vk.jpg', 'rb') as f:
    b64 = b64encode(f.read()).decode('utf-8')

try:
    result = solver.vkimage(files=b64,
                            steps='[5,4,7,7,14,22,8,3,2,7,23,22,2,8,24,5,9,20,2,5,0,6,22,4,5,11,12,12,9,6,18,3,21,18,17,'
                                  '7,6,1,4,19,8,11,3,14,20,6,16,11,23,0,10,14,10,9,24,3,14,14,10,0,15,10,6,6,20,12,18,13,'
                                  '20,7,13,9,22,14,24,14,17,22,0,4,6,11,10,15,18,20,0,3,6,4,23,12,15,14,18,4,2,9,5,2]',
                            )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
