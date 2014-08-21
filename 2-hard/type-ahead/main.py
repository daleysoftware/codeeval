import sys
import collections

# Provided in the problem description; hard coded.
TEXT_ARRAY = ['Mary', 'had', 'a', 'little', 'lamb', 'its', 'fleece', 'was',
              'white', 'as', 'snow', 'And', 'everywhere', 'that', 'Mary',
              'went', 'the', 'lamb', 'was', 'sure', 'to', 'go', 'It',
              'followed', 'her', 'to', 'school', 'one', 'day', 'which', 'was',
              'against', 'the', 'rule', 'It', 'made', 'the', 'children',
              'laugh', 'and', 'play', 'to', 'see', 'a', 'lamb', 'at', 'school',
              'And', 'so', 'the', 'teacher', 'turned', 'it', 'out', 'but',
              'still', 'it', 'lingered', 'near', 'And', 'waited', 'patiently',
              'about', 'till', 'Mary', 'did', 'appear', 'Why', 'does', 'the',
              'lamb', 'love', 'Mary', 'so', 'the', 'eager', 'children', 'cry',
              'Why', 'Mary', 'loves', 'the', 'lamb', 'you', 'know', 'the',
              'teacher', 'did', 'reply']

#TEXT_ARRAY = [t.lower() for t in TEXT_ARRAY]

def build_index(text_array, n):
    index = collections.defaultdict(dict)
    for i in xrange(len(text_array)-n):
        key = ' '.join(text_array[i:i+n])
        # Add this word to the index. Keep a word count.
        word = text_array[i+n]
        if word in index[key]:
            index[key][word] += 1
        else:
            index[key][word] = 1
    return index

def main():
    indexes = {}
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            n = int(test.strip().split(',')[0])-1
            search = test.strip().split(',')[1]
            # Build the index for this n-gram length if we haven't already.
            if n not in indexes: indexes[n] = build_index(TEXT_ARRAY, n)
            # Format the indexed result and print.
            result = indexes[n][search].items()
            total = sum(indexes[n][search].values())
            result.sort(key=lambda tup: tup[0])
            result.sort(key=lambda tup: tup[1], reverse=True)
            formatted_output = []
            for t in result:
                p = float(t[1])/total
                formatted_output.append(t[0] + ',' + ("%.3f" % p))
            print ';'.join(formatted_output)

if __name__ == '__main__':
    main()