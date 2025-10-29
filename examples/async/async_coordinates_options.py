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

solver = AsyncTwoCaptcha(api_key, defaultTimeout=120, pollingInterval=5, extendedResponse=True)


async def solve_captcha():
    try:
        return await solver.coordinates('../images/grid_2.jpg',
                                        lang='en',
                                        hintImg='../images/grid_hint.jpg',
                                        hintText='Select all images with an Orange',
                                        min_clicks=2,
                                        max_clicks=3)
    except Exception as e:
        sys.exit(e)


if __name__ == '__main__':
    result = asyncio.run(solve_captcha())
    sys.exit('result: ' + str(result))
