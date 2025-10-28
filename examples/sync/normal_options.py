import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=30, pollingInterval=5)

try:
    result = solver.normal(
        '../images/normal_2.jpg',
        numeric=4,
        minLen=4,
        maxLen=20,
        phrase=0,
        caseSensitive=0,
        calc=0,
        lang='en',
        # hintImg='../images/normal_hint.jpg',
        # hintText='Type red symbols only',
    )

except Exception as e:
    sys.exit(str(e))

else:
    sys.exit('result: ' + str(result))
