def bin_to_dec(decimal_numer):
    decimal_numer = str(decimal_numer)
    d_len = len(decimal_numer)
    sum = 0
    for x in range(d_len):
        sum +=(2**((d_len - 1) - x) * int(decimal_numer[x]))
    return sum
    
def dec_to_bin(binary_number):
    sum = ''
    while(binary_number > 0):
        sum += str(binary_number % 2)
        binary_number //= 2
    return int(sum[::-1])
    
hex_table = {0 : '0', 1: '1', 2 : '2', 3 : '3', 4 : '4',
             5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',
             10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',
             14 : 'E', 15 : 'F'}
             
def hex_to_dec(hex_number):
    h_len = len(hex_number)
    sum = 0
    for x in range(h_len):
        key_list = list(hex_table.keys())
        val_list = list(hex_table.values())
        key_from_value = val_list.index(hex_number[x].upper())
        sum +=(16**((h_len - 1) - x) * key_list[key_from_value])
    return int(sum)

def dec_to_hex(decimal_number):
    hex_value = ''
    while(decimal_number > 0):
        hex_value += hex_table[decimal_number % 16]
        decimal_number //= 16
    return hex_value[::-1]
