def bin_to_str(input_bin):
    input_len = len(input_bin)
    bin_list = [input_bin[x:y] for x, y in zip(range(0, input_len - 8, 8), range(8, input_len, 8)) ]
    output = ''.join([chr(int(bin, 2)) for bin in bin_list])
    return output
        

try:
    while True:
        print(bin_to_str(input().strip()))
except EOFError:
    pass
