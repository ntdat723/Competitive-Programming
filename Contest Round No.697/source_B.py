def solve(number):
    flag_x = False
    flag_y = False
    y = 0
    x = 0
    while number >= 2020 or number >= 2021:
        while not flag_x:
            r1 = (number - 2021*y)/2020
            if r1.is_integer():
                flag_x = True
            elif r1 < 1:
                break
            else:
                y += 1

        while not flag_y:
            r2 = (number - 2020*x)/2021
            if r2.is_integer():
                flag_y = True
            elif r2 < 1:
                break
            else:
                x += 1

        if flag_x or flag_y:
            return True
        else:
            return False
    return False


n = int(input())
cases = []
for i in range(n):
    num = int(input())
    cases.append(num)

res = []
for index in range(n):
    if solve(cases[index]):
        res.append(True)
    else:
        res.append(False)

for result in range(len(res)):
    if res[result]:
        print("YES")
    else:
        print("NO")