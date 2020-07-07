import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=30, pollingInterval=5)

try:
    result = solver.normal(
        './images/normal_2.jpg',
        numeric=4,
        minLen=4,
        maxLen=20,
        phrase=0,
        caseSensitive=0,
        calc=0,
        lang='en',
        # hintImg='./images/normal_hint.jpg',
        # hintText='Type red symbols only',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
