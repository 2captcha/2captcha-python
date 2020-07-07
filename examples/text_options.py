import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=40, pollingInterval=10)

try:
    result = solver.text('If tomorrow is Saturday, what day is today?',
                         lang='en')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
