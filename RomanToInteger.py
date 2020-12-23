string = "XVII"
dictionary = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
              'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

length = len(string)
sum = 0
idx = 0

while idx < len(string):
    if string[idx:idx+2] in dictionary:
        sum += dictionary[string[idx:idx+2]]
        idx += 2
    else:
        sum += dictionary[string[idx]]
        idx += 1
print(sum)