s = 'python php pascal javascript java c++'
tmp = s.split(' ')

maxCount = 0
result = ''

for i in tmp:
    if len(i) > maxCount:
        maxCount = len(i)
        result = i

print(result)