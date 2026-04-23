import gsClassUniversalConverter as gsConverter

obj = gsConverter.GsUniversalConverter()
conversion_opts = obj._conversion_options = ['hex_to_decimal', 'decimal_to_hex', 'bin_to_decimal', 'decimal_to_bin', 'octal_to_decimal', 'decimal_to_octal']
binary_test_batch = []
hexadecimal_test_batch = ['010', 'AB0', ['A','B', 0], ['F','D','B','E','C','A'], 'FH0', ['F','H','0']]
decimal_test_batch = [10, 16, '16', [1,6], 64, 128.5, 20000]

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