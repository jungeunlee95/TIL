def B(i):
    output = ""
    for j in range(15, -1, -1):
        output += "1" if i & (1 << j) else "0"
    return output[12:]

# a = [0,'F',9,7,'A',3]
a = [0,1,'D',0,6,0,7,9,8,6,1,'D',7,9,'F',9,9,'F']
result = ''
for i in a :
    if type(i) == int:
        result += B(i)
    else:
        c = ord(i) - ord('A') + 10
        result += B(c)

a = result
b = []
for i in range(0,len(a),7):
    b.append(a[i:i+7][::-1])
result = [0] * len(b)
for i in range(len(b)):
    for j in range(len(b[i])):
        if j==0 and b[i][j] == '1':
                result[i] += 1
        elif b[i][j] == '1':
            result[i] += 2**j
print(' '.join(map(str,result)))
