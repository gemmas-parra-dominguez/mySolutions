
class GsUniversalConverter:
    _dict_decimal_to_hexadecimal = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

    _dict_hexadecimal_to_decimal = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

    _dict_bin_to_decimal = {'0': 0, '1': 1}

    _dict_decimal_to_bin = {0: '0', 1: '1'}

    _conversion_options = ['hex_to_decimal', 'decimal_to_hex', 'bin_to_decimal', 'decimal_to_bin', 'octal_to_decimal', 'decimal_to_octal']

    _valid_bases = [2, 8, 10, 16]


    def __init__(self):
        pass

    def input_verification(self, input_data, convert_opt, conversion_base):
        # Options verification
        if not input_data:
            print("Input data is empty.")
            return False
        
        if not convert_opt in self._conversion_options:
            print("Conversion option is invalid.")
            return False
        
        if not conversion_base in self._valid_bases:
            print("Base is invalid.")
            return False
        return True

    def get_conversion(self, input_data='', convert_opt = '', conversion_base=2):
        if not self.input_verification(input_data, convert_opt, conversion_base):
            return -1
        
