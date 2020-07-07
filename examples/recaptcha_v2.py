import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LcPh1EUAAAAAIscNcV6Ru2ZEtoUIgvUn3pCXFcV',
        url='https://www.runt.com.co/consultaCiudadana/#/consultaVehiculo')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
