def numbers(tmp):
    mult = 1
    for i in tmp:
        mult *= i
    return mult


dt = [1, 103, -21, -52, 100]
print(numbers(dt))
