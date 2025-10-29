#!/usr/bin/env python3

import unittest
from pathlib import Path
from base64 import b64encode

images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
files = [str(images_path / 'vk.jpg')]
files_dict = {f'file_{i + 1}': path for i, path in enumerate(files)}

STEPS = ('[5,4,7,7,14,22,8,3,2,7,23,22,2,8,24,5,9,20,2,5,0,6,22,4,5,11,12,12,9,6,18,3,21,18,17,7,6,'
         '1,4,19,8,11,3,14,20,6,16,11,23,0,10,14,10,9,24,3,14,14,10,0,15,10,6,6,20,12,18,13,20,7,13,'
         '9,22,14,24,14,17,22,0,4,6,11,10,15,18,20,0,3,6,4,23,12,15,14,18,4,2,9,5,2]')

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncVkImage(AsyncAbstractTest):
    def test_single_file(self):
        sends = {'method': 'vkimage', 'file': files[0], 'steps': STEPS}
        self.send_return(sends, self.solver.vkimage, files=files[0], steps=STEPS)

    def test_files_list(self):
        sends = {'method': 'vkimage', 'files': files_dict, 'steps': STEPS}
        self.send_return(sends, self.solver.vkimage, files=files, steps=STEPS)

    def test_files_dict(self):
        sends = {'method': 'vkimage', 'files': files_dict, 'steps': STEPS}
        self.send_return(sends, self.solver.vkimage, files=files_dict, steps=STEPS)

    def test_all_params(self):
        params = {'files': files[0], 'steps': STEPS}
        sends = {'method': 'vkimage', 'file': files[0], 'steps': STEPS}
        self.send_return(sends, self.solver.vkimage, **params)

    def test_base64_body(self):
        with open(files[0], 'rb') as fh:
            body = b64encode(fh.read()).decode('utf-8')
        params = {'files': body, 'steps': STEPS}
        sends = {'method': 'vkimage', 'body': body, 'steps': STEPS}
        self.send_return(sends, self.solver.vkimage, **params)

    def test_not_found(self):
        self.invalid_file(self.solver.vkimage, steps=STEPS)

    def test_too_many(self):
        self.too_many_files(self.solver.vkimage, steps=STEPS)


if __name__ == '__main__':
    unittest.main()
