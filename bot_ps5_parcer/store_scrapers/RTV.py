import requests
from bs4 import BeautifulSoup



class RTVScraper():
    lst_obj = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

    def search_ps5(self):

        req = requests.get('https://www.euro.com.pl/konsole-playstation-5.bhtml?link=search#fromKeyword=playstation%205', headers=self.headers)

        src = req.text

        soup = BeautifulSoup(src, 'lxml')

        row_ps5 = soup.find_all(class_='product-row')


        for ps5 in row_ps5:
             ps5_name = ps5.find(class_='product-name').text.strip()
             ps5_link = 'www.euro.com.pl' + ps5.find(class_='js-save-keyword').get('href')
             ps5_price = ps5.find(class_='price-normal selenium-price-normal')
             if ps5_price != None:
                 ps5_price = ps5_price.text.strip().split()
                 ps5_price = ps5_price[0] + " " + ps5_price[1]
             else:
                continue


             ps5_obj = {
                 'name': ps5_name,
                 'link': ps5_link,
                 'price': ps5_price
             }

             self.lst_obj.append(ps5_obj)


    def get_data(self):
        return self.lst_obj





if __name__ == '__main__':
    scraper = RTVScraper()
    scraper.search_ps5()
    print(scraper.lst_obj)






