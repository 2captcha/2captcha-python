#!/usr/bin/env python3

import unittest


files = ['../examples/images/rotate.jpg']

hint_img = '../examples/images/grid_hint.jpg'
hint_text = 'Put the images in the correct way up'
        

try:
    from .abstract import AbstractTest

    files = [f[3:] for f in files]
    hint_img = hint_img[3:]

except ImportError:
    from abstract import AbstractTest







files_dict = {f'file_{e+1}': f for e, f in enumerate(files)}

checks = {'method' : 'rotatecaptcha'}



class RotateTest(AbstractTest):

    def test_single_file(self):
        
        sends = {'method': 'post', 'file': files[0], **checks}
        return self.send_return(sends, self.solver.rotate, files=files[0])



    def test_file_param(self):
        
        sends = {'method': 'post',
                 'files': {'file_1': files[0]},
                 **checks}

        return self.send_return(sends, self.solver.rotate, files=files[:1])



    def test_files_list(self):
        
        sends = {'method': 'post', 'files': files_dict, **checks}
        return self.send_return(sends, self.solver.rotate, files=files)



    def test_files_dict(self):
        
        sends = {'method': 'post', 'files': files_dict, **checks}
        return self.send_return(sends, self.solver.rotate, files=files_dict)



    def test_all_params(self):
        
        params = {
                'angle'    : 40,
                'lang'     : 'en',
                'hintImg'  :  hint_img,
                'hintText' :	hint_text
                }


        sends = {
                'method'           : 'rotatecaptcha',
                'angle'            : 40,
                'lang'             : 'en',
                'textinstructions' : hint_text,
                'files'            : {'file': files[0],'imginstructions': hint_img},
                **checks
                }
        
        return self.send_return(sends, self.solver.rotate, file=files[0], **params)



    def test_not_found(self):

        return self.invalid_file(self.solver.rotate)



    def test_too_many(self):

        return self.too_many_files(self.solver.rotate)








if __name__ == '__main__':

    unittest.main()

