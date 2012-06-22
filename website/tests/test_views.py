#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

import website
import unittest
import tempfile

class FPOTestCase(unittest.TestCase):

    def test_homepage(self):
        self.app = website.app.test_client()
        resp = self.app.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_admin(self):
        self.app = website.app.test_client()
        resp = self.app.get('/admin/')
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
