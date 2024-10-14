def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5, 7)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [True, 77, 'Space']
values_dict = {'a': 123, 'b': False, 'c': 'London'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [55, 'popcorn']
print_params(*values_list_2, 42)
