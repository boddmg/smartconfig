
CRC8_DEAFAULT_PLOY = 0x31

def crc8(data, poly = CRC8_DEAFAULT_PLOY, is_lsb = False):
    crc = 0
    if is_lsb:
        NEW_BIT_LOCATION = 0x01
        SHIFT = lambda x: x >> 1
    else:
        NEW_BIT_LOCATION = 0x80
        SHIFT = lambda x: x << 1

    for i in data:
        if type(i) == str:
            i = ord(i)
        crc = crc ^ i
        for bit in range(8):
            if crc & NEW_BIT_LOCATION:
                crc = SHIFT(crc) ^ poly
            else:
                crc = SHIFT(crc)
        crc &= 0xff
    return crc

