#!/usr/bin/env python3

import unittest
from base64 import b64encode


file = '../examples/audio/example.mp3'
url = 'https://github.com/2captcha/2captcha-python/raw/polukhin_audio/examples/audio/example.mp3'


with open(file, "rb") as media:
    b64 = b64encode(media.read()).decode('utf-8')

try:
    from .abstract import AbstractTest

    file = file[3:]
    
except ImportError:
    from abstract import AbstractTest




class AudioTest(AbstractTest):

    def test_base64(self):

        params = {
                'lang' : 'en',
                }

        sends = {
                'method': 'audio',
                'lang'  : 'en',                
                'body'  : b64,
                }

        return self.send_return(sends, self.solver.audio, file=b64, lang='en')

    def test_file(self):

        params = {
                'lang' : 'en',
                }

        sends = {            
                'method': 'audio',
                'lang'  : 'en',
                'body'  : b64,
                }

        return self.send_return(sends, self.solver.audio, file=file, lang='en')


    def test_url(self):

        sends = {            
                'method': 'audio',
                'lang'  : 'en',
                'body'  : b64,
                }

        return self.send_return(sends, self.solver.audio, file=url, lang='en')


if __name__ == '__main__':

    unittest.main()

