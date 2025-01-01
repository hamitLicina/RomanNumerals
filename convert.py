def int_to_roman(num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    result = ""
    
    for value, symbol in roman_numerals.items():
        while num >= value:
            result += symbol
            num -= value
    
    return result

# Test edelim
print(int_to_roman(1987))  # "MCMLXXXVII"

def roman_to_int(roman):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        current_value = roman_numerals[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

# Test edelim
print(roman_to_int("MCMLXXXVII"))  # 1987

def validate_roman_conversion():
    for num in range(1, 4001):
        roman = int_to_roman(num)
        converted_back = roman_to_int(roman)
        if num != converted_back:
            print(f"Error: {num} -> {roman} -> {converted_back}")
            return False
    print("All conversions are correct!")
    return True

# Test edelim
validate_roman_conversion()

# Programı çalıştır
if __name__ == "__main__":
    validate_roman_conversion()