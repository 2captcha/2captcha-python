import sys
import os
from base64 import b64encode

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

with open('../images/temu_main.png', 'rb') as f:
    body = b64encode(f.read()).decode('utf-8')
with open('../images/temu_part1.png', 'rb') as f:
    part1 = b64encode(f.read()).decode('utf-8')
with open('../images/temu_part2.png', 'rb') as f:
    part2 = b64encode(f.read()).decode('utf-8')
with open('../images/temu_part3.png', 'rb') as f:
    part3 = b64encode(f.read()).decode('utf-8')

try:
    result = solver.temu(body,
                         part1,
                         part2,
                         part3)

except Exception as e:
    sys.exit(str(e))

else:
    sys.exit('result: ' + str(result))
