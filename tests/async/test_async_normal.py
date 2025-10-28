#!/usr/bin/env python3

import unittest
from pathlib import Path

images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
file = str(images_path / 'normal.jpg')
hint_img = str(images_path / 'grid_hint.jpg')

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncNormalTest(AsyncAbstractTest):
    def test_file(self):
        sends = {'method': 'post', 'file': file}
        self.send_return(sends, self.solver.normal, file=file)

    def test_base64(self):
        b64 = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
        sends = {
            'method': 'base64',
            'body': b64,
        }

        self.send_return(sends, self.solver.normal, file=b64)

    def test_all_params(self):
        params = {
            'numeric': 4,
            'minLen': 4,
            'maxLen': 20,
            'phrase': 1,
            'caseSensitive': 1,
            'calc': 0,
            'lang': 'en',
            'hintImg': hint_img,
            'hintText': 'Type red symbols only',
        }

        sends = {
            'files': {'file': file, 'imginstructions': hint_img},
            'method': 'post',
            'numeric': 4,
            'min_len': 4,
            'max_len': 20,
            'phrase': 1,
            'regsense': 1,
            'calc': 0,
            'lang': 'en',
            'textinstructions': 'Type red symbols only',
        }

        self.send_return(sends, self.solver.normal, file=file, **params)

    def test_not_found(self):
        self.invalid_file(self.solver.normal)


if __name__ == '__main__':
    unittest.main()
