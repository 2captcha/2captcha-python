import sys
import os
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=300, pollingInterval=10)

resp = requests.get("https://www.mysite.com/distil_r_captcha_challenge")
challenge = resp.content.decode('utf-8').split(';')[0]

try:
    result = solver.geetest(
        gt='f3bf6dbdcf7886856696502e1d55e00c',
        apiServer='api-na.geetest.com',
        challenge=challenge,
        url='https://www.mysite.com/distil_r_captcha.html',
        #  proxy={
        #      'type': 'HTTPS',
        #      'uri': 'login:password@IP_address:PORT'
        #  }
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
