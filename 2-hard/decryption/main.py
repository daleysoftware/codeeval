def main():
    message = '012222  1114142503  0313012513  03141418192102  0113  2419182119021713  06131715070119'
    key = 'BHISOECRTMGWYVALUZDNFJKPQX'
    count = 0
    key_map = {}
    for c in key:
        key_map[c] = count
        count += 1
    result = ""
    for i in range(0, len(message), 2):
        if message[i:i+2] == '  ': result += ' '; continue
        result += chr(ord('A') + key_map[chr(ord('A') + int(message[i:i+2]))])
    print(result)

if __name__ == '__main__':
    main()
