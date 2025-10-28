#!/usr/bin/env python3

import unittest
from pathlib import Path

images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
files = [str(images_path / 'rotate.jpg')]

hint_img = str(images_path / 'grid_hint.jpg')
hint_text = 'Put the images in the correct way up'

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest

files_dict = {f'file_{e + 1}': f for e, f in enumerate(files)}

checks = {'method': 'rotatecaptcha'}


class AsyncRotateTest(AsyncAbstractTest):
    def test_single_file(self):
        sends = {'method': 'post', 'file': files[0], **checks}
        self.send_return(sends, self.solver.rotate, files=files[0])

    def test_file_param(self):
        sends = {'method': 'post',
                 'files': {'file_1': files[0]},
                 **checks}

        self.send_return(sends, self.solver.rotate, files=files[:1])

    def test_files_list(self):
        sends = {'method': 'post', 'files': files_dict, **checks}
        self.send_return(sends, self.solver.rotate, files=files)

    def test_files_dict(self):
        sends = {'method': 'post', 'files': files_dict, **checks}
        self.send_return(sends, self.solver.rotate, files=files_dict)

    def test_all_params(self):
        params = {
            'angle': 40,
            'lang': 'en',
            'hintImg': hint_img,
            'hintText': hint_text
        }

        sends = {
            'method': 'rotatecaptcha',
            'angle': 40,
            'lang': 'en',
            'textinstructions': hint_text,
            'files': {'file': files[0], 'imginstructions': hint_img},
            **checks
        }

        self.send_return(sends, self.solver.rotate, file=files[0], **params)

    def test_not_found(self):
        self.invalid_file(self.solver.rotate)

    def test_too_many(self):
        self.too_many_files(self.solver.rotate)


if __name__ == '__main__':
    unittest.main()
