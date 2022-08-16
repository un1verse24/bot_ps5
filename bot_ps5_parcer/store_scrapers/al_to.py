import requests
from bs4 import BeautifulSoup

class AlToScraper():


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}


    lst_obj = []

    def get_number_of_pages(self):
        req = requests.get('https://www.al.to/szukaj?sort_by=accuracy_desc&hide_unavailable=1&q=playstation%205&f%5Bgroups%5D%5B68%5D=1&f%5Bcategories%5D%5B2384%5D=1', headers=self.headers)
        soup = BeautifulSoup(req.text, 'lxml')

        try:
            pagination_block = soup.find_all(class_='sc-1xy3kzh-7')
        except Exception:
            return False

        try:
            pagination_block[-1].text  # fix for unavavailable error
            return pagination_block[-1].text
        except Exception:
            return None



    def search_ps5(self, url):

        req = requests.get(url, headers=self.headers)


        soup = BeautifulSoup(req.text, 'lxml')

        all_ps5_available_list = soup.find_all(class_='sc-162ysh3-1') #search all available ps5 on page and make list from divs

        for ps5 in all_ps5_available_list:
            name = ps5.find('h3').text.strip()
            link = 'https://www.al.to' + ps5.find('a').get('href')
            price = ps5.find(class_='sc-6n68ef-3').text
            ps5_obj = {
                'name': name,
                'link': link,
                'price': price
            }
            self.lst_obj.append(ps5_obj)

    def get_data(self):
        return self.lst_obj


if __name__ == '__main__':
    scraper = AlToScraper()
    if scraper.get_number_of_pages():
        for page in range(1, int(scraper.get_number_of_pages()) + 1):
            scraper.search_ps5(
                f'https://www.al.to/szukaj?sort_by=accuracy_desc&hide_unavailable=1&q=playstation%205&f%5Bgroups%5D%5B68%5D=1&f%5Bcategories%5D%5B2384%5D={page}')

        print(scraper.lst_obj)
