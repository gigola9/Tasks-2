numbs = [100, 44.5, 231, 8888, 7.81]

print(sum(numbs))
print(min(numbs))
print(max(numbs))
print(sum(numbs) / len(numbs))

numbs.append(102)
numbs[2] = 205
numbs.pop(3)
numbs.sort()
print(numbs)
