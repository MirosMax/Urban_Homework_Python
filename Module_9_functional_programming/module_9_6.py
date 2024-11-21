def all_variants(text):
    for i in range(1, len(text) + 1):
        start_index = 0
        end_index = start_index + i
        while len(text[start_index:end_index]) == i:
            yield text[start_index:end_index]
            start_index += 1
            end_index += 1


a = all_variants('abc')
for i in a:
    print(i)
