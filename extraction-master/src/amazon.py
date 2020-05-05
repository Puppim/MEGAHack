import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from query import insert_product, insert_characteristics


class ScrapingAmazon:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def run(self, urls):
        for url in urls:
            self.get_product_info(url)

    def get_product_info(self, url):
        print("Cadastrando produto...")
        self.driver.get(url)

        name = self.get_name()
        review = self.get_review()
        description = self.get_description()
        characteristics = self.get_additional_info()

        print("Nome: ", name)
        print("Review: ", review)
        print("Description: ", description)

        obj = {
            'name': name,
            'review': review,
            'description': description
        }

        product_id = insert_product(obj)

        for characteristic in characteristics:
            obj = {
                'question': characteristic['info'],
                'answer':  characteristic['desc'],
                'product_id': product_id
            }
            insert_characteristics(obj)

        # Get Comments
        # comments = self.driver.find_elements_by_css_selector(
        #     'div > div.a-row.a-spacing-small.review-data > span > div > div.a-expander-content.reviewText.review-text-content.a-expander-partial-collapse-content')
        # processed_commments = self.get_comments(comments)

        print("Produto cadastrado.")

    def get_name(self):
        try:
            return self.driver.find_element_by_id("productTitle").text
        except:
            pass

    def get_review(self):
        try:
            review = self.driver.find_element_by_xpath(
                '//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span').text
            review = float(re.sub('[^0-9\,]', '', review)[:-1].replace(",", '.'))
            return review
        except:
            pass

    def get_description(self):
        try:
            return self.driver.find_element_by_xpath(
                '//*[@id="productDescription"]/p').text
        except:
            pass

    def get_additional_info(self):

        info_table = self.driver.find_elements_by_xpath(
            '//*[@id="prodDetails"]/div/div[2]/div/div[2]/div/div/table/tbody/tr')

        # Model:
        # { desc: "Height", info: "100m" }
        additional_info = []

        for row in info_table:
            info = row.find_elements(By.TAG_NAME, "td")[0]
            desc = row.find_elements(By.TAG_NAME, "td")[1]

            if info.text != ' ' or desc.text != ' ':
                additional_info.append({
                    'info': re.sub(' +', ' ', info.text),
                    'desc': re.sub(' +', ' ', desc.text),
                })

        return additional_info

    def get_comments(self, comments):
        all_comments = []
        for comment in comments:
            if comment.text != '':
                all_comments.append(comment.text.replace('\n', ''))

        return all_comments


WATCHES_URLS = [
    "https://www.amazon.com.br/Xiaomi-Relogio-Smartwatch-Pulseira-Inteligente/dp/B082P4MJ7M?ref_=s9_apbd_otopr_hd_bw_bHjKTRb&pf_rd_r=DJSBGEWA0DFBFPKB474G&pf_rd_p=0fa49bf0-3df8-5590-ba63-bc0eb11a1867&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=16244073011",
    "https://www.amazon.com.br/Smartwatch-Xiaomi-Mi-Band-4/dp/B07VR2D1Q7/ref=pd_sbs_107_5/142-3693354-3350925?_encoding=UTF8&pd_rd_i=B07VR2D1Q7&pd_rd_r=b922152c-6ae1-48f6-af36-5ca67c6451f4&pd_rd_w=4kJCt&pd_rd_wg=Hjcmo&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=3JS5X42YVTW1ZMC1GVHA&psc=1&refRID=3JS5X42YVTW1ZMC1GVHA",
    "https://www.amazon.com.br/Smartwatch-Xiaomi-Original-Lacrado-Enviado/dp/B07VMZG7QS/ref=pd_sbs_107_3/142-3693354-3350925?_encoding=UTF8&pd_rd_i=B07VMZG7QS&pd_rd_r=e7e4b928-8d45-49d3-85bb-26490c708f6d&pd_rd_w=1vtXj&pd_rd_wg=xjVPB&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=WC9GMDY93SSBC95RW37M&psc=1&refRID=WC9GMDY93SSBC95RW37M",
]

ACCESSORIES_URLS = [
    "https://www.amazon.com.br/Cabo-Macho-Preto-018-8702-ChipSce/dp/B077PWLR7T/ref=gbph_img_m-3_3867_9140f236?smid=A1ZZFT5FULY4LN&pf_rd_p=8f081876-80c4-4a49-9430-da9a5b243867&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_i=16339926011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=M8JS6N62W31D6EHVQ371"
]

HOME_URLS = [
    "https://www.amazon.com.br/Umidificador-127V-Black-Decker-Preto/dp/B075ZJXD5K?ref_=s9_apbd_orecs_hd_bw_bIgvZhL&pf_rd_r=VA0KJPK4MXKMFPSK35HY&pf_rd_p=465d0788-1b5e-5455-ad71-109c3e538a55&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=17124719011",
    "https://www.amazon.com.br/Aquecedor-Cadence-Termoventilador-Auros-127V/dp/B076HRQ5P5?ref_=s9_apbd_otopr_hd_bw_bIgvZhL&pf_rd_r=VA0KJPK4MXKMFPSK35HY&pf_rd_p=7fd5e31e-d781-5506-8ac0-66c9466e7b1b&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=17124719011"
]

NEW_URLS = [
    'https://www.amazon.com.br/Widescreen-Tecnologia-Replacement-Logitech-Equipamentos/dp/B01MTTMPKT?pf_rd_r=PHD6Y622NRDT629JANBM&pf_rd_p=bf2f86e8-194b-511f-a6e0-60690e009ee0&pd_rd_r=811b095d-e7ae-4c1c-ae3e-4bf17ff9a7ab&pd_rd_w=U6Yyo&pd_rd_wg=Vp6nb&ref_=pd_gw_ri',
    'https://www.amazon.com.br/SPEED-MPG102-Fortrek-acess%C3%B3rios-notebooks/dp/B0765Y7VGX?pf_rd_r=D30NHWZXD4R5Z8P66CKE&pf_rd_p=bf2f86e8-194b-511f-a6e0-60690e009ee0&pd_rd_r=24f09fea-6e3b-44f5-ab7d-9f086b93671c&pd_rd_w=zQIdW&pd_rd_wg=sy8ln&ref_=pd_gw_ri',
    'https://www.amazon.com.br/dp/B076X734SK/ref=cm_gf_aaag_iaaa_d_p0_qd0_At6vEbCi7ifavuc3SVSv',
    'https://www.amazon.com.br/dp/B076LXCSCK/ref=cm_gf_aaag_iaaa_d_p0_qd0_oz671OQ2Q4lzbi4wZiA4',
    'https://www.amazon.com.br/dp/B0751KPMVK/ref=cm_gf_aaag_iaaa_d_p0_qd0_aw63gacEiRJJ1WzQevZq',
    'https://www.amazon.com.br/dp/B07MZPWG6P/ref=cm_gf_aaag_iaaa_d_p0_qd0_jE3rkZLOfqI5pLebTaI5',
    'https://www.amazon.com.br/7-lobos-Varinha-Harry-Potter/dp/B07XH446TH/ref=pd_sbs_197_6/136-7260408-9650662?_encoding=UTF8&pd_rd_i=B07XH446TH&pd_rd_r=e50a1eca-1e03-4f8a-8dd7-d8ffd6313f05&pd_rd_w=dAa1b&pd_rd_wg=MWVMg&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=1T5S9GM10S9DQ52TZAED&psc=1&refRID=1T5S9GM10S9DQ52TZAED',
    'https://www.amazon.com.br/Toalha-Dohler-Aveludada-harry-potter/dp/B0859MG9KB/ref=pd_sbs_21_8?_encoding=UTF8&pd_rd_i=B0859MG9KB&pd_rd_r=6d3395ed-93a2-44a9-82ce-12a902bdcfb6&pd_rd_w=0hF3N&pd_rd_wg=3NBDH&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=C0KKMXW9RJ6KPZSKBEX8&psc=1&refRID=C0KKMXW9RJ6KPZSKBEX8',
    'https://www.amazon.com.br/Controle-Sem-Fio-Bluetooth-Branco/dp/B01GW3H3U8/ref=zg_bs_videogames_home_3?_encoding=UTF8&psc=1&refRID=RYJRCJF2MXAS567AQA3A',
    'https://www.amazon.com.br/L%C3%A2mpada-Positivo-Casa-Inteligente-Compat%C3%ADvel/dp/B082FTRR76/ref=zg_bs_home_home_2?_encoding=UTF8&psc=1&refRID=RYJRCJF2MXAS567AQA3A',
    'https://www.amazon.com.br/Alcool-Em-Gel-70-Radnaq/dp/B086W72ZKL/ref=zg_bs_home_home_1?_encoding=UTF8&psc=1&refRID=RYJRCJF2MXAS567AQA3A',
    'https://www.amazon.com.br/Staging-Product-Not-Retail-Sale/dp/B07FQK1TS9/ref=zg_bs_electronics_home_1?_encoding=UTF8&psc=1&refRID=RYJRCJF2MXAS567AQA3A',
    'https://www.amazon.com.br/Echo-Dot-3%C2%AA-Gera%C3%A7%C3%A3o-Cor-Preta/dp/B07PDHSJ1H/ref=zg_bs_electronics_home_2?_encoding=UTF8&psc=1&refRID=RYJRCJF2MXAS567AQA3A',
    'https://www.amazon.com.br/Positivo-Casa-Inteligente-bidirecional-controlado/dp/B07RY35PSV/ref=pd_rhf_ee_s_pd_crcd_1_10?_encoding=UTF8&pd_rd_i=B07RY35PSV&pd_rd_r=a596fe11-120f-49e2-9e86-199e397e51f3&pd_rd_w=diWnB&pd_rd_wg=mQx7h&pf_rd_p=b762b69e-2f69-438e-86c7-b1c583041006&pf_rd_r=XM4RJYXQ70PCRC9ZWSN8&psc=1&refRID=XM4RJYXQ70PCRC9ZWSN8',
    'https://www.amazon.com.br/Resposta-eQualizer-Zowie-XL2411P-Polegadas/dp/B075JGL4WV?ref_=s9_apbd_otopr_hd_bw_bHrUqbb&pf_rd_r=6RMQ3Q4YFM4VWZRT77FX&pf_rd_p=dfd6eead-be55-57b6-bdaf-226199170f0a&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=16364756011',
    'https://www.amazon.com.br/dp/B076VRHBH7/ref=cm_gf_aAN_i1_i12_i9_d_p0_qd0_s1fYwU2J9v37X2oRaJla',
    'https://www.amazon.com.br/dp/B076N2S8FV/ref=cm_gf_aAN_i10_i11_iaab_d_p0_qd0_BwjhCKDKPdXk9gbsXGqD',
    'https://www.amazon.com.br/dp/B0752R3Z6J/ref=cm_gf_aAN_i1_i18_i9_d_p0_qd0_cRxmLz7DDDVNM0JXqKQ7',
    'https://www.amazon.com.br/dp/B07TDBLHN5/ref=cm_gf_aAN_i10_i6_i7_d_p0_qd0_UMdNvk2sB6f4a98dQ5nf',
    'https://www.amazon.com.br/SanDisk-Ultra-Pendrives-Preto/dp/B00P8XQPY4/ref=zg_bsnr_computers_home_3?_encoding=UTF8&psc=1&refRID=TNB1F3K1J4VQHKRP8GC5',
    'https://www.amazon.com.br/Len%C3%A7os-Umedecidos-Antiss%C3%A9pticos-Freeco-pacote/dp/B084LGS17D/ref=zg_bsnr_home_home_3?_encoding=UTF8&psc=1&refRID=TNB1F3K1J4VQHKRP8GC5',
    'https://www.amazon.com.br/Apoio-P%C3%A9-Multivis%C3%A3o-APOIO-PR-Preto/dp/B075SKB5DH/ref=zg_bsnr_home_home_2?_encoding=UTF8&psc=1&refRID=TNB1F3K1J4VQHKRP8GC5',
    'https://www.amazon.com.br/Cadeira-Escrit%C3%B3rio-Presidente-Zermatt-Conforsit/dp/B086VPRVZJ/ref=zg_bsnr_office_home_2?_encoding=UTF8&psc=1&refRID=TNB1F3K1J4VQHKRP8GC5',
    'https://www.amazon.com.br/Marcador-Stabilo-Pastel-76-4701-unidades/dp/B085P2RT8Q/ref=zg_bsnr_office_home_1?_encoding=UTF8&psc=1&refRID=TNB1F3K1J4VQHKRP8GC5',
    'https://www.amazon.com.br/Secador-Cabelos-Britnia-SP2300-Azul/dp/B076HVN356?ref_=Oct_DLandingS_D_07ba5b6a_62&smid=A1ZZFT5FULY4LN',
    'https://www.amazon.com.br/Masculina-Pares-Sport-Algod%C3%A3o-Branco/dp/B07RXM43Z7/ref=gbps_img_s-5_944c_f78546bf?smid=A2D2IJYKKBY81R&pf_rd_p=faada73d-e81c-4969-8eeb-7b66099f944c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=J3XJMCNP2QXT2EPF4PTN',
    'https://www.amazon.com.br/CROCS-204967-Crocs-LiteRideTM-Pacer/dp/B074F87Z5Z?ref_=Oct_DLandingS_D_80ba8640_60&smid=A1ZZFT5FULY4LN',
    'https://www.amazon.com.br/Pares-Botas-Casual-Feminina-Longo/dp/B0863L4FGH/ref=gbps_img_s-5_944c_b25f3503?smid=A313DDE64S7J3Z&pf_rd_p=faada73d-e81c-4969-8eeb-7b66099f944c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=J3XJMCNP2QXT2EPF4PTN',
    'https://www.amazon.com.br/Care-Sun-Shield-Shampoo-Keune/dp/B06Y5SK6SY/ref=gbps_img_s-5_944c_34d3a1f7?smid=A1ZZFT5FULY4LN&pf_rd_p=faada73d-e81c-4969-8eeb-7b66099f944c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=J3XJMCNP2QXT2EPF4PTN',
    'https://www.amazon.com.br/Ray-Ban-Round-Double-Bridge-RB3647N/dp/B01N31E8RZ/ref=gbps_img_s-5_944c_4f03eba5?smid=A28EISIM7YARD&pf_rd_p=faada73d-e81c-4969-8eeb-7b66099f944c&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=J3XJMCNP2QXT2EPF4PTN'
]

scraping = ScrapingAmazon()

scraping.run(NEW_URLS)
