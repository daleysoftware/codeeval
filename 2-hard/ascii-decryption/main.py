import sys
import re
import collections

def parse(line):
    split = line.strip().split(' | ')
    return int(split[0]), split[1], map(int, split[2].split(' '))

def array1_equals_array2(array1, array2):
    if len(array1) != len(array2): return False
    for i in xrange(len(array1)):
        if array1[i] != array2[i]: return False
    return True

def find_repeated_elements_in_array_of_length(length, array):
    result = set()
    for i in xrange(0, len(array)):
        array1 = array[i:i+length]
        for j in xrange(i+1, len(array)):
            array2 = array[j:j+length]
            if array1_equals_array2(array1, array2):
                result.add(tuple(array1))
                continue
    return result

def decrypt(length_repeated_word, last_letter_of_word, encrypted_message):
    repeated = find_repeated_elements_in_array_of_length(length_repeated_word, encrypted_message)
    for repeat in repeated:
        n = repeat[-1] - ord(last_letter_of_word)
        decrypted = ''.join([chr(e-n) for e in encrypted_message])
        repeat = ''.join([chr(r-n) for r in repeat])
        if collections.Counter(re.findall(r"[\w']+", decrypted))[repeat] >= 2:
            return decrypted

def main():
    with open(sys.argv[1], 'r') as fh:
        for line in fh:
            if len(line.strip()) == 0: continue
            length_repeated_word, last_letter_of_word, encrypted_message = parse(line)
            print decrypt(length_repeated_word, last_letter_of_word, encrypted_message)

if __name__ == '__main__':
    main()