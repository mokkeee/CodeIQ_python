columns_num = input().strip().count(',') + 1
columns = [set() for col in range(columns_num)]

try:
    while True:
        line = input().strip()
        for (val, column) in zip(line.split(','), columns):
            column.add(val)
except EOFError:
    print(','.join([str(len(c)) for c in columns]))
