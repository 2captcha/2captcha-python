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
    result = solver.alibaba(
        pageurl='https://www.example.com',
        scene_id='abc123xyz4',
        prefix='dlw3kug',
        user_id='Abc123Def456Ghi789Jkl012Mno345Pqr678Stu901=',
        user_user_id='Xyz987Abc654Def321Ghi098Jkl765Mno432Pqr109=',
        verify_type='1.0',
        region='sgp',
        user_certify_id='abc123def456ghi789jkl012mno345pq',
        api_get_lib='https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041',
        useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        # proxy={'type': 'HTTP',
        #        'uri': 'login:password@IP_address:PORT'}
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
