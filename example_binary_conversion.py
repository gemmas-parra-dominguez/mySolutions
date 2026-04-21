# Converting Hexadecimal to Decimal

def convert_binary_to_decimal(code, base = 2):
    binNumbers = {'0': 0, '1': 1}

    if type(code) != str:
        print("Conversion wasn't possible!")
        return -1
    
    count = 0
    power = len(code) - 1
    for char in code:
        if char not in binNumbers:
            print(f'{char} is not a hex character!')
        count = count + (binNumbers[char] * (base**power))
        power = power - 1

    return count

print("'000' equals ", convert_binary_to_decimal('000'))
print("'010' equals ", convert_binary_to_decimal('010'))
print("'111' equals ", convert_binary_to_decimal('111'))
print("'10000' equals ", convert_binary_to_decimal('10000'))
