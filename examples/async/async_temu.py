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
    # Read file and convert to base64
    with open('../images/temu_main.png', 'rb') as f:
        body = b64encode(f.read()).decode('utf-8')
    with open('../images/temu_part1.png', 'rb') as f:
        part1 = b64encode(f.read()).decode('utf-8')
    with open('../images/temu_part2.png', 'rb') as f:
        part2 = b64encode(f.read()).decode('utf-8')
    with open('../images/temu_part3.png', 'rb') as f:
        part3 = b64encode(f.read()).decode('utf-8')

    try:
        return await solver.temu(
            body,
            part1,
            part2,
            part3
        )
    except Exception as e:
        sys.exit(e)


if __name__ == '__main__':
    result = asyncio.run(solve_captcha())
    sys.exit('result: ' + str(result))
