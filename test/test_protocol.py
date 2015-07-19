import unittest
from smartconfig import Protocol
from smartconfig import Utilities
from smartconfig import crc8


class test_protocol(unittest.TestCase):
    def setUp(self):
        self.flag = 123
        self.base = 100
        self.packer = Protocol.Packer(self.flag, self.base)
        self.receiver = Protocol.Receiver(lambda data:Utilities.debug_print(data))

    def test_packer(self):
        packed_string = self.packer.calculate("123")
        crc = crc8.crc8("123")
        except_list = []
        except_list += [self.flag]
        except_list += [self.base + 8]
        except_list += [self.base + (ord('1')>>4) ]
        except_list += [self.base + (ord('1')&0x0f | (ord('1')&0xf0 ^ 0x10) )]
        except_list += [self.base + (ord('2')>>4 | (((ord('1')&0x0f) << 4) ^ 0x20))]
        except_list += [self.base + ( ord('2')&0x0f | (ord('2')&0xf0 ^ 0x30) )]
        except_list += [self.base + (ord('3')>>4 | ((ord('2')&0x0f) << 4 )^ 0x40)]
        except_list += [self.base + ( ord('3')&0x0f | (ord('3')&0xf0 ^ 0x50) )]
        except_list += [self.base + (crc>>4 | ((ord('3')&0x0f) << 4 )^ 0x60)]
        except_list += [self.base + ( crc&0x0f | (crc&0xf0 ^ 0x70) )]
        self.assertEqual(except_list, packed_string)

