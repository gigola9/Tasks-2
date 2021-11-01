def rem(tmp):
    return list(filter(lambda m: m % 2 == 0, tmp))


dt = [1, 103, 86, 77, 100]
print(rem(dt))
