import crc8

FLAG = 100
BASE = 100

class Encoder(object):
    def __init__(self, src_data):
        self.dst_data = self.calculate(src_data)

    def calculate(self, src_data = None):
        if src_data == None:
            return self.dst_data
        dst_data = []
        dst_data.append(FLAG)
        dst_data.append(BASE + len(src_data)*2 )
        src_data.append(crc8.crc8(src_data))

        for i in range(len(src_data)):
            now_nibble = src_data[i] >> 4
            dst_data.append( BASE + ( (((i * 2) ^ last_nibble) << 4) | now_nibble))
            last_nibble = now_nibble

            now_nibble = src_data[i] & 0x0f
            dst_data.append( BASE + ( (((i * 2 + 1) ^ last_nibble) << 4) | now_nibble))
            last_nibble = now_nibble
        return dst_data

class Decoder(object):
    def __init__(self):
        self.src_data = []

    def add_new_data_point(self, new_data):
        pass

