tmp = [1, 2, 3, 4, 4, 6, 11, 7, 8, 9]
tmp.sort()
dic = {}
print(tmp)

for i in tmp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

if len(dic) == len(tmp):
    print('სიას არ გააჩნია მოდა')
else:
    mx = 0
    res = []
    for i in dic.keys():
        if dic[i] > mx:
            mx = dic[i]
            res.clear()
            res.append(i)
        elif dic[i] == mx:
            res.append(i)
    print(f'მოდა არის {res}')

print(f'საშუალო არითმეტიკული {sum(tmp) / len(tmp)}')
print(f'მედიანა {(tmp[4] + tmp[5]) / 2}')

