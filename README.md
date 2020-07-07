## Installation


This package can be installed like this:

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
    		'apiKey':           'YOUR_API_KEY',
    		'softId':            123,
    		'callback':         'https://your.site/result-receiver',
    		'defaultTimeout':    120,
    		'recaptchaTimeout':  600,
    		'pollingInterval':   10,
	    }
solver = TwoCaptcha(**config)
```

## Solve captcha
Below shown only base examples for every captcha type. Check out examples directory to find more examples with all available options.

### Normal Captcha
```python 
result = solver.normal('path/to/captcha.jpg', param1=..., ...)
```

### Text Captcha
```python 
result = solver.text('If tomorrow is Saturday, what day is today?', param1=..., ...)
```

### ReCaptcha v2
```python 
result = solver.recaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                          url='https://mysite.com/page/with/recaptcha’,
                          param1=..., ...)
```

### ReCaptcha v3
```python
result = solver.recaptcha(sitekey=’6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/recaptcha',
                            version='v3',
                            param1=..., ...)
```

### FunCaptcha
```python
result = solver.funcaptcha(sitekey='6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                            url='https://mysite.com/page/with/funcaptcha',
                            param1=..., ...)

```


### GeeTest
```python
result = solver.geetest(gt='f1ab2cdefa3456789012345b6c78d90e',
                        challenge='12345678abc90123d45678ef90123a456b',
                        url='https://www.site.com/page/',
                        param1=..., ...)

```


### hCaptcha
```python
result = solver.funcaptcha(sitekey='f1ab2cdefa3456789012345b6c78d90e',
                            challenge='12345678abc90123d45678ef90123a456b',
                            url='https://www.site.com/page/', 
                            param1=..., ...)

```

### KeyCaptcha
```python
result = solver.keycaptcha(s_s_c_user_id=10,
    				   s_s_c_session_id='493e52c37c10c2bcdf4a00cbc9ccd1e8',
    				   s_s_c_web_server_sign='9006dc725760858e4c0715b835472f22-pz-',
    				   s_s_c_web_server_sign2='2ca3abe86d90c6142d5571db98af6714',
    				   url='https://www.keycaptcha.ru/demo-magnetic/', 
    				   param1=..., ...)

```

### Capy
```python
result = solver.capy(sitekey='PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
                     url='http://mysite.com/', 
                     param1=..., ...)
```
### Grid
```python
result = solver.grid('path/to/captcha.jpg', param1=..., ...)
```
### Canvas
```python
result = solver.canvas('path/to/captcha.jpg', param1=..., ...)
```
### ClickCaptcha
```python
result = solver.coordinates('path/to/captcha.jpg', param1=..., ...)
```

### Rotate
```python
result = solver.rotate(['path/to/captcha1.jpg', 'path/to/captcha2.jpg', ...], param1=..., ...)
```

## Other methods

### send / getResult
```python
import time
. . . . . 


id = solver.send(file='path/to/captcha.jpg')
time.sleep(20)

code = solver.getResult(id)
```

### balance
```python
balance = solver.balance()
```

### report
```python
solver.report(id, True) # captcha solved correctly
solver.report(id, False) # captcha solved incorrectly
```

### Error handling
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
