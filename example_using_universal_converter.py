import gsClassUniversalConverter as gsConverter

obj = gsConverter.GsUniversalConverter(True)
obj()
conversion_opts = obj._conversion_options = ['hex_to_decimal', 'decimal_to_hex', 'bin_to_decimal', 'decimal_to_bin', 'octal_to_decimal', 'decimal_to_octal', 'not_supported']
binary_test_batch = ['000', '101012', 111, '111', [1, '1', '1'], ['1','0','0','0','0']]
hexadecimal_test_batch = ['010', 'AB0', ['A','B', 0], ['F','D','B','E','C','A'], 'FH0', ['F','H','0']]
decimal_test_batch = [10, 16, '16', [1,6], 64, 128.5, 20000]
octal_test_batch = [10, '10', ['1', '0'], 8, '18', 100, 107]

# Converting Hexadecimal to Decimal
print(f"Hexadecimal {hexadecimal_test_batch[0]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[0], conversion_opts[0]))
print(f"Hexadecimal {hexadecimal_test_batch[1]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[1], conversion_opts[0]))
print(f"Hexadecimal {hexadecimal_test_batch[2]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[2], conversion_opts[0]))
print(f"Hexadecimal {hexadecimal_test_batch[3]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[3], conversion_opts[0]))
print(f"Hexadecimal {hexadecimal_test_batch[4]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[4], conversion_opts[0]))
print(f"Hexadecimal {hexadecimal_test_batch[5]} equals decimal ", obj.get_conversion(hexadecimal_test_batch[5], conversion_opts[0]))
print("\n")
# Converting Decimal to Hexadecimal
print(f"Decimal {decimal_test_batch[0]} equals hexadecimal", obj.get_conversion(decimal_test_batch[0], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[1]} equals hexadecimal", obj.get_conversion(decimal_test_batch[1], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[2]} equals hexadecimal", obj.get_conversion(decimal_test_batch[2], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[3]} equals hexadecimal", obj.get_conversion(decimal_test_batch[3], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[4]} equals hexadecimal", obj.get_conversion(decimal_test_batch[4], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[5]} equals hexadecimal", obj.get_conversion(decimal_test_batch[5], conversion_opts[1]))
print(f"Decimal {decimal_test_batch[6]} equals hexadecimal", obj.get_conversion(decimal_test_batch[6], conversion_opts[1]))
print("\n")
# Converting Binary to Decimal
print(f"Binary {binary_test_batch[0]} equals decimal ", obj.get_conversion(binary_test_batch[0], conversion_opts[2]))
print(f"Binary {binary_test_batch[1]} equals decimal ", obj.get_conversion(binary_test_batch[1], conversion_opts[2]))
print(f"Binary {binary_test_batch[2]} equals decimal ", obj.get_conversion(binary_test_batch[2], conversion_opts[2]))
print(f"Binary {binary_test_batch[3]} equals decimal ", obj.get_conversion(binary_test_batch[3], conversion_opts[2]))
print(f"Binary {binary_test_batch[4]} equals decimal ", obj.get_conversion(binary_test_batch[4], conversion_opts[2]))
print(f"Binary {binary_test_batch[5]} equals decimal ", obj.get_conversion(binary_test_batch[5], conversion_opts[2]))
print("\n")
# Converting Decimal to Binary
print(f"Decimal {decimal_test_batch[0]} equals binary", obj.get_conversion(decimal_test_batch[0], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[1]} equals binary", obj.get_conversion(decimal_test_batch[1], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[2]} equals binary", obj.get_conversion(decimal_test_batch[2], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[3]} equals binary", obj.get_conversion(decimal_test_batch[3], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[4]} equals binary", obj.get_conversion(decimal_test_batch[4], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[5]} equals binary", obj.get_conversion(decimal_test_batch[5], conversion_opts[3]))
print(f"Decimal {decimal_test_batch[6]} equals binary", obj.get_conversion(decimal_test_batch[6], conversion_opts[3]))
print("\n")
# Converting Octal to Decimal
print(f"Octal {octal_test_batch[0]} equals decimal ", obj.get_conversion(octal_test_batch[0], conversion_opts[4]))
print(f"Octal {octal_test_batch[1]} equals decimal ", obj.get_conversion(octal_test_batch[1], conversion_opts[4]))
print(f"Octal {octal_test_batch[2]} equals decimal ", obj.get_conversion(octal_test_batch[2], conversion_opts[4]))
print(f"Octal {octal_test_batch[3]} equals decimal ", obj.get_conversion(octal_test_batch[3], conversion_opts[4]))
print(f"Octal {octal_test_batch[4]} equals decimal ", obj.get_conversion(octal_test_batch[4], conversion_opts[4]))
print(f"Octal {octal_test_batch[5]} equals decimal ", obj.get_conversion(octal_test_batch[5], conversion_opts[4]))
print(f"Octal {octal_test_batch[6]} equals decimal ", obj.get_conversion(octal_test_batch[6], conversion_opts[4]))
print("\n")
# Converting Decimal to octal
print(f"Decimal {decimal_test_batch[0]} equals octal", obj.get_conversion(decimal_test_batch[0], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[1]} equals octal", obj.get_conversion(decimal_test_batch[1], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[2]} equals octal", obj.get_conversion(decimal_test_batch[2], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[3]} equals octal", obj.get_conversion(decimal_test_batch[3], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[4]} equals octal", obj.get_conversion(decimal_test_batch[4], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[5]} equals octal", obj.get_conversion(decimal_test_batch[5], conversion_opts[5]))
print(f"Decimal {decimal_test_batch[6]} equals octal", obj.get_conversion(decimal_test_batch[6], conversion_opts[5]))
print("\n")
print("Not supported conversion", obj.get_conversion(decimal_test_batch[0], conversion_opts[6]))