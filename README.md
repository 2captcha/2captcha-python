<a href="https://github.com/2captcha/2captcha-python"><img src="https://github.com/user-attachments/assets/a737d428-5233-4605-9d09-211fa213d069" width="82" height="30"></a>
<a href="https://github.com/2captcha/2captcha-javascript"><img src="https://github.com/user-attachments/assets/4d3b4541-34b2-4ed2-a687-d694ce67e5a6" width="36" height="30"></a>
<a href="https://github.com/2captcha/2captcha-go"><img src="https://github.com/user-attachments/assets/ab22182e-6cb2-41fa-91f4-d5e89c6d7c6f" width="63" height="30"></a>
<a href="https://github.com/2captcha/2captcha-ruby"><img src="https://github.com/user-attachments/assets/0270d56f-79b0-4c95-9b09-4de89579914b" width="75" height="30"></a>
<a href="https://github.com/2captcha/2captcha-cpp"><img src="https://github.com/user-attachments/assets/36de8512-acfd-44fb-bb1f-b7c793a3f926" width="45" height="30"></a>
<a href="https://github.com/2captcha/2captcha-php"><img src="https://github.com/user-attachments/assets/e8797843-3f61-4fa9-a155-ab0b21fb3858" width="52" height="30"></a>
<a href="https://github.com/2captcha/2captcha-java"><img src="https://github.com/user-attachments/assets/a3d923f6-4fec-4c07-ac50-e20da6370911" width="50" height="30"></a>
<a href="https://github.com/2captcha/2captcha-csharp"><img src="https://github.com/user-attachments/assets/f4d449de-780b-49ed-bb0a-b70c82ec4b32" width="38" height="30"></a>

# Python Module for 2Captcha API (captcha solver)

The easiest way to quickly integrate the [2Captcha] captcha-solving service into your code and automate the solving of any type of captcha.
Examples of API requests for different captcha types are available on the [Python captcha solver](https://2captcha.com/lang/python) page.

- [Python Module for 2Captcha API (captcha solver)](#python-module-for-2captcha-api-captcha-solver)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [TwoCaptcha instance options](#twocaptcha-instance-options)
  - [Solve captcha](#solve-captcha)
    - [Captcha options](#captcha-options)
    - [Normal Captcha](#normal-captcha)
    - [Audio Captcha](#audio-captcha)
    - [Text Captcha](#text-captcha)
    - [reCAPTCHA v2](#recaptcha-v2)
    - [reCAPTCHA v3](#recaptcha-v3)
    - [FunCaptcha](#funcaptcha)
    - [GeeTest](#geetest)
    - [GeeTest v4](#geetest-v4)
    - [Yandex Smart](#yandex-smart)
    - [Lemin Cropped Captcha](#lemin-cropped-captcha)
    - [Cloudflare Turnstile](#cloudflare-turnstile)
    - [Amazon WAF](#amazon-waf)
    - [KeyCaptcha](#keycaptcha)
    - [atbCAPTCHA](#atbcaptcha)
    - [Capy](#capy)
    - [Grid](#grid)
    - [Canvas](#canvas)
    - [ClickCaptcha](#clickcaptcha)
    - [Rotate](#rotate)
    - [MTCaptcha](#mtcaptcha)
    - [Friendly Captcha](#friendly-captcha)
    - [Cutcaptcha](#cutcaptcha)
    - [Tencent](#tencent)
    - [DataDome](#datadome)
    - [CyberSiARA](#cybersiara)
  - [Other methods](#other-methods)
    - [send / get\_result](#send--get_result)
    - [balance](#balance)
    - [report](#report)
  - [Error handling](#error-handling)
  - [Proxies](#proxies)
  - [Async calls](#async-calls)
  - [Examples](#examples)
  - [Examples using Selenium](#examples-using-selenium)
  - [Useful articles](#useful-articles)
  - [Get in touch](#get-in-touch)
  - [Join the team 👪](#join-the-team-)
  - [License](#license)
    - [Graphics and Trademarks](#graphics-and-trademarks)

## Installation

This package can be installed with Pip:

```bash
pip3 install 2captcha-python
```


## Configuration

TwoCaptcha instance can be created like this:

```python 
from twocaptcha import TwoCaptcha

solver = TwoCaptcha('YOUR_API_KEY')
```
Also, there are a few options that can be configured:

```python 
config = {
            'server':           '2captcha.com',
            'apiKey':           'YOUR_API_KEY',
            'softId':            123,
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
            'extendedResponse':  False
        }
solver = TwoCaptcha(**config)
```

### TwoCaptcha instance options

| Option           | Default value  | Description                                                                                                                                            |
| ---------------- | -------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------|
| server           | `2captcha.com` | API server. You can set it to `rucaptcha.com` if your account is registered there                                                                      |
| softId           | 4580           | your software ID obtained after publishing in [2captcha software catalog]                                                                              |
| callback         | -              | URL of your web server that receives the captcha recognition result. The URL should be first registered in [pingback settings] of your account         |
| defaultTimeout   | 120            | Polling timeout in seconds for all captcha types except reCAPTCHA. Defines how long the module tries to get the answer from the `res.php` API endpoint |
| recaptchaTimeout | 600            | Polling timeout for reCAPTCHA in seconds. Defines how long the module tries to get the answer from the `res.php` API endpoint                          |
| pollingInterval  | 10             | Interval in seconds between requests to the `res.php` API endpoint. Setting values less than 5 seconds is not recommended                              |
| extendedResponse | None           | Set to `True` to get the response with additional fields or in more practical format (enables `JSON` response from `res.php` API endpoint). Suitable for [ClickCaptcha](#clickcaptcha), [Canvas](#canvas) |


> [!IMPORTANT]
> Once `callback` is defined for the `TwoCaptcha` instance, all methods return only the captcha ID and DO NOT poll the API to get the result. The result will be sent to the callback URL.

To get the answer manually use [get_result method](#send--get_result)

## Solve captcha
When you submit any image-based CAPTCHA, you can provide additional options to help 2captcha workers solve it properly.

### Captcha options
| Option        | Default Value | Description                                                                                        |
| ------------- | ------------- | -------------------------------------------------------------------------------------------------- |
| numeric       | 0             | Defines if the captcha contains numeric or other symbols [see more info in the API docs][post options] |
| minLen        | 0             | minimal answer length                                                                              |
| maxLen        | 0             | maximum answer length                                                                              |
| phrase        | 0             | defines if the answer contains multiple words or not                                               |
| caseSensitive | 0             | defines if the answer is case sensitive                                                            |
| calc          | 0             | defines captcha requires calculation                                                               |
| lang          | -             | defines the captcha language; see the [list of supported languages]                                |
| hintImg       | -             | an image with a hint shown to workers with the captcha                                               |
| hintText      | -             | hint or task text shown to workers with the captcha                                                |

Below, you can find basic examples for every captcha type. Check out [examples directory] for more examples with all available options.

### Normal Captcha

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_normal_captcha)</sup>

To bypass a normal captcha (distorted text on an image) use the following method. This method can also be used to recognize any text in an image.

```python 
result = solver.normal('path/to/captcha.jpg', param1=..., ...)
# OR
result = solver.normal('https://site-with-captcha.com/path/to/captcha.jpg', param1=..., ...)
```

### Audio Captcha

<sup>[API method description.](https://2captcha.com/2captcha-api#audio)</sup>

Use the following method to bypass an audio captcha (mp3 formats only). 
You must provide the language as `lang = 'en'`. Supported languages are "en", "ru", "de", "el", "pt", "fr".

```python 
result = solver.audio('path/to/captcha.mp3', lang = 'lang', param1=..., ...)
# OR
result = solver.audio('https://site-with-captcha.com/path/to/captcha.mp3', lang = 'lang', param1=..., ...)
```

### Text Captcha

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_text_captcha)</sup>

This method can be used to bypass a captcha that requires answering a question provided in clear text.
```python 
result = solver.text('If tomorrow is Saturday, what day is today?', param1=..., ...)
```

### reCAPTCHA v2

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_recaptchav2_new)</sup>

Use the following method to solve reCAPTCHA V2 and obtain a token to bypass the protection.

```python 
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                          url='https://mysite.com/page/with/recaptcha',
                          param1=..., ...)
```

### reCAPTCHA v3

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_recaptchav3)</sup>

This method provides a reCAPTCHA V3 solver and returns a token.
```python
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/recaptcha',
                            version='v3',
                            param1=..., ...)
```

### FunCaptcha

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_funcaptcha_new)</sup>

FunCaptcha (Arkoselabs) solving method. Returns a token.
```python
result = solver.funcaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/funcaptcha',
                            param1=..., ...)

```


### GeeTest

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_geetest)</sup>

Method to solve GeeTest puzzle captcha. Returns a set of tokens as JSON.
```python
result = solver.geetest(gt='f1ab2cdefa3456789012345b6c78d90e',
                        challenge='12345678abc90123d45678ef90123a456b',
                        url='https://www.site.com/page/',
                        param1=..., ...)

```


### GeeTest v4

<sup>[API method description.](https://2captcha.com/2captcha-api#geetest-v4)</sup>

Use this method to solve GeeTest v4. Returns the response in JSON.
```python
result = solver.geetest_v4(captcha_id='e392e1d7fd421dc63325744d5a2b9c73',
                            url='https://www.site.com/page/',  
                            param1=..., ...)

```


### Lemin Cropped Captcha

<sup>[API method description.](https://2captcha.com/2captcha-api#lemin)</sup>

Use this method to solve the Lemin captcha. Returns JSON with an answer containing the following values: answer, challenge_id.
```python
result = solver.lemin(captcha_id='CROPPED_1abcd2f_a1234b567c890d12ef3a456bc78d901d',
                            div_id='lemin-cropped-captcha', 
                            url='https://www.site.com/page/',
                            param1=..., ...)

```

### Yandex Smart

Use this method to solve Yandex Smart Captcha. Returns JSON with the token.
```python
result = solver.yandex_smart(sitekey='0x1AAAAh45AAAAkg0s2VIOD34y5hy4h4h',
               url='http://mysite.com/', 
               proxy={'type': 'HTTPS', 'uri': 'login:password@IP_address:PORT'},
               userAgent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
```

### Cloudflare Turnstile

<sup>[API method description.](https://2captcha.com/2captcha-api#turnstile)</sup>

Use this method to solve Cloudflare Turnstile. Returns JSON with the token.
```python
result = solver.turnstile(sitekey='0x1AAAAAAAAkg0s2VIOD34y5',
                            url='http://mysite.com/', 
                            data='foo',
                            pagedata='bar',
                            action='challenge',
                            useragent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
```

### Amazon WAF

<sup>[API method description.](https://2captcha.com/2captcha-api#amazon-waf)</sup>

Use this method to solve Amazon WAF Captcha also known as AWS WAF Captcha is a part of Intelligent threat mitigation for Amazon AWS. Returns JSON with the token.
```python
result = solver.amazon_waf(sitekey='0x1AAAAAAAAkg0s2VIOD34y5',
                            iv='CgAHbCe2GgAAAAAj', 
                            context='9BUgmlm48F92WUoqv97a49ZuEJJ50TCk9MVr3C7WMtQ0X6flVbufM4n8mjFLmbLVAPgaQ1Jydeaja94iAS49ljb+sUNLoukWedAQZKrlY4RdbOOzvcFqmD/ZepQFS9N5w15Exr4VwnVq+HIxTsDJwRviElWCdzKDebN/mk8/eX2n7qJi5G3Riq0tdQw9+C4diFZU5E97RSeahejOAAJTDqduqW6uLw9NsjJBkDRBlRjxjn5CaMMo5pYOxYbGrM8Un1JH5DMOLeXbq1xWbC17YSEoM1cRFfTgOoc+VpCe36Ai9Kc='
                            url='https://non-existent-example.execute-api.us-east-1.amazonaws.com/latest'
                            param1=..., ...)

```


### KeyCaptcha

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_keycaptcha)</sup>

Token-based method to solve KeyCaptcha.
```python
result = solver.keycaptcha(s_s_c_user_id=10,
    				   s_s_c_session_id='493e52c37c10c2bcdf4a00cbc9ccd1e8',
    				   s_s_c_web_server_sign='9006dc725760858e4c0715b835472f22-pz-',
    				   s_s_c_web_server_sign2='2ca3abe86d90c6142d5571db98af6714',
    				   url='https://www.keycaptcha.ru/demo-magnetic/', 
    				   param1=..., ...)

```


### atbCAPTCHA

<sup>[API method description.](https://2captcha.com/2captcha-api#atb-captcha)</sup>

Use this method to solve atbCaptcha challenge. Returns a token to bypass the captcha.
```python
result = solver.atb_captcha(app_id='af25e409b33d722a95e56a230ff8771c',
                            api_server='https://cap.aisecurius.com',
                            url='http://mysite.com/', 
                            param1=..., ...)

```


### Capy

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_capy)</sup>

Token-based method to bypass Capy puzzle captcha.
```python
result = solver.capy(sitekey='PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
                     url='http://mysite.com/',
                     api_server='https://jp.api.capy.me/',
                     param1=..., ...)
```
### Grid

<sup>[API method description.](https://2captcha.com/2captcha-api#grid)</sup>

The grid method was originally called the Old reCAPTCHA V2 method. The method can be used to bypass any type of captcha where you can apply a grid on an image and click specific grid boxes. Returns numbers of boxes.

```python
result = solver.grid('path/to/captcha.jpg', param1=..., ...)
```

### Canvas

<sup>[API method description.](https://2captcha.com/2captcha-api#canvas)</sup>

The canvas method can be used when you need to draw a line around an object on an image. Returns a set of points' coordinates to draw a polygon.

```python
result = solver.canvas('path/to/captcha.jpg', param1=..., ...)
```

### ClickCaptcha

<sup>[API method description.](https://2captcha.com/2captcha-api#coordinates)</sup>

The ClickCaptcha method returns the coordinates of points on the captcha image. It can be used if you need to click on particular points in the image.

```python
result = solver.coordinates('path/to/captcha.jpg', param1=..., ...)
```

### Rotate

<sup>[API method description.](https://2captcha.com/2captcha-api#solving_rotatecaptcha)</sup>

This method can be used to solve a captcha that asks to rotate an object. It is mostly used to bypass FunCaptcha. Returns the rotation angle.

```python
result = solver.rotate('path/to/captcha.jpg', param1=..., ...)
```

### MTCaptcha

<sup>[API method description.](https://2captcha.com/2captcha-api#mtcaptcha)</sup>

Use this method to solve MTCaptcha and obtain a token to bypass the protection.
```python
result = solver.mtcaptcha(sitekey='MTPublic-KzqLY1cKH',
                          url='https://2captcha.com/demo/mtcaptcha',
                          param1=..., ...)
```

### Friendly Captcha

<sup>[API method description.](https://2captcha.com/2captcha-api#friendly-captcha)</sup>

Friendly Captcha solving method. Returns a token.

> [!IMPORTANT]
> To successfully use the received token, the captcha widget must not be loaded on the page. To do this, you need to abort request to `/friendlycaptcha/...module.min.js` on the page. When the captcha widget is already loaded on the page, there is a high probability that the received token will not work.

```python
result = solver.friendly_captcha(sitekey='FCMGEMUD2KTDSQ5H',
                                 url='https://friendlycaptcha.com/demo',
                                 param1=..., ...)
```

### Cutcaptcha

<sup>[API method description.](https://2captcha.com/2captcha-api#cutcaptcha)</sup>

Use this method to solve Cutcaptcha. Returns the response in JSON.
```python
result = solver.cutcaptcha(misery_key='ad52c87af17e2ec09b8d918c9f00416b1cb8c320',
                           apikey='SAs61IAI',
                           url='https://mysite.com/page/with/cutcaptcha',
                           param1=..., ...)
```

### Tencent

<sup>[API method description.](https://2captcha.com/2captcha-api#tencent)</sup>

Use this method to solve Tencent captcha. Returns a token.
```python
result = solver.tencent(app_id="197326679",
                        url="https://mysite.com/page/with/tencent",
                        param1=..., ...)
```

### DataDome

<sup>[API method description.](https://2captcha.com/2captcha-api#datadome)</sup>

Use this method to solve DataDome captcha.

> [!IMPORTANT]
> To solve the DataDome captcha, you must use a proxy. It is recommended to use [residential proxies].

```python
result = solver.datadome(captcha_url="https://geo.captcha-delivery.com/captcha/?initialCid=...",
                         pageurl="https://mysite.com/page/with/datadome",
                         userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                         proxy={
                            'type': 'HTTP',
                            'uri': 'login:password@IP_address:PORT'
                         },
                         param1=..., ...)
```

### CyberSiARA

<sup>[API method description.](https://2captcha.com/2captcha-api#cybersiara)</sup>

Use this method to solve CyberSiARA. Returns a token.
```python
result = solver.cybersiara(master_url_id='tpjOCKjjpdzv3d8Ub2E9COEWKt1vl1Mv',
                           pageurl='https://demo.mycybersiara.com/',
                           userAgent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                           param1=..., ...)
```

## Other methods

### send / get_result
These methods can be used for manual captcha submission and answer polling. The `send()` method supports sending any captcha 
type, to specify the captcha type you must send value `method` manually, for example `method='recaptcha'` for solving reCaptcha. 
You can find the value of the `method` parameter in the [API documentation](https://2captcha.com/2captcha-api).

Example for solving Normal captcha manually:
```python
import time
. . . . . 


id = solver.send(file='path/to/captcha.jpg')
time.sleep(20)

code = solver.get_result(id)
```

### balance

<sup>[API method description.](https://2captcha.com/2captcha-api#additional-methods)</sup>

Use this method to get your account's balance
```python
balance = solver.balance()
```

### report

<sup>[API method description.](https://2captcha.com/2captcha-api#complain)</sup>

Use this method to report good or bad captcha answers.
```python
solver.report(id, True) # captcha solved correctly
solver.report(id, False) # captcha solved incorrectly
```

## Error handling
In case of an error, the captcha solver throws an exception. It's important to properly handle these cases. We recommend using `try except` to handle exceptions.
The list of all errors can be found in the  [API documentation](https://2captcha.com/2captcha-api#list-of-inphp-errors).
```python
try:
    result = solver.text('If tomorrow is Saturday, what day is today?')
except ValidationException as e:
    # invalid parameters passed
	print(e)
except NetworkException as e:
	# network error occurred
	print(e)
except ApiException as e:
    # api respond with error
	print(e)
except TimeoutException as e:
    # captcha is not solved so far
	print(e)
```


## Proxies

You can pass your proxy as an additional argument for the following methods: recaptcha, funcaptcha, geetest, geetest v4, 
keycaptcha, capy puzzle, lemin, atbcaptcha, turnstile, amazon waf, mtcaptcha, friendly captcha, cutcaptcha, Tencent, DataDome, cybersiara. 


The proxy will be forwarded to the API to solve the captcha.

We have our own proxies that we can offer you. [Buy residential proxies] to avoid restrictions and blocks. [Quick start].

```python
proxy={
    'type': 'HTTPS',
    'uri': 'login:password@IP_address:PORT'
}
```

## Async calls
You can also make async calls with [asyncio], for example:

```python
import asyncio
import concurrent.futures
from twocaptcha import TwoCaptcha

API_KEY = "YOUR_API_KEY"
image = "data:image/png;base64,iVBORw0KGgoA..."

async def captchaSolver(image):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, lambda: TwoCaptcha(API_KEY).normal(image))
        return result

captcha_result = asyncio.run(captchaSolver(image))
```
## Examples
Examples of solving all supported captcha types are located in the [examples] directory.

## Examples using Selenium
Also we have a [separate repository](https://github.com/2captcha/captcha-solver-selenium-python-examples) you can find examples of captcha solving using [Selenium](https://pypi.org/project/selenium/) library. At the moment we have implemented examples of bypassing [reCAPTCHA](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/reCAPTCHA), [Cloudflare](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/cloudflare), [Coordinates](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/coordinates), [MTCaptcha](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/mtcaptcha),  [normal captcha](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/normal_captcha) (image captcha) and [text captcha](https://github.com/2captcha/captcha-solver-selenium-python-examples/tree/main/examples/text_captcha) using Selenium.

## Useful articles

- Amazon captcha solver: Code example for bypassing the [Amazon captcha](https://2captcha.com/blog/amazon-captcha-solving)
- [Captcha bypass in Selenium](https://2captcha.com/blog/captcha-bypass-in-selenium)

## Get in touch

<a href="mailto:support@2captcha.com"><img src="https://github.com/user-attachments/assets/539df209-7c85-4fa5-84b4-fc22ab93fac7" width="80" height="30"></a>
<a href="https://2captcha.com/support/tickets/new"><img src="https://github.com/user-attachments/assets/be044db5-2e67-46c6-8c81-04b78bd99650" width="81" height="30"></a>

## Join the team 👪

There are many ways to contribute, of which development is only one! Find your next job. Open positions: AI experts, scrapers, developers, technical support, and much more! 😍

<a href="mailto:job@2captcha.com"><img src="https://github.com/user-attachments/assets/36d23ef5-7866-4841-8e17-261cc8a4e033" width="80" height="30"></a>


## License

The code in this repository is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

### Graphics and Trademarks

The graphics and trademarks included in this repository are not covered by the MIT License. Please contact <a href="mailto:support@2captcha.com">support</a> for permissions regarding the use of these materials.


<!-- Shared links for README.md -->
[2Captcha]: https://2captcha.com/
[2captcha software catalog]: https://2captcha.com/software
[pingback settings]: https://2captcha.com/setting/pingback
[post options]: https://2captcha.com/2captcha-api#normal_post
[list of supported languages]: https://2captcha.com/2captcha-api#language
[examples directory]: /examples
[asyncio]: https://docs.python.org/3/library/asyncio.html
[Buy residential proxies]: https://2captcha.com/proxy/residential-proxies
[Quick start]: https://2captcha.com/proxy?openAddTrafficModal=true
[examples]: ./examples
[residential proxies]: https://2captcha.com/proxy/residential-proxies
