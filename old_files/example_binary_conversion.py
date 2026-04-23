# Converting Binary to Decimal

def convert_binary_to_decimal(input_code, base = 2):
    dict_bin_numbers = {'0': 0, '1': 1}

    # Only string or list are valid input data types.
    valid_input = (type(input_code) == str) or (type(input_code) == list) or (type(input_code) == int)
    
    if not valid_input:
        # Return -1 if input isn't valid.
        print("Input isn't string or list, it's invalid!")
        return -1
    
    # Transform any valid data type into a string before processing
    if (type(input_code) == int):
        # If input_code is an int or float, it's converted to str.
        value = str(input_code)
        print("Input isn't an string, it is converted to ", value)
    elif type(input_code) == list:
        # If input_code is a list, elements are combined in a single string.
        value = "".join(map(str, input_code))
    else:
        value = input_code 
    
    # Initializing variables
    count = 0
    power = len(value) - 1
    # Calculate the corresponding decimal value
    for char in value:
        if char not in dict_bin_numbers:
            print(f'{char} is not a binary character!')
        # Calculation is perfomed as (binary value[0])*(base)^(n) + (binary value[1])*(base)^(n-1) + (binary value[2])*(base)^(n-2) + ...
        count += (dict_bin_numbers[char] * (base**power))
        power -= 1
    return count

def get_binary_code(input_value, dict_bin_numbers, base = 2):
    # Initializing variables
    remainder = input_value % base
    value = int(input_value / base)
    # If quotient eauqls 0, conversion is over.
    if (value == 0):
        return '1'
    # Recursively, divide the input value by the base, obtain its corresponding binary character, add it to the code.
    return dict_bin_numbers[remainder] + get_binary_code(value, dict_bin_numbers)


def convert_decimal_to_binary(input_value, base = 2):
    # dict_bin_numbers is a dictionary that maps the values of the decimal system with their corresponding binary system characters.
    dict_bin_numbers = {0: '0', 1: '1'}

    # Only string or list are valid input data types.
    valid_input = (type(input_value) == int) or (type(input_value) == float) or (type(input_value) == str) or (type(input_value) == list)
    
    if not valid_input:
        # Return -1 if input isn't valid.
        print("Input isn't string or list, it's invalid!")
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
    
    if (value < base):
        return dict_bin_numbers[value]
    
    # Reverse the order of the list from [LSB ... MSB] to [MSB ... LSB]
    return get_binary_code(value, dict_bin_numbers)[::-1]

print("Hexadecimal '000' equals ", convert_binary_to_decimal('000'))
print("Hexadecimal '010' equals ", convert_binary_to_decimal('010'))
print("Hexadecimal 111 equals ", convert_binary_to_decimal(111))
print("Hexadecimal '111' equals ", convert_binary_to_decimal('111'))
print("Hexadecimal ['1','0','0','0,'0'] equals ", convert_binary_to_decimal(['1','0','0','0','0']))
print("\n")
print("Decimal 0 equals ", convert_decimal_to_binary(0))
print("Decimal 10 equals ", convert_decimal_to_binary(10))
print("Decimal '166' equals ", convert_decimal_to_binary('166'))
print("Decimal [1, 6, 6] equals ", convert_decimal_to_binary([1, 6, 6]))
