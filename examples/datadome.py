import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.datadome(
        captcha_url="https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAZirHgKBVrxwAsVuKlQ%3D%3D&cid=6UMFxKqnfKi2eFFrE1qXfCKp63PJZG8paEmhrdvBTCjLMsxEBnwN1ll6DMj3zgknV12vVMEGIGlz_PwXqp3KInLKNssKELeGAiA30KzBLiZkbsANFUppr57BQ~_~zqk7&referer=https%3A%2F%2Fdd.burak.fr%2F&hash=47C8DCE2BC1F24F1810FD12D144E2A&t=fe&s=39587&e=bec7a70727d6522cc2763179059323aa7d2faac7420c5da690fffd096a893c12",
        pageurl="https://dd.burak.fr/",
        userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        proxy={
            'type': 'HTTP',
            'uri': 'login:password@IP_address:PORT'
        }
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))