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
    		# 'callback':         'https://your.site/result-receiver', # if set, sovler with just return captchaId, not polling API for the answer
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }

solver = TwoCaptcha(**config)

"""
Important: the values of the 'iv' and 'context' parameters are dynamic, for every request to our API you need to get new values. 
The values 'iv' and 'context' need to be looked for in the page code.
"""

try:
    result = solver.amazon_waf(sitekey='AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AGIqvS8v6ScFa8ZpNRrlQgKAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMx9gxoe10Zg35PWhzAgEQgDvUtMMkqkFQByMLK2329D8iX4mjvaTuUhU70LD4vLp54v3+4K1nYY2hB+OM1hMbncnMbP63y4UOrY77jg==',
                               iv='CgAGVTNd9JAAAAnB',
                               context='Lte3LdSjiAN6nNcV0omaNt/ydFmd/eTwRCxYEeuW97LZe3IbAXWi4Er9CWQ3HbDgJ0KSpDgwyoskjKCK4VRQzYufPCdrfCYCveZCt9pMNoAluEtj0oix2GXOPVkw2d4bYOg3MtY5ZUHLR3L467NEInnRE99w5NOgokH5Ie7eOi5sYAqYtZrHABGEgrdAOVvU7bcwvrCERi9wB/WS75geb3oFy6z7Apue9GFa86Ld20jjgy4LWfaen+2fpfKHmCHTKVWfto17Bg+l5i0sr+uFRzpk1We64Fhh1Wl1NHF6M6dpS5s=',
                               url='https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest',
                               challenge_script="https://41bcdd4fb3cb.610cd090.us-east-1.token.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/challenge.js",
                               captcha_script="https://41bcdd4fb3cb.610cd090.us-east-1.captcha.awswaf.com/41bcdd4fb3cb/0d21de737ccb/cd77baa6c832/captcha.js",
                               callback="https://mysite.com/2captcha.txt"
                               # proxy={
                               #     'type': 'HTTPS',
                               #     'uri': 'login:password@IP_address:PORT'
                               # }
                            )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
