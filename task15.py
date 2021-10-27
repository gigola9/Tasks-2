numbs = [100, 44.5, 231, 8888, 7.81]

print('ჯამი ' + str(sum(numbs)))
print('მინიმალური ' + str(min(numbs)))
print('მაქსიმალური ' + str(max(numbs)))
print('საშუალო ' + str(sum(numbs) / len(numbs)))

numbs.append(102)
numbs[2] = 205
numbs.pop(3)
numbs.sort()
