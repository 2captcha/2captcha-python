#!/usr/bin/env python3

import unittest
from pathlib import Path

images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
file = str(images_path / 'grid.jpg')
hint_img = str(images_path / 'grid_hint.jpg')
hint_text = 'Select all images with an Orange'
checks = {'coordinatescaptcha': 1}

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


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
