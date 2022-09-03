from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



class ElectroScraper():

    def __init__(self):

        self.lst_obj = []
        self.options = Options()
        self.options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }


    # options = webdriver.ChromeOptions()
    # options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')

    def get_last_page(self, url):
        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)

            driver.get(url)
            driver.implicitly_wait(30)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            amount_of_pages = soup.find(class_='is-total').text.strip()

            return int(amount_of_pages)

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()

    def search_ps5(self, url):

        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)

            driver.get(url)
            driver.implicitly_wait(30)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            all_ps5_items = soup.find(class_='c-grid').find_all(class_='c-grid_col')


        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()


            for item in all_ps5_items:
                try:
                    price = item.find(class_='a-price_price').text
                    if price != None:
                        name = item.find('a').text.strip()
                        link = 'https://www.electro.pl' + item.find('a').get('href')

                        ps5_obj = {
                            'name': name,
                            'link': link,
                            'price': price
                        }

                        self.lst_obj.append(ps5_obj)


                except Exception:
                    continue

    def get_data(self):
        return self.lst_obj



if __name__ == '__main__':
    scraper = ElectroScraper()
    for page in range(1, scraper.get_last_page('https://www.electro.pl/konsole-i-gry/playstation-5/konsole-ps5') + 1):
        scraper.search_ps5(f'https://www.electro.pl/konsole-i-gry/playstation-5/konsole-ps5?page={page}')

    print(scraper.lst_obj)

















