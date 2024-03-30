import os
import urllib.request


def download_page(url, file_name):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
        with open(file_name, 'wb') as file:
            file.write(html)
        print(f'A página {url} foi baixada com sucesso como {file_name}!')
    except Exception as e:
        print(f"ocorreu um erro ao baixar a página: {e}")


class Page:

    def __init__(self, url: str, name: str):
        self.url = url
        self.name = name
        download_page(url, name)

    def read(self, encoding='utf-8'):

        with open(self.name, 'r', encoding=encoding) as html_file:
            return html_file.read()