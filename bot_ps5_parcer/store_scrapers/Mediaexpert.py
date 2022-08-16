import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MediaExpertScraper():
    lst_ps5 = []
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
     }
    def fetch(self, url):
        return requests.get(url, headers=self.headers)




    def found_last_page(self, url):
        driver = webdriver.Chrome(service=ChromeService(
            executable_path='/Users/rostislavohrim/Desktop/Навчання IT/just_studing/chrome_driver/chromedriver'))
        driver.get(url)

        a = ActionChains(driver)
        a.scroll_by_amount(0, 1000)
        a.perform()
        soup = BeautifulSoup(driver.page_source, 'lxml')
        return int(soup.find(class_='from').text.split()[1])

    def search_ps5(self):
        driver = webdriver.Chrome(service=ChromeService(executable_path='/Users/rostislavohrim/Desktop/Навчання IT/just_studing/chrome_driver/chromedriver'))
        for page in range(1, self.found_last_page('https://www.mediaexpert.pl/gaming/playstation-5/konsole-ps5') + 1):
            driver.get(f'https://www.mediaexpert.pl/gaming/playstation-5/konsole-ps5?page={page}')
            end_of_page = driver.find_element(By.XPATH, '//*[@id="section_list-pagination"]/div/span/small')
            a = ActionChains(driver)
            a.move_to_element(end_of_page)
            a.perform()
            soup = BeautifulSoup(driver.page_source, 'lxml')
            all_items = soup.find_all(class_='offer-box')
            flag = True
            if flag == False:
                break
            for item in all_items:
                if item.find(class_='main-price') != None:
                    name = item.find('h2', class_='name').text.strip()
                    price = item.find(class_='main-price').text.split()
                    link = 'https://www.mediaexpert.pl/' + item.find('h2', class_='name').find('a').get('href')

                    obj = {
                        'name': name,
                        'price': price[0] + ' ' + price[1],
                        'link': link
                    }

                    self.lst_ps5.append(obj)

    def get_data(self):
        return self.lst_ps5



if __name__ == '__main__':
    scraper = MediaExpertScraper()
    scraper.search_ps5()
    print(scraper.lst_ps5)







# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
#
# req = requests.get('https://www.mediaexpert.pl/search?query%5Bmenu_item%5D=49972&query%5Bquerystring%5D=playstation%205&sort=price_desc&page=1', headers=headers)

# page_text = req.text

# with open('ps5_expert.html', 'w') as file:
#     file.write(page_text)


# with open('ps5_expert.html') as file:
#     page_text = file.read()
#
# soup = BeautifulSoup(page_text, 'lxml')
#
# ps5_data_mediaexpert = soup.find_all(class_='whole')
# lst_ps = []
# for item in ps5_data_mediaexpert:
#     a_ps = item.find_parent().find_parent().find_parent().find_parent().find_parent().find_parent().find_parent()
#     lst_ps.append(a_ps)
#
#
# lst_sum = []
# for item in lst_ps:
#     try:
#         item_info_package = []
#         name_ps5 = item.find(class_='name is-section').text
#         if 'Konsola' in name_ps5:
#             # print(name_ps5)
#             link_ps5 = 'https://www.mediaexpert.pl/' + item.find('a', class_='is-animate spark-link').get('href')
#             # print(link_ps5)
#             price_ps5 = item.find(class_='whole').text
#             price_ps5 = price_ps5.split()
#             price_ps5 = ' '.join(price_ps5)
#             # print(price_ps5)
#             item_info_package.append(name_ps5.strip())
#             item_info_package.append(link_ps5)
#             item_info_package.append(price_ps5)
#             print(item_info_package)
#             lst_sum.append(item_info_package)
#     except Exception:
#         continue
#
# print(lst_sum)
#
#
#
#







