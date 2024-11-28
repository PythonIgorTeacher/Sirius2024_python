#Получить базовую ссылку
#обойти все теги <a> на странице
#найти все "хорошие" ссылки на этом же ресурсе
#добавить их в "очередь" для обхода
#обойти эти ссылки
#сохранить работающие ссылки в файл.
#нужно: отслеживать уже посещенные ссылки
#фильтровать содержимое ссылок


import urllib.request as r
import urllib.error as err
import bs4
from queue import Queue

base_url = 'stihi.ru' #корневой сайт
full_url = f'https://www.{base_url}'#адрес сайта, где ищем ссылки
urls_queue = Queue()#сюда сохраняем ссылки на будущее для обхода
used_urls = set() #тут сохраняем отработанные ссылки
filter = {'shop'} #фильтр для отбраковки неправильных ссылок

def crawler():
    while not urls_queue.empty():
        #отправка запросов и поиск ссылок:
        url = urls_queue.get() #получили одну из ссылок из очереди
        used_urls.add(url)     #запоминаем, что ссылку уже использовали
        response = r.urlopen(url) #отправляем запрос
        print('url:',url)

        soup = bs4.BeautifulSoup(response.read(),'html.parser')
        links = soup.find_all('a') #ищем все ссылки (теги <a>)
        for link in links:
            link = link['href']
            #проверяем ссылку черз фильтр- если есть одно из слов, которое мы не хотим
            if any(element in str(link) for element in filter):
                continue #переход к следующей ссылке
            if full_url not in link: #проверяем целостность ссылки
                link = full_url+ link
            if link in used_urls:
                continue
            else:
                urls_queue.put(link)




if __name__ == '__main__':
    #основное тело программы:
    #import urllib.error as err
    urls_queue.put(full_url)  # кладем первую ссылку в очередь
    while True:
        try:
            crawler()
        except err.URLError as e: #если возникает ошибка - обрабатываем
            print(full_url,e.reason)