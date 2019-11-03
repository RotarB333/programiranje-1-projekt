import csv
import os
import requests
stran = 'https://scryfall.com/search?as=full&order=set&page=1&q=set%3Am20+unique%3Aprints&unique=cards'

print(stran)

def download_url_to_string(url):    
    try:
        page_content = requests.get(url).text
    except requests.exception.RequestException as e:
        print(e)
        page_content =""
    return page_content

def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

def save_frontpage(page, directory, filename):
    #content = page_content(page)
    content = download_url_to_string(page)
    save_string_to_file(content, directory, filename)
    return None

def read_file_to_string(directory, filename):
    vsebina = open(os.path.join(directory, filename),'r', encoding='utf-8').read()
    return vsebina

for start in range(1, 19, 1) :
    url = ('https://scryfall.com/search?as=full&order=set&page={}&q=set%3Am20+unique%3Aprints&unique=cards'.format(start))
    ime_datoteke = f'karte-{start}.html'
    save_frontpage(url,'karte-HTML',ime_datoteke)
    print(start)