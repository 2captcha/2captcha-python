import asyncio
import os
import sys
from base64 import b64encode

import aiofiles

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
    async with aiofiles.open('../images/canvas.jpg', 'rb') as f:
        b64 = b64encode(await f.read()).decode('utf-8')

    try:
        return await solver.canvas(b64, hintText='Draw around apple')
    except Exception as e:
        print(e)
        return e


if __name__ == '__main__':
    result = asyncio.run(solve_captcha())
    sys.exit('result: ' + str(result))
