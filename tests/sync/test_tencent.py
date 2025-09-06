#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class TencentTest(AbstractTest):

    def test_all_params(self):
        params = {
            "app_id": "197322596",
            "url": "https://www.holla.world/random-video-chat#app"
        }

        sends = {
            "method":  "tencent",
            "app_id": "197322596",
            "pageurl": "https://www.holla.world/random-video-chat#app",
        }

        return self.send_return(sends, self.solver.tencent, **params)


if __name__ == '__main__':
    unittest.main()
