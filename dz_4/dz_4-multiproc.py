import time
from multiprocessing import Process
from sys import argv

import requests


def download(url):
    response = requests.get(url)
    filename = 'multiproc_' + url.split('/')[-1]
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

    processes = []
    start_time = time.time()

    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
