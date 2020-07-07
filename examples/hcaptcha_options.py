import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=300, pollingInterval=10)

try:
    result = solver.hcaptcha(sitekey='10000000-ffff-ffff-ffff-000000000001',
                             url='https://www.site.com/page/',
                             proxy={
                                 'type': 'HTTPS',
                                 'uri': 'login:password@IP_address:PORT'
                             })

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
