"""
Задание

Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения
в URL-адресе. Например, URL-адрес:
https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени
выполнения программы.

"""

import requests
import threading
import time
from sys import argv


def download(url):
    response = requests.get(url)
    filename = 'thread_' + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    urls = (argv[1],) if len(argv) > 1 else [
        'https://haski-mana.ru/wp-content/uploads/0/e/1/0e15cdeb52bd31e55661f574a12db2eb.jpeg',
        'https://natalyland.ru/wp-content/uploads/e/c/d/ecd84c093b3b5713390bbedb7b3c7002.jpeg',
        'http://www.dogwallpapers.net/wallpapers/collie-rough-dog-at-the-sunset-pic.jpg',
        'https://krasnodar.polvamvdom.ru/f/product/texture_lis-lisa-portret.jpg',
        'https://cdn1.ozone.ru/s3/multimedia-t/6450633953.jpg',
    ]

    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
