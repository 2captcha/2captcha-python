#!/usr/bin/env python3

import unittest


file = '../examples/images/canvas.jpg'
hint = 'Draw around apple'
hint_img = '../examples/images/canvas_hint.jpg'

checks = {'canvas' : 1, 'recaptcha' : 1, 'textinstructions' : hint}


try:
    from .abstract import AbstractTest

    file = file[3:]
    hint_img = hint_img[3:]

except ImportError:
    from abstract import AbstractTest






class CanvasTest(AbstractTest):

    def test_file_param(self):
        
        sends = {'method': 'post', 'file': file, **checks}
        return self.send_return(sends, self.solver.canvas, file=file, hintText=hint)



    def test_base64_param(self):
        
        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        sends = {
                'method': 'base64',
                'body'  : b64,
                **checks,
                }

        return self.send_return(sends, self.solver.canvas, file=b64, hintText=hint)



    def test_all_params(self):
        
        
        params = {
                'previousId' :	0,
                'canSkip'    :	0,
                'lang'       :	'en',
                'hintImg'    :  hint_img,
                'hintText'   :	hint
                }


        sends = {
                'method'           : 'post',
                'previousID'       :  0,
                'can_no_answer'    :  0,
                'lang'             : 'en',
                'files'            : {'file': file,'imginstructions': hint_img},
                **checks
                }
        
        return self.send_return(sends, self.solver.canvas, file=file, **params)



    def test_not_found(self):

        return self.invalid_file(self.solver.canvas, hintText=hint)









if __name__ == '__main__':

    unittest.main()

