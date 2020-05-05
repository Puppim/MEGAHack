from selenium import webdriver
from query import inser_characteristics, insert_product
from selenium.webdriver.common.by import By
from time import sleep


class ScrapingMercadoLivre:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def run(self, urls):
        for url in urls:
            self.get_product_info(url)

    def get_product_info(self, url):
        print("Cadastrando produto...")
        self.driver.get(url)

        name = self.get_name()
        description = self.get_description()
        review = self.get_review()
        characteristics = self.get_characteristics()

        obj = {
            'name': name,
            'description': description,
            'review': review
        }

        # product_id = insert_product(obj)

        print("*Name: \n", name)
        print("*Description: \n", description)
        print("*Characteristics: \n", characteristics)


        for characteristic in characteristics:
            obj = {
                'question': characteristic['info'],
                'answer':  characteristic['desc'],
                # 'product_id': product_id
            }
            # inser_characteristics(obj)

        print("Produto cadastrado.")



    def get_name(self):
        try:
            print("entrou name")                                               
            return self.driver.find_element_by_css_selector("#root-app > div > div.ui-pdp-container.ui-pdp-container--pdp > div.ui-pdp-container__row.ui-pdp--relative.ui-pdp-with--separator--fluid.pb-40 > div.ui-pdp-container__col.col-3.pb-40 > div.ui-pdp-container__row.ui-pdp-with--separator--fluid.ui-pdp-with--separator--48 > div.ui-pdp-container__col.col-2.mr-32 > div.ui-pdp-container__top-wrapper.mt-40 > div.ui-pdp-header > h1").text
        except:
            pass

    def get_review(self):
        try:
            print("entrou review")                                               
            return self.driver.find_element_by_xpath('//*[@id="root-app"]/div/div[2]/div[3]/div[1]/div[1]/div/section/header/div/div/h2').text
        except:
            pass
    

    def get_description(self):
        try:
            print("entrou description")                                               
            return self.driver.find_element_by_xpath('//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[3]/div/div/p').text
        except:
            pass

    def get_characteristics(self):
        try:
            print("entrou characteristics")                                               
            characteristics = []
            
            button = self.driver.find_element_by_xpath('//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[4]/div/div/div[2]/span')
            sleep(1)
            button.click()
            
            info = self.driver.find_elements_by_xpath('//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[4]/div/div/div[2]/div/div/ul/li/span')
            desc = self.driver.find_elements_by_xpath('//*[@id="root-app"]/div/div[2]/div[1]/div[1]/div[4]/div/div/div[2]/div/div/ul/li/p')

            for i in range(0, len(info)):
                characteristics.append({
                    'info': info[i].text,
                    'desc': desc[i].text
                })
            
            return characteristics
        except:
            pass


HOME_URLS = [
    "https://www.mercadolivre.com.br/fone-de-ouvido-sem-fio-xiaomi-redmi-airdots-preto/p/MLB15283838?source=search#searchVariation=MLB15283838&position=1&type=product&tracking_id=957fbb18-1281-4fbb-89cd-1d4ee7da24ae",
]

scraping = ScrapingMercadoLivre()
scraping.run(HOME_URLS)
