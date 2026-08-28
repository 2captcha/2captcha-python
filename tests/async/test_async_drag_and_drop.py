#!/usr/bin/env python3

import asyncio
import json
import unittest
from base64 import b64encode
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

images_path = Path(__file__).resolve().parents[2] / 'examples' / 'images'
background = str(images_path / 'canvas.jpg')
image1 = str(images_path / 'grid.jpg')
image2 = str(images_path / 'normal.jpg')

with open(image1, 'rb') as fh:
    image1_b64 = b64encode(fh.read()).decode('utf-8')

with open(image2, 'rb') as fh:
    image2_b64 = b64encode(fh.read()).decode('utf-8')

with open(background, 'rb') as fh:
    background_b64 = b64encode(fh.read()).decode('utf-8')

background_url = 'https://example.com/background.jpg'
image1_url = 'https://example.com/image1.jpg'
image2_url = 'https://example.com/image2.jpg'

background_url_bytes = b'background-url-bytes'
image1_url_bytes = b'image1-url-bytes'
image2_url_bytes = b'image2-url-bytes'

background_url_b64 = b64encode(background_url_bytes).decode('utf-8')
image1_url_b64 = b64encode(image1_url_bytes).decode('utf-8')
image2_url_b64 = b64encode(image2_url_bytes).decode('utf-8')

URL_CONTENT = {
    background_url: background_url_bytes,
    image1_url: image1_url_bytes,
    image2_url: image2_url_bytes,
}


def fake_get(url, status_code=200):
    if url not in URL_CONTENT:
        raise AssertionError(f'unexpected url requested: {url}')
    return MagicMock(status_code=status_code, content=URL_CONTENT[url])


try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncDragAndDrop(AsyncAbstractTest):

    def test_files(self):
        sends = {
            'method': 'drag_drop',
            'body': background_b64,
            'images': json.dumps([image1_b64, image2_b64]),
        }

        self.send_return(sends, self.solver.drag_and_drop,
                         body=background, images=[image1, image2])
        self.assertNotIn('file', self.solver.api_client.incomings)

    def test_base64(self):
        sends = {
            'method': 'drag_drop',
            'body': background_b64,
            'images': json.dumps([image1_b64, image2_b64]),
        }

        self.send_return(sends, self.solver.drag_and_drop,
                         body=background_b64, images=[image1_b64, image2_b64])
        self.assertNotIn('file', self.solver.api_client.incomings)

    def test_url(self):
        sends = {
            'method': 'drag_drop',
            'body': background_url_b64,
            'images': json.dumps([image1_url_b64, image2_url_b64]),
        }

        with patch('httpx.AsyncClient.get', new_callable=AsyncMock, side_effect=fake_get) as mock_get:
            self.send_return(sends, self.solver.drag_and_drop,
                             body=background_url, images=[image1_url, image2_url])

        mock_get.assert_any_call(background_url)
        mock_get.assert_any_call(image1_url)
        mock_get.assert_any_call(image2_url)
        self.assertNotIn('file', self.solver.api_client.incomings)

    def test_images_order_preserved_with_mixed_sources(self):
        fake_b64_string = 'B' * 60

        sends = {
            'method': 'drag_drop',
            'body': background_b64,
            'images': json.dumps([image1_url_b64, image2_b64, fake_b64_string]),
        }

        with patch('httpx.AsyncClient.get', new_callable=AsyncMock, side_effect=fake_get):
            self.send_return(sends, self.solver.drag_and_drop,
                             body=background, images=[image1_url, image2, fake_b64_string])

    def test_all_params(self):
        params = {
            'body': background,
            'images': [image1, image2],
            'hintText': 'Drag the images to proper position',
            'language': 0,
            'lang': 'en',
            'header_acao': 0,
        }

        sends = {
            'method': 'drag_drop',
            'body': background_b64,
            'images': json.dumps([image1_b64, image2_b64]),
            'textinstructions': 'Drag the images to proper position',
            'language': 0,
            'lang': 'en',
            'header_acao': 0,
        }

        self.send_return(sends, self.solver.drag_and_drop, **params)
        self.assertNotIn('file', self.solver.api_client.incomings)

    def test_body_not_found(self):
        self.invalid_file(self.solver.drag_and_drop, images=[image1])

    def test_image_not_found(self):
        with self.assertRaises(self.solver.exceptions):
            asyncio.run(self.solver.drag_and_drop(background, ['lost_file']))

    def test_body_url_download_failure(self):
        with patch('httpx.AsyncClient.get', new_callable=AsyncMock,
                   side_effect=lambda url: fake_get(url, status_code=404)):
            with self.assertRaises(self.solver.exceptions):
                asyncio.run(self.solver.drag_and_drop(background_url, [image1]))

    def test_image_url_download_failure(self):
        with patch('httpx.AsyncClient.get', new_callable=AsyncMock,
                   side_effect=lambda url: fake_get(url, status_code=500)):
            with self.assertRaises(self.solver.exceptions):
                asyncio.run(self.solver.drag_and_drop(background, [image1_url]))


if __name__ == '__main__':
    unittest.main()
