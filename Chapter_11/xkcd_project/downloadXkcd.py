#! python3
# downloadXkcd.py - Загружает все комиксы xkcd.

import requests
import os
import bs4

url = 'http://xkcd.com'  # начальный url-адрес
os.makedirs('xkcd', exist_ok=True)  # сохраняем комикс в папке ./xkcd

while not url.endswith('#'):
    # Загрузка страницы.
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Поиск url-адреса изображения комикса.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Не удалось найти изображение комикса.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Загрузить изображение.
            print('Загружается изображение %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Пропустить этот комикс
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # Сохранение изображения в папке ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Получение url-адреса кнопки Prev.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Готово.')
