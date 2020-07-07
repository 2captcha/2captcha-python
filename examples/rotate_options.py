import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=10)

try:
    result = solver.rotate(
        ['images/rotate.jpg', 'images/rotate_2.jpg', 'images/rotate_3.jpg'],
        angle=40,
        lang='en',
        # hintImg  = 'images/rotate_hint.jpg'
        hintText='Put the images in the correct way up')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
