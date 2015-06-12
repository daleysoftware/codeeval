import sys

# Input logic.
line_reader = open(sys.argv[1], 'r')
lines = []
for line in line_reader:
    line = line.strip()
    lines.append(line)
line_reader.close()

# First line and initialization.
checkpoint = lines[0].find('C')
position = lines[0].find('_') if checkpoint == -1 else checkpoint
temp = list(lines[0])
temp[position] = '|'
print(''.join(temp))
previous_position = position

# All other lines.
for i in range(1, len(lines)):
    line = lines[i]
    checkpoint = line.find('C')
    if checkpoint != -1 and abs(checkpoint - previous_position) <= 1:
        position = checkpoint
    else:
        position = line.find('_')
    # Need to modify the python string == annoying.
    temp = list(line)
    if position < previous_position:
        temp[position] = '/'
    elif position == previous_position:
        temp[position] = '|'
    else:
        temp[position] = '\\'
    previous_position = position
    print(''.join(temp))
