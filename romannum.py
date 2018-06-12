num = int(input("Input number: "))

def roman_converter(n):
    num_values = [(1000000,'M'+ u'\u0304'),(900000,'C\u0304M\u0304'),(100000,'C'+ u'\u0304'),(90000,'X\u0304C\u0304'),(50000,'L'+ u'\u0304'),(40000,'X\u0304L\u0304'),(10000,'X'+ u'\u0304'),(5000,'V'+ u'\u0304'),(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                  (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman_num = " "
    while n > 0:
        for i, r in num_values:
            while n >= i:
                roman_num += r
                n -= i
    return roman_num

print(roman_converter(num))
