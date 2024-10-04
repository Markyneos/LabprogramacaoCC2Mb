'''
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

LVIII - 58
MCMXCIV - 1994
'''

# def romanoEmInt(roman: str) -> int:
#     romanos = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     numero = 0
#     auxList = []

#     for i in range(len(roman)):
#         if roman[i] in romanos:
#             auxList.append(romanos[roman[i]])
#         else:
#             print("Algarismo romano inválido")
#     try:
#         for i in range(len(auxList)):
#             if auxList[i] < auxList[i + 1]:
#                 numero -= auxList[i]
#             else:
#                 numero += auxList[i]
#     except IndexError:
#         numero += auxList[i]
#     return numero

def romanoEmInt_v1(roman: str) -> int:
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    romano = list(roman)
    romano.reverse()
    result = 0
    previous = 0

    for char in romano:
        try:
            value = romans[char]
        except ValueError:
            print("Algarismo inválido")
        
        if value < previous:
            result -= value
        else:
            result += value

        previous = value
    return result

def romanToInt_v2(roman):
    roman_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    index = 0
    while index < len(roman):
        if roman_numbers[roman[index]] < roman_numbers[roman[index + 1]]:
            result += roman_numbers[roman[index + 1]] - roman_numbers[roman[index]]
            index += 2
        else:
            result += roman_numbers[roman[index]]
            index += 1
    return result







print(romanToInt_v2("XIV")) #14
print(romanToInt_v2(""))