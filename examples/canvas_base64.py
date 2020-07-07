import sys
import os
from base64 import b64encode

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

with open('./images/canvas.jpg', 'rb') as f:
    b64 = b64encode(f.read()).decode('utf-8')

try:
    result = solver.canvas(b64, hintText='Draw around apple')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
