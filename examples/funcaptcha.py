import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.funcaptcha(sitekey='69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC',
                               url='https://mysite.com/page/with/funcaptcha',
                               surl='https://client-api.arkoselabs.com')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
