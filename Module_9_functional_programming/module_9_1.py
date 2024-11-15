def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([1, 2, 3, 4, 5, 6, 7], max, min))
print(apply_all_func([5, 2, 99, 4, 77, 6, 1], max, min, len, sum, sorted))
