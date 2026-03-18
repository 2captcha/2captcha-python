import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from twocaptcha import AsyncTwoCaptcha

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_2CAPTCHA=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = AsyncTwoCaptcha(api_key)

async def solve_captcha():
    try:
        return await solver.altcha(
            pageurl='https://mysite.com/page/with/altcha',
            challenge_json='{"algorithm":"SHA-256","challenge":"a4c9d8e7f1b23a6c...",..."signature":"7b3e2a9d5c8f1046e2d91c3a..."}',
            # challenge_url='https://example/altcha',
        )
    except Exception as e:
        sys.exit(e)

if __name__ == '__main__':
    result = asyncio.run(solve_captcha())
    sys.exit('result: ' + str(result))