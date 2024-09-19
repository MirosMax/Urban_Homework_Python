calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_param = len(string), string.upper(), string.lower()
    return string_param


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()

    if string.lower() in list_to_search:
        flag = True
    return flag


print(string_info('Welcome to the real world'))
print(string_info('Hakuna Matata'))
print(string_info('World Peace'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
