import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=180, pollingInterval=15)

try:
    result = solver.funcaptcha(
        sitekey='FB18D9DB-BAFF-DDAC-A33B-6CF22267BC0A',
        url='https://mysite.com/page/with/funcaptcha',
        surl='https://client-api.arkoselabs.com',
        userAgent=
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        **{'data[key]': 'value'},  #optional data param used by some websites
        proxy={
            'type': 'HTTP',
            'uri': 'login:password@123.123.123.123:8080'
        })

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
