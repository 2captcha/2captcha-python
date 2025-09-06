#!/usr/bin/env python3

import unittest

file = '../examples/images/grid.jpg'
hint_img = '../examples/images/grid_hint.jpg'
hint_text = 'Select all images with an Orange'
checks = {'coordinatescaptcha': 1}

try:
    from .abstract_async import AsyncAbstractTest

except ImportError:
    from abstract_async import AsyncAbstractTest

    file = file[3:]
    hint_img = hint_img[3:]


class AsyncCoordinatesTest(AsyncAbstractTest):
    def test_file_param(self):
        sends = {'method': 'post', 'file': file, **checks}
        self.send_return(sends, self.solver.coordinates, file=file)

    def test_base64_param(self):
        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        sends = {
            'method': 'base64',
            'body': b64,
            **checks,
        }

        self.send_return(sends, self.solver.coordinates, file=b64)

    def test_all_params(self):
        params = {
            'lang': 'en',
            'hintImg': hint_img,
            'hintText': hint_text
        }

        sends = {
            'method': 'post',
            'lang': 'en',
            'files': {'file': file, 'imginstructions': hint_img},
            'textinstructions': hint_text,
            **checks
        }

        self.send_return(sends, self.solver.coordinates, file=file, **params)

    def test_not_found(self):
        self.invalid_file(self.solver.coordinates)


if __name__ == '__main__':
    unittest.main()
