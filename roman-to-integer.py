
def romanToInt(s):
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    roman = {
        "I": 1,
        "V": 2,
        "X": 3,
        "L": 4,
        "C": 5,
        "D": 6,
        "M": 7 
    }
    result = 0

    i = 0
    while i < len(s) - 1:
        current_char = s[i]
        next_char = s[i+1]

        # if i == len(s) - 2:
        #     print("1")
        #     result += numbers[roman[next_char] - 1]
        print(f"CURRENT_CHAR: {current_char}")
        print(f"NEXT_CHAR: {next_char}")
        if roman[next_char] % 2 == 1 and roman[next_char] - roman[current_char] == (1 or 2):
            print("1")
            result += numbers[roman[next_char] - 1] - numbers[roman[current_char] - 1]
        else:
            print(2)
            result += numbers[roman[current_char] - 1]

        i += 1
    
    print(result)
    return result
    
romanToInt("IV")