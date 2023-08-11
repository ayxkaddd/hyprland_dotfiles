#!/usr/bin/python3

import os
import sys
import random
import string
import pathlib
import requests
import time

DOWNLOAD_DIR = f"{str(pathlib.Path.home())}/pics/walls"
retry_list = []


def generate_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


def get_ext(url):
    return os.path.splitext(url)[1]


def download_wallpaper(url):
    global retry_list
    small_url = f"https://.../{url.split('/')[-1]}"
    print(f"[***] Downloading {small_url}")
    res = requests.get(url, allow_redirects=True)
    if res.status_code == 200:
        download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
        open(download_path, 'wb').write(res.content)
        print(f"[+++] Downloading done of {small_url}")
    else:
        print(f"[!!!] Failed to download {small_url}. Appended to retry_list")
        retry_list.append(url)


def wallpaper_search_api(query):
    if query == "--random" or query == "-r":
        query_url = "https://wallhaven.cc/api/v1/search?sorting=random"
    else:
        query_url = f"https://wallhaven.cc/api/v1/search?q={query}&sorting=random" 
    
    res = requests.get(query_url)
    response = res.json()
    dl_links = []
    for wallpaper in response["data"]:
        dl_links.append(wallpaper["path"])

    return dl_links


def download_unsucces(url):
    res = requests.get(url, allow_redirects=True)
    if res.status_code == 200:
        download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
        open(download_path, 'wb').write(res.content)
        print(f"[+++] Downloading done of {url}")
    else:
        print(f"[!!!] Failed to download {url}. (Broken link or you sent 2 much requests.) Manual downloading needed.")


def retry_unsucces():
    global retry_list
    print(f"[***] Retrying to download {len(retry_list)} unsuccesfully downloaded wallpapers")
    if len(retry_list) == 0:
        print("[***] No need to retry!")
    else:
        for url in retry_list:
            print(url)
            download_unsucces(url)

    retry_list = []


if __name__ == "__main__":
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    if len(sys.argv) < 2:
        print("Usage waldl.py <search_query>")
        quit()

    query = sys.argv[1]
    wallpapers = wallpaper_search_api(query)

    for wallpaper in wallpapers:
        download_wallpaper(wallpaper)

    retry_unsucces()
    print(f"[+++] Download complete!")
