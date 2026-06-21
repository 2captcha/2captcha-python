import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

config = {
            'server':           '2captcha.com', # can be also set to 'rucaptcha.com'
    		'apiKey':           api_key,
    		'softId':            123,
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = TwoCaptcha(**config)

try:
    result = solver.yidun(
        sitekey='6b4d7e0c4f5a4c7db2f3a1e8c9d6f123',
        pageurl='https://mysite.com/page/with/yidun',
        yidun_get_lib='https://cstaticdun.126.net/load.min.js',
        yidun_api_server_subdomain='c.dun.163.com',
        challenge='8f7e4d2c1b9a6f5e3d4c7b8a9e0f123456789abcdef123456789abcdef1234',
        hcg='9a217825f3dcfac3d34e551e93819d610dec931e5e2a2236edf0e1f3f320c191',
        hct=1751469954806,
        useragent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/148.0.0.0 Safari/537.36",
        # proxy={'type': 'HTTP',
        #        'uri': 'login:password@IP_address:PORT'}
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))