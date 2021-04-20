import sys
'../../' in sys.path or sys.path.append('../../')

from twocaptcha import TwoCaptcha



sol = TwoCaptcha('YOUR_API_KEY', defaultTimeout=120)


try:
    result = sol.keycaptcha(s_s_c_user_id          = 10,
                            s_s_c_session_id       = '493e52c37c10c2bcdf4a00cbc9ccd1e8',
                            s_s_c_web_server_sign  = '9006dc725760858e4c0715b835472f22-pz-',
                            s_s_c_web_server_sign2 = '2ca3abe86d90c6142d5571db98af6714',
                            url                    = 'https://www.keycaptcha.ru/demo-magnetic/', 
                            proxy                  = {
                                                      'type': 'HTTPS',
                                                      'uri': 'login:password@IP_address:PORT'})

        
except Exception as e:
    sys.exit(e)
    
else:
    sys.exit('result: ' + str(result))

    