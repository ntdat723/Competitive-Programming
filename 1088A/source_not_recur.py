a, b = map(int, input().split())
hours = a
remainder = 0
made = 0
while a >= b:
    if a - b >= 0:
        a -= b
        hours += 1
        made += 1
    else:
        hours += a
        break
    if made == b:
        hours += 1
        made = 1
made += a
while made >= b:
    if made - b >= 0:
        made -= b
        hours += 1
        made += 1

print(hours)