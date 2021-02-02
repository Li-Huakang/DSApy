def toString(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return toString(num//base, base) + convertString[num % base]

print(toString(769, 16))