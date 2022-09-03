import requests
from bs4 import BeautifulSoup

class EmpikScraper:
    lst_obj = []
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    def search_ps5(self, url):
        req = requests.get(url, headers=self.headers)

        soup = BeautifulSoup(req.text, 'lxml')

        all_items = soup.find_all(class_='js-energyclass-product')

        for item in all_items:
            try:
                name = item.find(class_='ta-product-title').text.strip()
                price = item.find(class_='ta-price-tile').text.split(',')
                price = price[0].split()
                price = ''.join(price)
                price = int(price)
                link = 'https://www.empik.com' + item.find(class_='seoTitle').get('href').strip()

                one_obj = {
                    'name': name,
                    'price': price,
                    'link': link
                }

                self.lst_obj.append(one_obj)

            except:
                continue

    def get_data(self):
        return self.lst_obj



if __name__ == '__main__':
    scraper = EmpikScraper()
    scraper.search_ps5('https://www.empik.com/gry-i-programy/playstation-5/konsole,342803,s?qtype=facetForm')
    print(scraper.lst_obj)