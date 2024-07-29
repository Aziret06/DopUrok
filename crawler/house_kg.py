import requests
from parsel import Selector
from pprint import pprint


class HouseParser:
    MAIN_URL = 'https://www.house.kg/kupit-kvaprtiru'
    BASE_URL = 'https://www.house.kg'

    def get_page(self):
        response = requests.get(HouseParser.MAIN_URL)
        print(response.status_code)

        self.page = response.text

    def get_flat_links(self):
        selector = Selector(text=self.page)
        links = selector.css('div.left-image a::attr(href)').getall()
        links = list(map(lambda l: f'{HouseParser.BASE_URL}{l}', links))
        pprint(links)
        return links


if __name__ == '__main__':
    parser = HouseParser()
    parser.get_page()
    parser.get_flat_links()
