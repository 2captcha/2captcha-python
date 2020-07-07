#!/usr/bin/env python3

import unittest


file = '../examples/images/grid.jpg'
hint_img = '../examples/images/grid_hint.jpg'
hint_text = 'Select all images with an Orange'


try:
    from .abstract import AbstractTest

    file = file[3:]
    hint_img = hint_img[3:]

except ImportError:
    from abstract import AbstractTest






class GridTest(AbstractTest):

    def test_file_param(self):
        
        sends = {'method': 'post', 'file': file, 'recaptcha': 1}
        return self.send_return(sends, self.solver.grid, file=file)



    def test_base64_param(self):
        
        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        sends = {
                'method'    : 'base64',
                'body'      : b64,
                'recaptcha' : 1
                }

        return self.send_return(sends, self.solver.grid, file=b64)



    def test_all_params(self):
        
        params = {
                'rows'       :	3,
                'cols'       :	3,
                'previousId' :	0,
                'canSkip'    :	0,
                'lang'       :	'en',
                'hintImg'    :  hint_img,
                'hintText'   :	hint_text
                }


        sends = {
                'method'           : 'post',
                'recaptcha'        : 1,
                'recaptcharows'    : 3,
                'recaptchacols'    : 3,
                'previousID'       : 0,
                'can_no_answer'    : 0, 
                'lang'             : 'en',
                'files'            : {'file': file,'imginstructions': hint_img},
                'textinstructions' : hint_text,
                }
        
        return self.send_return(sends, self.solver.grid, file=file, **params)



    def test_not_found(self):

        return self.invalid_file(self.solver.grid)









if __name__ == '__main__':

    unittest.main()

