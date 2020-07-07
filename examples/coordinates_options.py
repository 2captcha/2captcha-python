import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=120, pollingInterval=5)

try:
    result = solver.coordinates('./images/grid_2.jpg',
                                lang='en',
                                hintImg='./images/grid_hint.jpg',
                                hintText='Select all images with an Orange')
except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
