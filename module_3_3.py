def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [3.14, 'list', 3]
values_dict = {'a': 3, 'b': 'абзац', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [22.2, 'жесть']

print_params(*values_list_2)
print_params(*values_list_2,42)