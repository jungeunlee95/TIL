def B(i):
    output = ""
    for j in range(15, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output[12:]

keys = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001' ,'101111']
# a = [0, 'D', 'E', 'C']
a = [0, 2, 6, 9, 'F', 'A', 'C', 9, 'A', 0]
result = ''
for i in a :
    if type(i) == int:
        result += B(i)
    else:
        c = ord(i) - ord('A') + 10
        result += B(c)
c = 0
for i in range(len(result)):
    if result[i:i+6] in keys:
        c = i
        break
for i in range(c, len(result), 6):
    if result[i:i+6] in keys:
        print(keys.index(result[i:i+6]), end=' ')
print()

