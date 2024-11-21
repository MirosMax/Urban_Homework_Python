def is_prime(func):
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        flag = 'Простое'
        if result_func > 1:
            for i in range(2, result_func):
                if result_func % i == 0:
                    flag = 'Составное'
        else:
            flag = 'Составное'
        print(flag)
        return result_func
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
