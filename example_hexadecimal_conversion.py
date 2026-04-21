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

print("'000' equals ", convert_hexa_to_decimal('000'))
print("'10' equals ", convert_hexa_to_decimal('10'))
print("'ABC' equals ", convert_hexa_to_decimal('ABC'))
print("'FDBECA' equals ", convert_hexa_to_decimal('FDBECA'))
