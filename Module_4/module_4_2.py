def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


# inner_function()  # приводит к ошибке, потому что эта функция является локальной для test_function
test_function()
