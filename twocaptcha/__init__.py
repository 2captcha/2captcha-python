from .api import ApiClient
from .solver import TwoCaptcha

from .async_api import AsyncApiClient
from .async_solver import AsyncTwoCaptcha

from .solver import SolverExceptions, ValidationException, NetworkException, ApiException, TimeoutException


"""
Python 3 package for easy integration with the API of 2captcha captcha solving service to bypass recaptcha, 
funcaptcha, geetest and solve any other captchas.

website 2captcha [https://2captcha.com/]
support@2captcha.com
# License: MIT
"""

__author__ = '2captcha'
__version__ = '2.0.2'
