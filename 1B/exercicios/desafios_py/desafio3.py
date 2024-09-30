# def isPalindrome(number: int) -> bool:
#     if number < 0:
#         return False
#     algarismos = [i for i in str(number)]
#     algarismos2 = algarismos.copy()

#     algarismos.reverse()

#     for i in range(len(algarismos)):
#         if algarismos[i] != algarismos2[i]:
#             return False
#     return True

def isPalindrome(number: int) -> bool:
    if number < 0:
        return False
    algarismos = []
    while number >= 1:
        resto = number % 10
        algarismos.append(resto)
        number = number // 10
    algarismos2 = algarismos.copy()
    algarismos.reverse()
    return algarismos == algarismos2


print(isPalindrome(10))
print(isPalindrome(101))
print(isPalindrome(-101))
