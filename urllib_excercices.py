# ##пример использования модуля urllib.request
# import urllib.request as r
#
# url = 'https://www.example.com'
# response = r.urlopen(url)
# print(response.read().decode('utf-8'))
#
# with  r.urlopen(url) as response:
#     html = response.read().decode('utf-8')
# print(html)


# ##пример использования urllib.parse
# from urllib.parse import urlparse, urlencode
# #разделяем ссылку на кусочки для анализа содержимого
# url = 'https://www.example.com/search?q=python&amp;lang=en'
# #GET -запросы у которых данные содержатся в ссылке
# #POST - запросы, которые отправляются в виде словарей
# print(urlparse(url))
# #готовим данные для отправки в качестве GET-запроса
# parameters = {'q':'python', 'lang':'en'}
# query_string = urlencode(parameters)
# print(query_string) #закодированный GET-запрос


# #Что такое запрос, Как использовать заголовки и отправлять данные
# import urllib.request
# import urllib.parse
# values = {'name':'Ivan','password':'123465'}
# data = urllib.parse.urlencode(values).encode('utf-8')
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
# #Пример отправки данных в POST запросе
# #req = urllib.request.Request('https://example.com/', data, headers)
# req = urllib.request.Request('https://example.com/', headers=headers)
# with urllib.request.urlopen(req) as response:
#     html = response.read()
#     print(html)


# #Работа с ошибками
# import urllib.request as r
# import urllib.parse as p
# import urllib.error as err
# data = {'name':'me', 'password':'123'}
# data = p.urlencode(data).encode('utf-8')
# req = r.Request('https://www.example.com/sirius')
# #отрабатываем ошибку:
# try:
#     html = r.urlopen(req).read()
#
# except err.URLError as e:
#     print(e,'\n',e.reason,'\n',e.code)
# else:
#     print('Всё хорошо, страница доступна')




import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.stihi.ru'
req = urllib.request.Request(url) #запрос
html = urllib.request.urlopen(req) #выполняем запрос
html = html.read()
#готовим парсер: features - Тип парсера
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify()) #красиво распечатать строку с содержимым HTML-документ
# print(soup.get_text()) #получить весь текст со страницы
#
# #ищем все теги <a>, которые содержат ссылки
# links = soup.findAll('a')
# for link in links:
#     print(link['href'],link.text)
##прямой поисск по имени тега:
title = soup.title
print(title.name, title.string, title.parent.name)
print(soup.p['class'])
##подробный поиск при помщи функции find и доп. атрибутов
# print(soup.find(id='litclubtv'))


##Двухуровневый поиск
body = soup.find('body') #нашли "тело" страницы
#Нашли все картинки внутри Body
images = body.find_all('img')
for img in images:
    print(img['src'])