tmp = [1, 103, 86, 77, 100]
i = 0

while i < len(tmp):
    if tmp[i] % 2 == 1:
        tmp.pop(i)
    else:
        i += 1

print(tmp)
