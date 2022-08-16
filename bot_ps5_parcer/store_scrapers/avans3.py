from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service as ChromeService


class AvansScraper():

    lst_obj = [] # list with all item links on the page


    def get_last_page(self, url):
        # options = webdriver.ChromeOptions()
        # options.add_argument(
        #     'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')

        try:
            driver = webdriver.Chrome(service=ChromeService(
                executable_path='/Users/rostislavohrim/Desktop/Навчання IT/just_studing/chrome_driver/chromedriver',
                ))

            driver.get(url=url)
            driver.implicitly_wait(20)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            last_page = soup.find(class_='is-total').text.strip()
            return int(last_page)

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()


    def search_ps5(self, url):
        # options = webdriver.ChromeOptions()
        # options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')

        try:
            driver = webdriver.Chrome(service=ChromeService(
                executable_path='/Users/rostislavohrim/Desktop/Навчання IT/just_studing/chrome_driver/chromedriver',
            ))

            driver.get(url=url)
            driver.implicitly_wait(20)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            all_ps5 = soup.find(class_='c-grid').find_all(class_='c-grid_col')


            for item in all_ps5:
                try:
                    price = item.find(class_='a-price_price').text
                    if price != None:
                        name = item.find('a').text.strip()
                        link = 'https://www.avans.pl' + item.find('a').get('href')
                        one_ps5_obj = {
                            'name': name,
                            'link': link,
                            'price': price
                        }
                        self.lst_obj.append(one_ps5_obj)
                except Exception:
                    continue


        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()

    def get_data(self):
        return self.lst_obj


if __name__ == '__main__':
    scraper = AvansScraper()
    for page in range(1, scraper.get_last_page('https://www.avans.pl/konsole-i-gry/playstation-5/konsole-ps5') + 1):
        scraper.search_ps5(f'https://www.avans.pl/konsole-i-gry/playstation-5/konsole-ps5?page={page}')

    print(scraper.lst_obj)