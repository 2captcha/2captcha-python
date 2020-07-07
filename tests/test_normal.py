#!/usr/bin/env python3

import unittest

file = '../examples/images/normal.jpg'
hint_img = '../examples/images/grid_hint.jpg'


try:
    from .abstract import AbstractTest

    file = file[3:]
    hint_img = hint_img[3:]
    
except ImportError:
    from abstract import AbstractTest




class NormalTest(AbstractTest):
    
    def test_file(self):
        
        sends = {'method': 'post', 'file': file}
        return self.send_return(sends, self.solver.normal, file=file)



    # def test_file_params(self):
        
    #     return self.test_send_return(self.method, self.file, method='post')



    def test_base64(self):
        
        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        sends = {
                'method': 'base64',
                'body'  : b64,
                }

        return self.send_return(sends, self.solver.normal, file=b64)



    def test_all_params(self):

        
        params = {
                'numeric'       : 4,
                'minLen'        : 4,
                'maxLen'        : 20,
                'phrase'        : 1,
                'caseSensitive' : 1,
                'calc'          : 0,
                'lang'          : 'en',
                'hintImg'       : hint_img,
                'hintText'      : 'Type red symbols only',
                }


        sends = {
                'files'            : {'file': file,'imginstructions': hint_img},
                'method'           : 'post',
                'numeric'          : 4,
                'min_len'          : 4,
                'max_len'          : 20,
                'phrase'           : 1,
                'regsense'         : 1,
                'calc'             : 0,
                'lang'             : 'en',
                'textinstructions' : 'Type red symbols only',
                }

        # files = {
        #         'file'            : file,
        #         'imginstructions' : hint,
        #         }

        return self.send_return(sends, self.solver.normal, file=file, **params)



    def test_not_found(self):

        return self.invalid_file(self.solver.normal)










if __name__ == '__main__':

    unittest.main()

