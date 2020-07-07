import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
        url='https://mysite.com/page/with/recaptcha',
        invisible=1,
        action='verify',
        proxy={
            'type': 'HTTPS',
            'uri': 'login:password@IP_address:PORT'
        })

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
