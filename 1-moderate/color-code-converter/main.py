import sys
import re
import colorsys
import struct

def format_rgb(r, g, b):
    return "RGB(%d,%d,%d)" % (r, g, b)

def is_hsl(color_code):
    return 'HSL' in color_code
def hsl_to_rgb(color_code):
    color_code = color_code.split('(')[1].split(')')[0]
    split = color_code.split(',')
    h = float(split[0])/360.0
    l = float(split[1])/100.0
    s = float(split[2])/100.0
    r, g, b =  colorsys.hls_to_rgb(h, l, s)
    r = int(round(r * 255, 0))
    g = int(round(g * 255, 0))
    b = int(round(b * 255, 0))
    return format_rgb(r, g, b)

def is_hsv(color_code):
    return 'HSV' in color_code
def hsv_to_rgb(color_code):
    color_code = color_code.split('(')[1].split(')')[0]
    split = color_code.split(',')
    h = float(split[0])/360.0
    s = float(split[1])/100.0
    v = float(split[2])/100.0
    r, g, b =  colorsys.hsv_to_rgb(h, s, v)
    r = int(round(r * 255, 0))
    g = int(round(g * 255, 0))
    b = int(round(b * 255, 0))
    return format_rgb(r, g, b)

def is_cmyk(color_code):
    return len(color_code) > 1 and color_code[0] == '('
def cmyk_to_rgb(color_code):
    color_code = re.sub('\(', '', color_code)
    color_code = re.sub('\)', '', color_code)
    split = color_code.split(',')
    c = float(split[0])
    m = float(split[1])
    y = float(split[2])
    k = float(split[3])
    r = int(round(255.0 * (1.0-c) * (1.0-k), 0))
    g = int(round(255.0 * (1.0-m) * (1.0-k), 0))
    b = int(round(255.0 * (1.0-y) * (1.0-k), 0))
    return format_rgb(r, g, b)

def is_hex(color_code):
    return len(color_code) > 1 and color_code[0] == '#'
def hex_to_rgb(color_code):
    r, g, b = struct.unpack('BBB', color_code[1:].decode('hex'))
    return format_rgb(r, g, b)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    color_code = test.strip()
    if len(color_code) == 0:
        continue
    if is_hsl(color_code):
        print hsl_to_rgb(color_code)
    elif is_hsv(color_code):
        print hsv_to_rgb(color_code)
    elif is_cmyk(color_code):
        print cmyk_to_rgb(color_code)
    elif is_hex(color_code):
        print hex_to_rgb(color_code)
    else:
        raise Exception()
test_cases.close()
