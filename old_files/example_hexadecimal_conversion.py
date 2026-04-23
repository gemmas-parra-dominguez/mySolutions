# Function convert_hex_to_decimal(input_value, base = 16) gets as input an hexadecimal code of type string or list, to be converted into a number of decimal base. The result is an integer positive number.
def convert_hex_to_decimal(input_value, base = 16):
    # dict_hexadecimal_numbers is a dictionary that maps the values of the hexadecimal system with their corresponding decimal system values.
    dict_hexadecimal_numbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

    # Only string or list are valid input data types.
    valid_input = (type(input_value) == str) or (type(input_value) == list)
    
    if not valid_input:
        # Return -1 if input isn't valid.
        print("Input isn't string or list, it's invalid!")
        return -1
    
    if (type(input_value) == list):
        # If input_value is a list, elements are combined in a single string.
        code = "".join(map(str, input_value))
    else:
        code = input_value
    # Get decimal value
    return get_decimal_value(code, dict_hexadecimal_numbers)

# Function get_decimal_value(code, hexNumbers, base = 16) gets as input an string representing an hexadecimal code to be converted into a decimal value.
def get_decimal_value(input_code, dict_hexadecimal_numbers, base = 16):
    # Initializing variables
    count = 0
    power = len(input_code) - 1

    # Iterate in the hex code to calculate the decimal value.
    for char in input_code:
        # Verify input characters are hex valid
        if char not in dict_hexadecimal_numbers:
            # Return -1 if character isn't valid.
            print(f'{char} is not a hex character!')
            return -1
        # Calculation is perfomed as (decimal value[0])*(base)^(n) + (decimal value[1])*(base)^(n-1) + (decimal value[2])*(base)^(n-2) + ...
        count += (dict_hexadecimal_numbers[char] * (base**power))
        power -= 1
    
    return count

def get_hex_value(input_value, base = 16):
    hexa_code = int(input_value % base)
    number = int(input_value / base)

    if (input_value < base):
        return str(int(input_value))

    if hexa_code == 0:
        if (number < base):
            return '0' + ',' + str(int(input_value / base))
        else:
            return '0' + ',' + get_hex_value(number)
    
    return str(hexa_code) + ',' + get_hex_value(number)
    
# Function map_to_hex_string(input_code, dict_hexadecimal_numbers) maps the input values to their corresponding hexadecimal character. The result is an string.
def map_to_hex_string(input_code, dict_hexadecimal_numbers):
    # Initializing variable
    hexa_code = ''

    # Iterate in the input code to map the correct hex value
    for code in range(0,len(input_code)):
        if input_code[code] not in dict_hexadecimal_numbers:
            # Verify each code has a correspondig hex character
            print(f'{input_code[code]} is not a hex character!')
            # Return empty character if code isn't found.
            return ''
        # Append the character to the string        
        hexa_code += dict_hexadecimal_numbers[input_code[code]]
    
    return hexa_code

def get_hexa_code(input_value, dict_hexadecimal_numbers):
    # 1. Analyze the units, tens, hundreds, etc. of input value to obtain its corresponding value in a system based 16.
    # 2. Split the output string into a list of strings.
    # 3. Reverse the order of the list from [LSB ... MSB] to [MSB ... LSB]
    code = get_hex_value(input_value).split(',')[::-1]
    # Map the computed list of string to its corresponding hexadecimal character.
    return map_to_hex_string(code, dict_hexadecimal_numbers)

# Function convert_decimal_to_hex(input_value, base = 16) gets as input a positive number of type int, floar, string or list value, to be converted into an hexadecimal base code, the result is an string.
def convert_decimal_to_hex(input_value, base = 16):
    # dict_hexadecimal_numbers is a dictionary that maps the values of the decimal system with their corresponding hexadecimal system characters.
    dict_hexadecimal_numbers = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F' }
    
    # Only int, float, string or list are valid input data types.
    valid_input = (type(input_value) == int) or (type(input_value) == float) or (type(input_value) == str) or (type(input_value) == list)

    if not valid_input:
        # Return -1 if input isn't valid.
        print("Input data type is invalid!")
        return -1
    
    if (type(input_value) == str) or (type(input_value) == float):
        # If input_value is an string or float, it's converted to int.
        value = int(input_value)
        print("Input isn't an integer number, it is converted to ", value)
    elif type(input_value) == list:
        # If input_value is a list, elements are combined in a single string.
        value_str = "".join(map(str, input_value))
        # Then, it's converted to int.
        value = int(value_str)
    else:
        value = input_value 

    # Get hexadecimal code   
    return get_hexa_code(value, dict_hexadecimal_numbers)

# Converting Hexadecimal to Decimal
print("Hexadecimal '000' equals decimal ", convert_hex_to_decimal('000'))
print("Hexadecimal '10' equals decimal ", convert_hex_to_decimal('10'))
print("Hexadecimal 'ABC' equals decimal ", convert_hex_to_decimal('ABC'))
print("Hexadecimal ['A','B', 0] equals decimal ", convert_hex_to_decimal(['A','B', 0]))
print("Hexadecimal ['F','D','B','E','C','A'] equals decimal ", convert_hex_to_decimal(['F','D','B','E','C','A']))
print("Hexadecimal ['F','H','0'] equals decimal ", convert_hex_to_decimal(['F','H','0']))
print("\n")
print("Decimal 10 equals hexadecimal", convert_decimal_to_hex(10))
print("Decimal 15 equals hexadecimal", convert_decimal_to_hex(15))
print("Decimal '16' equals hexadecimal", convert_decimal_to_hex('16'))
print("Decimal 64 equals hexadecimal", convert_decimal_to_hex(64))
print("Decimal [1,1,2] equals hexadecimal", convert_decimal_to_hex([1,1,2]))
print("Decimal 200 equals hexadecimal", convert_decimal_to_hex(200))
print("Decimal 20000 equals hexadecimal", convert_decimal_to_hex(20000))
