def difference(*args):
    if len(args) == 0:
        return 0
    else:
        max_number = max(args)
        min_number = min(args)
        return round(max_number - min_number, 2) #число, количество знаков,которое мы хотим оставить после запятой(если значение отрицательное,то перед запятой)
assert difference(1, 2, 3) == 2
assert difference(5, -5) == 10
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
assert difference() == 0
print('OK')