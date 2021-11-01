def chck(dt):
    mx = 0
    num = 0

    for i in dt:
        currMax = dt.count(i)
        if currMax > mx:
            mx = currMax
            num = i
    print(f'ყველაზე ხშირად განმეორებადი რიცხვია {num}')
    print(f'რაოდენობა: {mx}')


tmp = [1, 5, 23, 5, 12, 2, 5, 1, 18, 5]
chck(tmp)
