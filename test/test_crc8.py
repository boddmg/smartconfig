#!/bin/python
# test_crc8.py

from nose.tools import *
from smartconfig.crc8 import crc8

def test_crc8():
    input = "2333333333"
    output = 0xe9
    assert_equal(crc8(input), output)

