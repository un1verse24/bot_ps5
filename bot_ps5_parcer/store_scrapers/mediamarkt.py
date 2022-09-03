import requests
from bs4 import BeautifulSoup






class MediaMarktScraper():
    lst_obj = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    def search_ps5(self):

        req = requests.get('https://mediamarkt.pl/konsole-i-gry/playstation-5/konsole-ps5', headers=self.headers)

        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        row_ps5 = soup.find_all(class_='offer')


        for ps5 in row_ps5:
            try:
                flag = ps5.find(class_='pricing is-unavailable') # check availability
                if flag == None:
                    price = ps5.find(class_='availability-available').find(class_='whole').text.strip()
                    name = ps5.find(class_='title').text.strip()
                    link = 'https://mediamarkt.pl' + ps5.find(class_='header').find('a').get('href')
            except Exception:
                print(self.lst_obj)
                break

            ps5_obj = {
                 'name': name,
                 'link': link,
                 'price': price
             }

            if ps5_obj in self.lst_obj:
                continue
            else:
                self.lst_obj.append(ps5_obj)

    def get_data(self):
        return self.lst_obj




if __name__ == '__main__':
    scraper = MediaMarktScraper()
    scraper.search_ps5()
    print(scraper.lst_obj)





