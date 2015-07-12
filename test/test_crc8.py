#!/bin/python
# test_crc8.py

import unittest
from smartconfig.crc8 import crc8


class test_crc8(unittest.TestCase):
    def test_crc8(self):
        input = "2333333333"
        output = 0xe9
        self.assertEqual(crc8(input), output)


