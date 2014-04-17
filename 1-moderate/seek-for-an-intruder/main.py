import sys
import re
import socket
import struct
import operator

def ip_address_is_valid(address):
    if address < 0x1000000:
        return False

    try:
        socket.inet_aton(int_to_formatted_ip(address))
    except socket.error:
        return False
    except struct.error:
        return False
    else:
        return True

def int_to_formatted_ip(x):
    return socket.inet_ntoa(struct.pack('!L', x))

def _find_helper(regex, formatter, content):
    ips = []
    for m in re.finditer(regex, content):
        ips.append(formatter(m.group(1)))
    return content, ips

def find_binary(content):
    regex = "([0,1]{8}[\.]?[0-1]{8}[\.]?[0-1]{8}[\.]?[0-1]{8})"
    def formatter(ip):
        return int(ip.replace(".", ""), 2)
    return _find_helper(regex, formatter, content)

def find_dotted_hex(content):
    regex = "(0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2}\.0x[0-9a-fA-F]{2})"
    def formatter(ip):
        return int(ip.replace("0x", "").replace(".", ""), 16)
    return _find_helper(regex, formatter, content)

def find_dotted_octal(content):
    regex = "([0-7]{4}\.[0-7]{4}\.[0-7]{4}\.[0-7]{4})"
    def formatter(ip):
        int_value = 0
        for sub_octal in ip.split('.'):
            int_value <<= 8
            int_value |= int(sub_octal, 8)
        return int_value
    return _find_helper(regex, formatter, content)

def find_dotted_decimal(content):
    regex = "([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    def formatter(ip):
        int_value = 0
        for sub in ip.split('.'):
            int_value <<= 8
            int_value |= int(sub)
        return int_value
    return _find_helper(regex, formatter, content)

def find_hex(content):
    regex = "(0x[0-9a-fA-F]{8})"
    def formatter(ip):
        return int(ip.replace("0x", ""), 16)
    return _find_helper(regex, formatter, content)

def find_octal(content):
    regex = "(0[0-7]+)"
    def formatter(ip):
        return int(ip, 8)

    return _find_helper(regex, formatter, content)
def find_decimal(content):
    regex = "([0-9]+)"
    def formatter(ip):
        return int(ip)
    return _find_helper(regex, formatter, content)

def main(content):
    all_ips = []
    for func in [find_dotted_octal, find_dotted_hex, find_binary,
                 find_dotted_decimal, find_hex, find_octal, find_decimal]:
        content, ips = func(content)
        all_ips.extend(ips)

    all_ips_frequency_map = {}
    for ip in all_ips:
        if not ip_address_is_valid(ip):
            continue

        if ip in all_ips_frequency_map:
            all_ips_frequency_map[ip] += 1
        else:
            all_ips_frequency_map[ip] = 1

    sorted_ips = sorted(all_ips_frequency_map.iteritems(), key=operator.itemgetter(1), reverse=True)

    max_frequency = sorted_ips[0][1]
    result = []
    for ip in sorted_ips:
        if ip[1] != max_frequency:
            break
        result.append(int_to_formatted_ip(ip[0]))
    print ' '.join(result)

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as content_file:
        content = content_file.read()
    main(content)