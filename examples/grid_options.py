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

solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=12)

try:
    result = solver.grid(
        file='./images/grid_2.jpg',
        rows=3,
        cols=3,
        previousId=0,
        canSkip=0,
        lang='en',
        hintImg='./images/grid_hint.jpg',
        # hintText='Select all images with an Orange',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
