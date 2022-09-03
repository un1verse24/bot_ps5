from bot_ps5_parcer.store_scrapers.mediamarkt import MediaMarktScraper
from bot_ps5_parcer.store_scrapers.RTV import RTVScraper
from bot_ps5_parcer.store_scrapers.avans3 import AvansScraper
from bot_ps5_parcer.store_scrapers.Electro import ElectroScraper
from bot_ps5_parcer.store_scrapers.x_com import XComScraper
from bot_ps5_parcer.store_scrapers.al_to import AlToScraper
from bot_ps5_parcer.store_scrapers.neonet_through_ceneo import NeoScraper
from bot_ps5_parcer.store_scrapers.Mediaexpert import MediaExpertScraper
from bot_ps5_parcer.store_scrapers.Empik import EmpikScraper


class AllShopsScraper:
    lst_ps5 = []

    def set_scrapers(self):
        self.scraper_mediamarkt = MediaMarktScraper()
        self.scraper_rtv = RTVScraper()
        self.scraper_avans = AvansScraper()
        self.scraper_electro = ElectroScraper()
        self.scraper_xcom = XComScraper()
        self.scraper_alto = AlToScraper()
        self.scraper_neonet = NeoScraper()
        self.scraper_mediaexpert = MediaExpertScraper()
        self.scraper_empik = EmpikScraper()

        self.scrapers_list = [self.scraper_mediamarkt, self.scraper_rtv, self.scraper_xcom, self.scraper_alto, self.scraper_avans, self.scraper_electro, self.scraper_neonet, self.scraper_mediaexpert, self.scraper_empik]

        # self.scraper_avans,
        # self.scraper_electro,



    def search_data(self):
        self.scraper_mediamarkt.search_ps5()
        self.scraper_rtv.search_ps5()

        if self.scraper_xcom.get_number_of_pages():
            for page in range(1, int(self.scraper_xcom.get_number_of_pages()) + 1):
                self.scraper_xcom.search_ps5(f'https://www.x-kom.pl/g-7/c/2572-konsole-playstation.html?hide_unavailable={page}')

        if self.scraper_alto.get_number_of_pages():
            for page in range(1, int(self.scraper_alto.get_number_of_pages()) + 1):
                self.scraper_alto.search_ps5(
                    f'https://www.al.to/szukaj?sort_by=accuracy_desc&hide_unavailable=1&q=playstation%205&f%5Bgroups%5D%5B68%5D=1&f%5Bcategories%5D%5B2384%5D={page}')

        for page in range(1, self.scraper_avans.get_last_page('https://www.avans.pl/konsole-i-gry/playstation-5/konsole-ps5') + 1):
            self.scraper_avans.search_ps5(f'https://www.avans.pl/konsole-i-gry/playstation-5/konsole-ps5?page={page}')

        for page in range(1,
                          self.scraper_electro.get_last_page('https://www.electro.pl/konsole-i-gry/playstation-5/konsole-ps5') + 1):
            self.scraper_electro.search_ps5(f'https://www.electro.pl/konsole-i-gry/playstation-5/konsole-ps5?page={page}')

        self.scraper_neonet.search_ps5('https://www.ceneo.pl/86467784')
        self.scraper_neonet.search_ps5('https://www.ceneo.pl/96861968')

        self.scraper_mediaexpert.search_ps5()
        self.scraper_empik.search_ps5('https://www.empik.com/gry-i-programy/playstation-5/konsole,342803,s?qtype=facetForm')


    def get_data(self):
        self.set_scrapers()
        self.search_data()

        for scraper in self.scrapers_list:
            scraper.get_data()
            self.lst_ps5 += scraper.get_data()

        return self.lst_ps5





if __name__ =='__main__':
    all_scraper = AllShopsScraper()
    all_scraper.get_data()
    print(all_scraper.lst_ps5)

