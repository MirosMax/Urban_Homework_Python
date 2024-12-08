import requests
import pprint

# получение данных сайта с помощью метода get
resource = requests.get('https://www.wikipedia.org/')

# получение содержимого сайта в байтах
pprint.pprint(resource.content)

# получение кода состояния сайта
print('Статус ответа от сайта:', resource.status_code)

# получение содержимого сайта в виде текста
print(resource.text)

# передача и получение данных cookies

cookies = {'session_token': '15791385794'}
resource = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(resource.text)

# скачивание изображения

url_img = 'https://avatars.mds.yandex.net/i?id=9188cb1df3c6cad43940eea817037580_l-5276057-images-thumbs&n=13'
resource_url = requests.get(url_img)
with open('image.jpg', 'wb') as file:
    file.write(resource_url.content)

# отправка на сервер данных с помощью post

data = {'key': '7777777777777'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.text)
