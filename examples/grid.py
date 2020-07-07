import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.grid('./images/grid_2.jpg',
                         hintText='Select all images with an Orange',
                         rows=3,
                         cols=3)

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
