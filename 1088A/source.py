def light_up(original, rebuild):
    hours = original
    if original // rebuild != 0:
        hours += light_up(original // rebuild, rebuild)
    return hours


def remaining(remainder, rebuild):
    hours = remainder // rebuild
    rm = remainder // rebuild
    if remainder // rebuild != 0 or rm :
        rm += remaining(rm // rebuild, rebuild)
    return rm


a, b = map(int, input().split())
residual = 0
a_c = a
while a // b != 0 or a % b != 0:
    residual += a % b
    a //= b
print(light_up(a_c, b) + remaining(residual, b))
