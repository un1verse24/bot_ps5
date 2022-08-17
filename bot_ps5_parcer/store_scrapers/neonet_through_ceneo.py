import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# don't forget that we don't have links for for items in neonet, when we add to ome scraper

class NeoScraper():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    list_objects = []


    def search_ps5(self, url):
        driver = webdriver.Chrome(service=ChromeService(executable_path='/Users/rostislavohrim/Desktop/Навчання IT/just_studing/chrome_driver/chromedriver'))
        driver.get(url)
        driver.implicitly_wait(10)
        # button = driver.find_element(By.XPATH, '//*[@id="click"]/div[2]/section[1]/ul/li[2]/div/div[2]/div[1]/ul/li[2]')
        # button2 = driver.find_element(By.XPATH, '//*[@id="click"]/div[2]/section[3]/ul/li[1]/div/div[2]/div[1]/ul/li[2]')
        # list_counter_of_offers = driver.find_element(By.XPATH, '//*[@id="click"]/div[2]/section[1]/ul/li[2]/div/div[2]/div[1]/ul/li[1]').text


        # counter_of_offers = list_counter_of_offers[1].strip(')').strip('(')
        # try:
        #     counter_of_offers = int(counter_of_offers)
        # except Exception:
        #     counter_of_offers = 1

        # counter = 1
        # a = ActionChains(driver)
        # a.move_to_element(button)
        # a.click(button)
        #
        # # while True:
        # #     counter += 1
        # #     button_offer = driver.find_element(By.XPATH, f'//*[@id="click"]/div[2]/section[1]/ul/li[2]/div/div[2]/div[2]/div[5]/div[1]/ul/li[{counter}]/div/div[4]')
        # #     # //*[@id="click"]/div[2]/section[1]/ul/li[2]/div/div[2]/div[2]/div[5]/div[1]/ul/li[2]/div/div[4]
        # #     # //*[@id="click"]/div[2]/section[1]/ul/li[2]/div/div[2]/div[2]/div[5]/div[1]/ul/li[3]/div/div[4]
        # #     try:
        # #         a.click(button_offer)
        # #     except Exception:
        # #         break
        #
        # # a.click(button2)
        # a.perform()

        soup = BeautifulSoup(driver.page_source, 'lxml')
        all_stores = soup.find_all(class_='product-offers__list__item')

        for store in all_stores:
            if 'Neonet' in store.find(class_='offer-shop-opinions').text:
                all_ps5 = store.find_all(class_='product-offer-details__others-list__item__container')
                for ps5 in all_ps5:
                    name = ps5.find(class_='product-offer-details__others-list__item__title').text.strip().split('>>')
                    price = ps5.find(class_='product-offer-details__others-list__item__price').text.strip().split(',')


                    ps5_obj = {
                        'name': name[0],
                        'price': price[0],
                        'link': 'копіюйте назву і вставляйте в гугл'
                    }

                    self.list_objects.append(ps5_obj)
                break

            else:
                continue


    def get_data(self):
        return self.list_objects



if __name__ == '__main__':

    Scraper = NeoScraper()
    Scraper.search_ps5('https://www.ceneo.pl/86467784')
    Scraper.search_ps5('https://www.ceneo.pl/96861968')
    print(Scraper.list_objects)








# # here we can train and upgrade re expressions for searching neonet in text
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# req = requests.get('https://www.ceneo.pl/86467784', headers=headers)
#
#
#
# with open('html/ceneo.pl.html') as file:
#     page_html = file.read()
#
#
# soup = BeautifulSoup(page_html, 'lxml')
#
# all_blocks = soup.find_all(class_='product-offer__details__toolbar__links')
# store_neonet = None
# for store in all_blocks:
#     info_store = store.find('a').text.split()
#     if 'Neonet' in info_store:
#         store_neonet = store
#         break
#
#
# print(store_neonet)






