def roman_v1(ch):
    M= ch.count('M')
    D= ch.count('D')
    C= ch.count('C')
    X= ch.count('X')
    V= ch.count('V')
    I= ch.count('I')
    return (M*1000 + D*500 + C*100 + X*10 + V*5 + I)

def roman_v2(ch):
    count = 0
    for i in ch:
        if i == 'M':
            count += 1000
        elif i == 'D':
            count += 500
        elif i == 'C':
            count += 100
        elif i == 'X':
            count += 10
        elif i == 'V':
            count += 5
        elif i == 'I':
            count += 1
    return count


ch = input("Input a roman number using letters M, D, C, X and I: ")
print(roman_v1(ch))
print(roman_v2(ch))
