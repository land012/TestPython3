__author__ = 'xudazhou'

def bytestoint(bytearr):
    i1 = bytearr[0] << 24
    i2 = bytearr[1] << 16
    i3 = bytearr[2] << 8
    i4 = bytearr[3]
    return i1 + i2 + i3 + i4