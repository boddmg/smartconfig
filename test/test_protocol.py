import unittest
from smartconfig import protocol


class test_protocol(unittest.TestCase):
    def __init__(self):
        encoder = protocol.Encoder()
        encoder.calculate()
        self.assertEqual()