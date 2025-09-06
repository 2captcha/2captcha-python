#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest

class AmazonWAFTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'sitekey' : 'AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AFsClhVgr5q0UFRdXhhHEwiAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLMbH8d6uQSrYTraoAgEQgDvtSNxdEyG7Zu393cHyPdWNCZgeIB52+W7fCTI8U5z15z1NdPUdnB1ZHoK7ewpwoSMm5mzkJJld0cnvGw==',
                'url'     : 'https://www.site.com/page/',
                'iv'      : 'CgAAYDJb9CAAACAq',
                'context' : 'wCho9T9OcETTT8fu1k6+rszr5aGt4eLd+K3mHpV8VbSkjAWJGJx/iQ16RKDCTQBtU5OSeE+SQqoS5iTzhgGtvwgmBbr7X/I+aXaNfb2JRZ8eJ7CnQpM9QRwnv7vGgrGRBGhkh/jaVYmXdy0j0x21s3dCBlA4VN3naDHIweZqkyhXqJBNI1Ep8OMSnhXtPebboB117aBW4IU4XEOii8EE1G4Z7ndWhrNVVXYYwVoxfnSqfYX//CJir6dZfLMbCt5t7NnO8yjsx/YHGVXFVBt2Zrj0ZTxowoYbHU/BKyFaXgUj+ZQ='
                }
        
        sends = {
                'method'  : 'amazon_waf',
                'sitekey' : 'AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AFsClhVgr5q0UFRdXhhHEwiAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLMbH8d6uQSrYTraoAgEQgDvtSNxdEyG7Zu393cHyPdWNCZgeIB52+W7fCTI8U5z15z1NdPUdnB1ZHoK7ewpwoSMm5mzkJJld0cnvGw==',
                'iv'      : 'CgAAYDJb9CAAACAq',
                'context' : 'wCho9T9OcETTT8fu1k6+rszr5aGt4eLd+K3mHpV8VbSkjAWJGJx/iQ16RKDCTQBtU5OSeE+SQqoS5iTzhgGtvwgmBbr7X/I+aXaNfb2JRZ8eJ7CnQpM9QRwnv7vGgrGRBGhkh/jaVYmXdy0j0x21s3dCBlA4VN3naDHIweZqkyhXqJBNI1Ep8OMSnhXtPebboB117aBW4IU4XEOii8EE1G4Z7ndWhrNVVXYYwVoxfnSqfYX//CJir6dZfLMbCt5t7NnO8yjsx/YHGVXFVBt2Zrj0ZTxowoYbHU/BKyFaXgUj+ZQ=',
                'pageurl' : 'https://www.site.com/page/',
                }

        return self.send_return(sends, self.solver.amazon_waf, **params)


if __name__ == '__main__':

    unittest.main()


        # sitekey='AQIDAHjcYu/GjX+QlghicBgQ/7bFaQZ+m5FKCMDnO+vTbNg96AFsClhVgr5q0UFRdXhhHEwiAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMLMbH8d6uQSrYTraoAgEQgDvtSNxdEyG7Zu393cHyPdWNCZgeIB52+W7fCTI8U5z15z1NdPUdnB1ZHoK7ewpwoSMm5mzkJJld0cnvGw==',
        # iv='CgAAYDJb9CAAACAq',
        # context='wCho9T9OcETTT8fu1k6+rszr5aGt4eLd+K3mHpV8VbSkjAWJGJx/iQ16RKDCTQBtU5OSeE+SQqoS5iTzhgGtvwgmBbr7X/I+aXaNfb2JRZ8eJ7CnQpM9QRwnv7vGgrGRBGhkh/jaVYmXdy0j0x21s3dCBlA4VN3naDHIweZqkyhXqJBNI1Ep8OMSnhXtPebboB117aBW4IU4XEOii8EE1G4Z7ndWhrNVVXYYwVoxfnSqfYX//CJir6dZfLMbCt5t7NnO8yjsx/YHGVXFVBt2Zrj0ZTxowoYbHU/BKyFaXgUj+ZQ=',
        # url='https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest',