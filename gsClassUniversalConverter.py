
class GsUniversalConverter:
    _dict_decimal_to_hexadecimal = {
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
    '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F' }

    _dict_hexadecimal_to_decimal = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

    _dict_bin_to_decimal = {'0': 0, '1': 1}

    _dict_decimal_to_bin = {0: '0', 1: '1'}

    _conversion_options = ['hex_to_decimal', 'decimal_to_hex', 'bin_to_decimal', 'decimal_to_bin', 'octal_to_decimal', 'decimal_to_octal']

    def __init__(self):
        pass

    def input_verification(self, input_data, convert_opt):
        # Options verification
        if not input_data:
            print("Input data is empty.")
            return False
        if not ((type(input_data) == str) or (type(input_data) == list) or (type(input_data) == int) or (type(input_data) == float)):
            print("Input data isn't supported")
            return False

        if not convert_opt in self._conversion_options:
            print("Conversion option is invalid.")
            return False
        
        return True

    def get_conversion(self, input_data='', convert_opt = ''):
        if not self.input_verification(input_data, convert_opt):
            return -1
        # Select correct function  
        # _conversion_options = ['hex_to_decimal', 'decimal_to_hex', 'bin_to_decimal', 'decimal_to_bin', 'octal_to_decimal', 'decimal_to_octal']      
        if convert_opt == self._conversion_options[0]:
            return self.convert_hex_to_decimal(input_data)
        elif convert_opt == self._conversion_options[1]:
            return self.convert_decimal_to_hex(input_data)
        elif convert_opt == self._conversion_options[2]:
            return self.convert_binary_to_decimal(input_data)
        elif convert_opt == self._conversion_options[3]:
            return self.convert_decimal_to_binary(input_data)
        elif convert_opt == self._conversion_options[4]:
            return -1
        elif convert_opt == self._conversion_options[5]:
            return -1
        else:
            print("Conversion option is invalid.")
            return -1
    
    def convert_binary_to_decimal(self, input_code):
        base = 2               
        # Transform any valid data type into a string before processing
        if (type(input_code) == int):
            # If input_code is an int, it's converted to str.
            value = str(input_code)
        elif (type(input_code) == float):
            # If input_code is a float, it's converted to str.
            value = str(int(input_code))
            print(f"Input {value} isn't an int, it is converted to ", value)
        elif type(input_code) == list:
            # If input_code is a list, elements are combined in a single string.
            value = "".join(map(str, input_code))
        else:
            value = input_code

        return self.get_decimal_value(value, self._dict_bin_to_decimal, base)

    # CHECK
    def get_binary_code(self, input_value, dict_bin_chats):
        base = 2
        # Initializing variables
        remainder = input_value % base
        value = int(input_value / base)
        # If quotient eauqls 0, conversion is over.
        if (value == 0):
            return '1'
        # Recursively, divide the input value by the base, obtain its corresponding binary character, add it to the code.
        return dict_bin_chats[remainder] + self.get_binary_code(value, dict_bin_chats)

    # CHECK
    def convert_decimal_to_binary(self, input_value):
        base = 2
        
        if (type(input_value) == str) or (type(input_value) == float):
            # If input_value is an string or float, it's converted to int.
            value = int(input_value)
            print(f"Input {input_value} isn't int, it is converted to ", value)
        elif type(input_value) == list:
            # If input_value is a list, elements are combined in a single string.
            value_str = "".join(map(str, input_value))
            # Then, it's converted to int.
            value = int(value_str)
        else:
            value = input_value 
        
        if (value < base):
            return self._dict_decimal_to_bin[value]
        
        # Reverse the order of the list from [LSB ... MSB] to [MSB ... LSB]
        return self.get_binary_code(value, self._dict_decimal_to_bin)[::-1]

    # CHECK
    def convert_hex_to_decimal(self, input_value):
        base = 16

        # Only string or list are valid input data types.
        valid_input = (type(input_value) == str) or (type(input_value) == list)
        
        if not valid_input:
            # Return -1 if input isn't valid.
            print(f"Input {input_value} isn't string or list, it's invalid!")
            return -1
        
        if (type(input_value) == list):
            # If input_value is a list, elements are combined in a single string.
            code = "".join(map(str, input_value))
        else:
            code = input_value
        # Get decimal value
        return self.get_decimal_value(code, self._dict_hexadecimal_to_decimal, base)

    # CHECK
    def get_decimal_value(self, input_code='', dict_base_chars='', base = 2):
        # Initializing variables
        count = 0
        power = len(input_code) - 1

        # Iterate in the hex code to calculate the decimal value.
        for char in input_code:
            # Verify input characters are hex valid
            if char not in dict_base_chars:
                # Return -1 if character isn't valid.
                print(f'{char} is not a valid character!')
                return -1
            # Calculation is perfomed as (decimal value[0])*(base)^(n) + (decimal value[1])*(base)^(n-1) + (decimal value[2])*(base)^(n-2) + ...
            count += (dict_base_chars[char] * (base**power))
            power -= 1
        
        return count

    # CHECK
    def get_hex_value(self, input_value):
        base = 16
        hexa_code = int(input_value % base)
        number = int(input_value / base)

        if (input_value < base):
            return str(int(input_value))

        if hexa_code == 0:
            if (number < base):
                return '0' + ',' + str(int(input_value / base))
            else:
                return '0' + ',' + self.get_hex_value(number)
        
        return str(hexa_code) + ',' + self.get_hex_value(number)
    
    # CHECK
    def map_to_hex_string(self, input_code, dict_hexadecimal_chars):
        # Initializing variable
        hexa_code = ''

        # Iterate in the input code to map the correct hex value
        for code in range(0,len(input_code)):
            if input_code[code] not in dict_hexadecimal_chars:
                # Verify each code has a correspondig hex character
                print(f'{input_code[code]} is not a hex character!')
                # Return empty character if code isn't found.
                return ''
            # Append the character to the string        
            hexa_code += dict_hexadecimal_chars[input_code[code]]
        
        return hexa_code
    
    #CHECK
    def get_hexa_code(self, input_value, dict_hexadecimal_chars):
        # 1. Analyze the units, tens, hundreds, etc. of input value to obtain its corresponding value in a system based 16.
        # 2. Split the output string into a list of strings.
        # 3. Reverse the order of the list from [LSB ... MSB] to [MSB ... LSB]
        code = self.get_hex_value(input_value).split(',')[::-1]
        # Map the computed list of string to its corresponding hexadecimal character.
        return self.map_to_hex_string(code, dict_hexadecimal_chars)

    # CHECK
    def convert_decimal_to_hex(self, input_value):
        base = 16
                
        # Only int, float, string or list are valid input data types.
        valid_input = (type(input_value) == int) or (type(input_value) == float) or (type(input_value) == str) or (type(input_value) == list)

        if not valid_input:
            # Return -1 if input isn't valid.
            print("Input data type is invalid!")
            return -1
        
        if (type(input_value) == str) or (type(input_value) == float):
            # If input_value is an string or float, it's converted to int.
            value = int(input_value)
            print(f"Input {input_value} isn't int, it is converted to ", value)
        elif type(input_value) == list:
            # If input_value is a list, elements are combined in a single string.
            value_str = "".join(map(str, input_value))
            # Then, it's converted to int.
            value = int(value_str)
        else:
            value = input_value 

        # Get hexadecimal code   
        return self.get_hexa_code(value, self._dict_decimal_to_hexadecimal)
