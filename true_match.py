from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

result = divide(49, 7)
print(result)
# result3 = divide(49, 7)
