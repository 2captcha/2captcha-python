# Python Module for 2Captcha API
The easiest way to quickly integrate [2Captcha] captcha solving service into your code to automate solving of any types of captcha.

- [Installation](#installation)
- [Configuration](#configuration)
- [Solve captcha](#solve-captcha)
  - [Normal Captcha](#normal-captcha)
  - [Text](#text-captcha)
  - [ReCaptcha v2](#recaptcha-v2)
  - [ReCaptcha v3](#recaptcha-v3)
  - [FunCaptcha](#funcaptcha)
  - [GeeTest](#geetest)
  - [hCaptcha](#hcaptcha)
  - [KeyCaptcha](#keycaptcha)
  - [Capy](#capy)
  - [Grid (ReCaptcha V2 Old Method)](#grid)
  - [Canvas](#canvas)
  - [ClickCaptcha](#clickcaptcha)
  - [Rotate](#rotate)
- [Other methods](#other-methods)
  - [send / getResult](#send--getresult)
  - [balance](#balance)
  - [report](#report)
- [Error handling](#error-handling)

## Installation

This package can be installed with Pip:

```pip3 install 2captcha-python```


## Configuration

TwoCaptcha instance can be created like this:

```python 
from twocaptcha import TwoCaptcha

solver = TwoCaptcha('YOUR_API_KEY')
```
Also there are few options that can be configured:

```python 
config = {
            'server':           '2captcha.com',
            'apiKey':           'YOUR_API_KEY',
            'softId':            123,
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)
```

### TwoCaptcha instance options

|Option|Default value|Description|
|---|---|---|
|server|`2captcha.com`|API server. You can set it to `rucaptcha.com` if your account is registered there|
|softId|-|your software ID obtained after publishing in [2captcha sofware catalog]|
|callback|-|URL of your web-sever that receives the captcha recognition result. The URl should be first registered in [pingback settings] of your account|
|defaultTimeout|120|Polling timeout in seconds for all captcha types except ReCaptcha. Defines how long the module tries to get the answer from `res.php` API endpoint|
|recaptchaTimeout|600|Polling timeout for ReCaptcha in seconds. Defines how long the module tries to get the answer from `res.php` API endpoint|
|pollingInterval|10|Interval in seconds between requests to `res.php` API endpoint, setting values less than 5 seconds is not recommended|

>  **IMPORTANT:** once `callback` is defined for `TwoCaptcha` instance, all methods return only the captcha ID and DO NOT poll the API to get the result. The result will be sent to the callback URL.
To get the answer manually use [getResult method](#send--getresult)

## Solve captcha
When you submit any image-based captcha use can provide additional options to help 2captcha workers to solve it properly.

### Captcha options
|Option|Default Value|Description|
|---|---|---|
|numeric|0|Defines if captcha contains numeric or other symbols [see more info in the API docs][post options]|
|minLength|0|minimal answer lenght|
|maxLength|0|maximum answer length|
|phrase|0|defines if the answer contains multiple words or not|
|caseSensitive|0|defines if the answer is case sensitive|
|calc|0|defines captcha requires calculation|
|lang|-|defines the captcha language, see the [list of supported languages] |
|hintImg|-|an image with hint shown to workers with the captcha|
|hintText|-|hint or task text shown to workers with the captcha|

Below you can find basic examples for every captcha type. Check out [examples directory] to find more examples with all available options.

### Normal Captcha
To bypass a normal captcha (distorted text on image) use the following method. This method also can be used to recognize any text on the image.
```python 
result = solver.normal('path/to/captcha.jpg', param1=..., ...)
# OR
result = solver.normal('https://site-with-captcha.com/path/to/captcha.jpg', param1=..., ...)
```

### Text Captcha
This method can be used to bypass a captcha that requires to answer a question provided in clear text.
```python 
result = solver.text('If tomorrow is Saturday, what day is today?', param1=..., ...)
```

### ReCaptcha v2
Use this method to solve ReCaptcha V2 and obtain a token to bypass the protection.
```python 
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                          url='https://mysite.com/page/with/recaptcha',
                          param1=..., ...)
```

### ReCaptcha v3
This method provides ReCaptcha V3 solver and returns a token.
```python
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/recaptcha',
                            version='v3',
                            param1=..., ...)
```

### FunCaptcha
FunCaptcha (Arkoselabs) solving method. Returns a token.
```python
result = solver.funcaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/funcaptcha',
                            param1=..., ...)

```


### GeeTest
Method to solve GeeTest puzzle captcha. Returns a set of tokens as JSON.
```python
result = solver.geetest(gt='f1ab2cdefa3456789012345b6c78d90e',
                        challenge='12345678abc90123d45678ef90123a456b',
                        url='https://www.site.com/page/',
                        param1=..., ...)

```


### hCaptcha
Use this method to solve hCaptcha challenge. Returns a token to bypass captcha.
```python
result = solver.hcaptcha(sitekey='10000000-ffff-ffff-ffff-000000000001',
                            url='https://www.site.com/page/', 
                            param1=..., ...)

```

### KeyCaptcha
Token-based method to solve KeyCaptcha.
```python
result = solver.keycaptcha(s_s_c_user_id=10,
    				   s_s_c_session_id='493e52c37c10c2bcdf4a00cbc9ccd1e8',
    				   s_s_c_web_server_sign='9006dc725760858e4c0715b835472f22-pz-',
    				   s_s_c_web_server_sign2='2ca3abe86d90c6142d5571db98af6714',
    				   url='https://www.keycaptcha.ru/demo-magnetic/', 
    				   param1=..., ...)

```

### Capy
Token-based method to bypass Capy puzzle captcha.
```python
result = solver.capy(sitekey='PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
                     url='http://mysite.com/',
                     api_server='https://jp.api.capy.me/',
                     param1=..., ...)
```
### Grid
Grid method is originally called Old ReCaptcha V2 method. The method can be used to bypass any type of captcha where you can apply a grid on image and need to click specific grid boxes. Returns numbers of boxes.
```python
result = solver.grid('path/to/captcha.jpg', param1=..., ...)
```
### Canvas
Canvas method can be used when you need to draw a line around an object on image. Returns a set of points' coordinates to draw a polygon.
```python
result = solver.canvas('path/to/captcha.jpg', param1=..., ...)
```
### ClickCaptcha
ClickCaptcha method returns coordinates of points on captcha image. Can be used if you need to click on particular points on the image.
```python
result = solver.coordinates('path/to/captcha.jpg', param1=..., ...)
```

### Rotate
This method can be used to solve a captcha that asks to rotate an object. Mostly used to bypass FunCaptcha. Returns the rotation angle.
```python
result = solver.rotate('path/to/captcha.jpg', param1=..., ...)
```

## Other methods

### send / getResult
These methods can be used for manual captcha submission and answer polling.
```python
import time
. . . . . 


id = solver.send(file='path/to/captcha.jpg')
time.sleep(20)

code = solver.get_result(id)
```

### balance
Use this method to get your account's balance
```python
balance = solver.balance()
```

### report
Use this method to report good or bad captcha answer.
```python
solver.report(id, True) # captcha solved correctly
solver.report(id, False) # captcha solved incorrectly
```

### Error handling
If case of an error captcha solver throws an exception. It's important to properly handle these cases. We recommend to use `try except` to handle exceptions. 
```python
Try:
    result = solver.text('If tomorrow is Saturday, what day is today?')
Except ValidationException as e:
    # invalid parameters passed
	print(e)
Except NetworkException as e:
	# network error occurred
	print(e)
Except ApiException as e:
    # api respond with error
	print(e)
Except TimeoutException as e:
    # captcha is not solved so far
	print(e)
```


### Proxies

You can pass your proxy as an additional argumen for methods: recaptcha, funcaptcha and geetest. The proxy will be forwarded to the API to solve the captcha.

```python
proxy={
    'type': 'HTTPS',
    'uri': 'login:password@IP_address:PORT'
}
```

### Async calls
You can also make async calls with [asyncio], for example:

```python
import asyncio
import concurrent.futures
from twocaptcha import TwoCaptcha

captcha_result = await captchaSolver(image)

async def captchaSolver(image):
    loop = asyncio.get_running_loop()
    with concurrent.future.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, lambda: TwoCaptcha(API_KEY).normal(image))
        return result
```


[2Captcha]: https://2captcha.com/
[2captcha sofware catalog]: https://2captcha.com/software
[pingback settings]: https://2captcha.com/setting/pingback
[post options]: https://2captcha.com/2captcha-api#normal_post
[list of supported languages]: https://2captcha.com/2captcha-api#language
[examples directory]: /examples
[asyncio]: https://docs.python.org/3/library/asyncio.html
