# Converting Hexadecimal to Decimal

def convert_hexa_to_decimal(code, base = 16):
    hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

    if type(code) != str:
        print("Conversion wasn't possible!")
        return -1
    
    count = 0
    power = len(code) - 1
    for char in code:
        if char not in hexNumbers:
            print(f'{char} is not a hex character!')
        count = count + (hexNumbers[char] * (base**power))
        power = power - 1

    return count

def get_hexa_value_string(value, base = 16):
    hexa_code = int(value % base)
    number = int(value / base)

    if (value < base):
        return str(int(value))

    if hexa_code == 0:
        if (number < base):
            return '0' + ',' + str(int(value / base))
        else:
            return '0' + ',' + get_hexa_value_string(number)
    
    return str(hexa_code) + ',' + get_hexa_value_string(number)
    
def map_to_hexa_string(code, hexNumbers):
    hexa_code = ''
    for word in range(0,len(code)):
        if code[word] not in hexNumbers:
            print(f'{code[word]} is not a hex character!')
        hexa_code = hexa_code + hexNumbers[code[word]]
    
    return hexa_code

def get_hexa_code_list(value):
    code = get_hexa_value_string(value)
    return  code.split(',')[::-1]

def convert_decimal_to_hexa(input, base = 16):
    hexNumbers = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F' }
    
    value = int(input)
    if type(input) != int:
        print("Input isn't an integer number, it is converted to ", value)
    # Case value is in [0, 15]
    if (value < base):
        return hexNumbers[str(value)]
    else:
        code = get_hexa_code_list(value)

    return map_to_hexa_string(code, hexNumbers)


print("'000' equals ", convert_hexa_to_decimal('000'))
print("'10' equals ", convert_hexa_to_decimal('10'))
print("'ABC' equals ", convert_hexa_to_decimal('ABC'))
print("'FDBECA' equals ", convert_hexa_to_decimal('FDBECA'))
print(convert_decimal_to_hexa(10))
print(convert_decimal_to_hexa(15))
print(convert_decimal_to_hexa(16))
print(convert_decimal_to_hexa(64))
print(convert_decimal_to_hexa(112))
print(convert_decimal_to_hexa(200))
print(convert_decimal_to_hexa(20000))
