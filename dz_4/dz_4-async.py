import asyncio
import time
from sys import argv

import requests


async def download(url):
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {"stream": True})
    filename = 'async_' + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    urls = (argv[1],) if len(argv) > 1 else [
        'https://haski-mana.ru/wp-content/uploads/0/e/1/0e15cdeb52bd31e55661f574a12db2eb.jpeg',
        'https://natalyland.ru/wp-content/uploads/e/c/d/ecd84c093b3b5713390bbedb7b3c7002.jpeg',
        'http://www.dogwallpapers.net/wallpapers/collie-rough-dog-at-the-sunset-pic.jpg',
        'https://krasnodar.polvamvdom.ru/f/product/texture_lis-lisa-portret.jpg',
        'https://cdn1.ozone.ru/s3/multimedia-t/6450633953.jpg',
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
