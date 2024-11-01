class WordsFinder:
    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for element in self.file_names:
            with open(element, encoding='utf-8') as file:
                words_file = []
                for line in file:
                    line = line.lower().strip()
                    new_line = ''
                    for char in line:
                        if char in symbols:
                            continue
                        else:
                            new_line += char
                    # print(new_line)
                    new_line = new_line.split()
                    words_file += new_line
                all_words[element] = words_file
        return all_words

    def find(self, word):
        result_find = {}
        for key, item in self.get_all_words().items():
            if word.lower() in item:
                result_find[key] = item.index(word.lower()) + 1
        return result_find

    def count(self, word):
        result_find = {}
        for key, item in self.get_all_words().items():
            if word.lower() in item:
                result_find[key] = item.count(word.lower())
        return result_find


# проверка работы программы
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt'
                      )
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
