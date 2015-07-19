import crc8
import Utilities


FLAG = 200
BASE = 100


class DataPoint(object):
    def __init__(self, id, data):
        self.id = id
        self.data = data


class Node(object):
    def __init__(self, id):
        self._id = id
        self._data_queue = []

    def push_data(self, data):
        if self._is_new_data_point_valid(data):
            self._data_queue += [data]

    def _is_new_data_point_valid(self, data):
        pass


class Packer(object):
    def __init__(self, flag, base):
        self._flag = flag
        self._base = base
        pass

    def calculate(self, src_data = None):
        if src_data == None:
            return self.dst_data
        src_data = bytearray(src_data)
        src_data.append(crc8.crc8(src_data))
        dst_data = []
        dst_data.append(self._flag)
        dst_data.append(self._base + len(src_data)*2 )
        last_nibble = 0

        for i in range(len(src_data)):
            now_nibble = int(src_data[i]) >> 4
            dst_data.append( self._base + ( (((i * 2) ^ last_nibble) << 4) | now_nibble))
            last_nibble = now_nibble

            now_nibble = int(src_data[i]) & 0x0f
            dst_data.append( self._base + ( (((i * 2 + 1) ^ last_nibble) << 4) | now_nibble))
            last_nibble = now_nibble
        return dst_data


class Receiver(object):
    def __init__(self, received_callback, cache_depth = 100):
        self._cache_depth = cache_depth
        self._node = {}
        self._received_callback = received_callback

    def add_new_data_point(self, new_data_point):
        assert(type(new_data_point) == DataPoint)
        if self._node.has_key(new_data_point.id):
            self._node[new_data_point.id].push_data(new_data_point.data)
        else:
            if len(self._node) > self._cache_depth:
                self._node.pop(
                    min(self._node,
                        key=lambda x: len(self._node[x]._data_queue)))
            self._node[new_data_point.id] = Node(new_data_point.id)
            self._node[new_data_point.id].push_data(new_data_point.data)




