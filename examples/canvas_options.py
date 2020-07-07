import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=120, pollingInterval=5)

try:
    result = solver.canvas(
        './images/canvas.jpg',
        previousId=0,
        canSkip=0,
        lang='en',
        hintImg='./images/canvas_hint.jpg',
        hintText='Draw around apple',
        #    callback='http://127.0.0.1/test/'
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('sent: ' + str(result))
