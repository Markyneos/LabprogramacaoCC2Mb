'''
Data types
- Text: str
- Numerics: int, float, complex
- Sequences: : list, tuple, range
- Mapping: dict
- Set: set, frozenset
- boolean: bool (True, False)
- Bynary: bytes, bytearray, memoryview
- none: NonoType
'''

x = ['Wagner', 'Carlos', 'José']
print(type(x))
x = ('Wagner', 'Carlos', 'José')
print(type(x))
x = ('Wagner', 1)
print(type(x))
print(x)

x = 3+2j
y = 2j
z = -2j
a = x + y

print(a)