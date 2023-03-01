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

solver = TwoCaptcha(api_key)

try:
    result = solver.amazon_waf(
        sitekey='AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AFsClhVgr5q0UFRdXhhHEwiAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLMbH8d6uQSrYTraoAgEQgDvtSNxdEyG7Zu393cHyPdWNCZgeIB52+W7fCTI8U5z15z1NdPUdnB1ZHoK7ewpwoSMm5mzkJJld0cnvGw==',
        iv='CgAAYDJb9CAAACAq',
        context='wCho9T9OcETTT8fu1k6+rszr5aGt4eLd+K3mHpV8VbSkjAWJGJx/iQ16RKDCTQBtU5OSeE+SQqoS5iTzhgGtvwgmBbr7X/I+aXaNfb2JRZ8eJ7CnQpM9QRwnv7vGgrGRBGhkh/jaVYmXdy0j0x21s3dCBlA4VN3naDHIweZqkyhXqJBNI1Ep8OMSnhXtPebboB117aBW4IU4XEOii8EE1G4Z7ndWhrNVVXYYwVoxfnSqfYX//CJir6dZfLMbCt5t7NnO8yjsx/YHGVXFVBt2Zrj0ZTxowoYbHU/BKyFaXgUj+ZQ=',
        url='https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
