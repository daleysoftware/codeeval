import sys
import binascii
import socket
import struct

def ip_to_hex(ip):
    return binascii.hexlify(socket.inet_aton(ip)).decode('utf-8')

def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def compute_checksum(data):
    s = 0
    for i in range(0, len(list(data)), 2):
        w = ord(data[i]) + (ord(data[i+1]) << 8)
        s = carry_around_add(s, w)
    return ~s & 0xffff

def format_data(data):
    data = [data[i:i+2] for i in range(0, len(list(data)), 2)]
    data = map(lambda x: int(x, 16), data)
    list(data)
    return struct.pack("%dB" % len(list(data)), *data)

def main():
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            test = test.strip().split(' ')
            src = ip_to_hex(test[0])
            dst = ip_to_hex(test[1])
            package = ''.join(test[2:])
            ihl = int(package[1])
            header_length = 48 if (ihl > 5) else 40
            header = package[:header_length]
            new_header = header[:20] + '0000' + src + dst + header[40:]
            checksum = format(compute_checksum(format_data(new_header)), 'x').zfill(4)
            new_header = new_header[:20] + checksum[2:4] + checksum[0:2] + new_header[24:]
            print(' '.join([new_header[i:i+2] for i in range(0, len(new_header), 2)]))

if __name__ == '__main__':
    main()
