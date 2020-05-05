from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from query import insert_question


class ScraperQuestions:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def run(self, urls):
        self.get_all_questions(urls)

    def find_question(self, question):
        try:
            question_text = question.find_element(
                By.CSS_SELECTOR, "article.questions__item--question > div.questions__content > p").text
            return question_text
        except:
            pass

    def find_answer(self, question):
        try:
            answer_text = question.find_element(
                By.CSS_SELECTOR, "article.questions__item--answer > div.questions__content > p").text
            return answer_text
        except:
            pass

    def get_all_questions(self, urls):
        for url in urls:
            self.get_question(url)

    def get_questions_from_question_object(self, questions):
        print("Perguntas")
        for question in questions:
            question_text = self.find_question(question)
            answer_text = self.find_answer(question)

            obj = {
                'question': question_text,
                'answer': answer_text
            }

            print("Sendo inserido: ")
            print("Pergunta:", obj['question'])
            print("Resposta: ", obj['answer'])

            insert_question(obj)

    def get_question(self, url):
        self.driver.get(url)

        button_does_exist = True

        while button_does_exist:
            try:
                see_more_button = self.driver.find_element_by_xpath(
                    '//*[@id="showMoreQuestionsButton"]')
                see_more_button.click()
            except:
                button_does_exist = False
                print("Indo aos comentários")
                sleep(1)

        try:
            iframe = self.driver.find_element_by_css_selector(
                "#modal-iframe").get_attribute("src")
            self.driver.get(iframe)

            try:
                questions = self.driver.find_elements_by_xpath(
                    '//*[@id="vip-section-question"]/div[2]/div[4]/ul/li'
                )
                self.get_questions_from_question_object(questions)
            except:
                print("Erro")

        except:
            sleep(2)
            try:
                questions = self.driver.find_elements_by_css_selector(
                    "#vip-section-question > div.modal__content > div:nth-child(11) > ul > li"
                )
                self.get_questions_from_question_object(questions)
            except:
                print("Erro")

        print('\n\n\n')


URLS = ['https://produto.mercadolivre.com.br/MLB-1209172852-kit-emagrecedor-abdomen-dia-e-noite-120-caps-body-action-_JM?variation=35140335143&quantity=1#reco_item_pos=3&reco_backend=promotions-sorted-by-score-mlb&reco_backend_type=low_level&reco_client=home_seller-promotions-recommendations&reco_id=aefa67d3-303b-40e8-b54d-e84eaca343c8&c_id=/home/promotions-recommendations/element&c_element_order=4&c_uid=32b5cc80-eb56-4d30-89bc-984234ca97b7',
        'https://produto.mercadolivre.com.br/MLB-1148305949-combo-para-emagrecer-bcaa-colageno-shake-termogenico-_JM?quantity=1#reco_item_pos=2&reco_backend=machinalis-v2p-pdp-v2&reco_backend_type=low_level&reco_client=vip-v2p&reco_id=0ae22577-2619-4a68-907b-a402d6b608f2',
        'https://produto.mercadolivre.com.br/MLB-786341088-kit-colageno-hidrolisado-300-capsulas-max-titanium-_JM?variation=25207697049&quantity=1#reco_item_pos=2&reco_backend=machinalis-v2p-pdp-v2&reco_backend_type=low_level&reco_client=vip-v2p&reco_id=f52cc926-23a6-4f4c-9dea-32b0ceb03bdb',
        'https://produto.mercadolivre.com.br/MLB-1142223824-seca-barriga-goji-berry-colageno-500mg-120-comprimidos-_JM?variation=32152559463&quantity=1#reco_item_pos=1&reco_backend=machinalis-domain-pads&reco_backend_type=low_level&reco_client=vip-pads&reco_id=d82a0e19-0115-4832-95bf-a4978a9b23d3&is_advertising=true&ad_domain=VIPCORE_RECOMMENDED&ad_position=2&ad_click_id=ODdlYTAzYTUtNTEyNC00OTRmLTgyZTgtOGM5ZDdhZjQzMzFi',
        'https://produto.mercadolivre.com.br/MLB-1312092377-kit-3-biotina-firmeza-crescimento-saude-cabelos-unhas-pele-_JM?variation=42993217448&quantity=1#reco_item_pos=4&reco_backend=machinalis-domain-pads&reco_backend_type=low_level&reco_client=vip-pads&reco_id=f989ab0b-034f-4522-836b-1d388aea9dd4&is_advertising=true&ad_domain=VIPCORE_RECOMMENDED&ad_position=5&ad_click_id=NmQxNzVhYmEtY2UyNi00YWJlLWI1MTYtZjc2ZTdlOTZmZTk5',
        'https://produto.mercadolivre.com.br/MLB-903229287-gaba-acido-gama-aminobutirico-200mg-60-caps-_JM?variation=32229733422&quantity=1#reco_item_pos=2&reco_backend=p2p-v9&reco_backend_type=low_level&reco_client=vip&reco_id=cfd075ab-9fb5-459f-b88d-483ab199126d',
        'https://produto.mercadolivre.com.br/MLB-1068452924-kit-c-10-relogio-masculino-atacado-10-caixas-10-bate-_JM?quantity=1&variation=32868862807#position=1&type=item&tracking_id=6fd42058-e909-4ffd-959e-9e069e978def',
        'https://produto.mercadolivre.com.br/MLB-930542160-relogio-technos-masculino-performer-sports-2315jb8r-_JM?quantity=1#position=17&type=item&tracking_id=6fd42058-e909-4ffd-959e-9e069e978def',
        'https://produto.mercadolivre.com.br/MLB-1050323077-relogio-curren-masculino-importado-original-8077-nota-fiscal-_JM?searchVariation=24980941053&quantity=1&variation=24980941053#searchVariation=24980941053&position=16&type=item&tracking_id=6fd42058-e909-4ffd-959e-9e069e978def',
        'https://produto.mercadolivre.com.br/MLB-1045456985-relogio-speedo-monitor-cardiaco-original-esport-80565g0epnp1-_JM?quantity=1&variation=41906123959#position=21&type=item&tracking_id=6fd42058-e909-4ffd-959e-9e069e978def',
        'https://produto.mercadolivre.com.br/MLB-943961389-pulseira-invicta-subaqua-noma-3-original-somos-fornecedor-_JM?quantity=1&variation=32351723883#position=22&type=item&tracking_id=6fd42058-e909-4ffd-959e-9e069e978def',
        'https://produto.mercadolivre.com.br/MLB-1186582690-kit-5-bermuda-moleton-shorts-academia-atacado-nf-full-_JM?quantity=1#reco_item_pos=26&reco_backend=promotions-sorted-by-score-mlb&reco_backend_type=low_level&reco_client=seller-promotions&reco_id=2b52621d-2c86-4088-b9c7-612b93d47615&deal_print_id=dfc964c0-8d71-11ea-90b0-d17364a543a9&model_version=release-2.0.0-bacalao&promotion_type=TODAY_PROMOTION',
        'https://produto.mercadolivre.com.br/MLB-1219850117-jogo-de-soquete-57-pecas-14-catraca-chave-allen-stels-_JM?quantity=1#reco_item_pos=34&reco_backend=promotions-sorted-by-score-mlb&reco_backend_type=low_level&reco_client=seller-promotions&reco_id=2b52621d-2c86-4088-b9c7-612b93d47615&deal_print_id=dfc964c0-8d71-11ea-90b0-d17364a543a9&model_version=release-2.0.0-bacalao&promotion_type=TODAY_PROMOTION',
        'https://produto.mercadolivre.com.br/MLB-1266084754-kit-pesqueiro-4-varas-telescopica-2-de-270-2-de-360-brin-_JM?quantity=1#reco_item_pos=42&reco_backend=promotions-sorted-by-score-mlb&reco_backend_type=low_level&reco_client=seller-promotions&reco_id=2b52621d-2c86-4088-b9c7-612b93d47615&deal_print_id=dfc964c0-8d71-11ea-90b0-d17364a543a9&model_version=release-2.0.0-bacalao&promotion_type=TODAY_PROMOTION',
        'https://produto.mercadolivre.com.br/MLB-938200916-jogo-assadeiras-5-pecas-conjunto-forma-bolo-borda-alta-kit-_JM?quantity=1#position=1&type=item&tracking_id=fa201ed2-7b61-4f8e-90b7-8af0dab2d216',
        'https://produto.mercadolivre.com.br/MLB-850050950-faca-tatica-karambit-cs-go-multi-color-fade-real-fulltang-_JM?quantity=1&variation=44954533117#position=1&type=item&tracking_id=522ff55b-f9c9-44dd-bab2-93714ab070eb',
        'https://produto.mercadolivre.com.br/MLB-1172906671-sensor-de-freio-abs-volvo-xc60-s60-v60-lado-direito-_JM?quantity=1#position=2&type=item&tracking_id=d29bd6ed-3531-40f5-b1ca-f32b819949d1',
        'https://produto.mercadolivre.com.br/MLB-1155821966-kit-disco-freio-dianteiro-pastilhas-jac-j3-14-16-16v-_JM?quantity=1#position=1&type=item&tracking_id=d29bd6ed-3531-40f5-b1ca-f32b819949d1',
        'https://produto.mercadolivre.com.br/MLB-1066669543-corrente-masculino-banhada-a-ouro-18k-cordo-ping-cruz-_JM?searchVariation=34923298856&quantity=1&variation=34923298856#searchVariation=34923298856&position=3&type=item&tracking_id=b08a51fa-fca1-457f-84e0-95b44244f224',
        'https://produto.mercadolivre.com.br/MLB-1313572881-cordo-de-prata-925-escama-de-peixe-pingente-crucifixo-47mm-_JM?searchVariation=43086336145&quantity=1&variation=43086336145#searchVariation=43086336145&position=14&type=item&tracking_id=b08a51fa-fca1-457f-84e0-95b44244f224',
        'https://produto.mercadolivre.com.br/MLB-1019263070-rottweiler-filhotes-40-dias-frete-gratis-_JM?quantity=1#position=5&type=item&tracking_id=8d9f51d2-9536-4c08-bdb5-6664fe7d06a8',
        'https://produto.mercadolivre.com.br/MLB-1141648882-spitz-alemo-ou-lulu-da-pomernia-ano-_JM?searchVariation=36124566245&quantity=1&variation=36124566245#searchVariation=36124566245&position=47&type=item&tracking_id=8d9f51d2-9536-4c08-bdb5-6664fe7d06a8',
        'https://produto.mercadolivre.com.br/MLB-1229535790-cortina-300-leds-branca-fria-fixa-3m-x-2m-110v-3fb1-b0-_JM?quantity=1#position=1&type=item&tracking_id=88f60ece-e956-4d0a-aeb3-7b3a59b9417e',
        'https://produto.mercadolivre.com.br/MLB-811800476-cortina-blecaute-blackout-corta-luz-quarto-ou-sala-_JM?searchVariation=32760779361&quantity=1&variation=32760779361#searchVariation=32760779361&position=1&type=item&tracking_id=2827d353-c170-45d2-8566-08bb6488ecb9',
        'https://produto.mercadolivre.com.br/MLB-935560371-cortina-oxford-de-salaquarto-300x250-promoco-_JM?searchVariation=31554576107&quantity=1&variation=31554576107#searchVariation=31554576107&position=2&type=item&tracking_id=2827d353-c170-45d2-8566-08bb6488ecb9',
        "https://produto.mercadolivre.com.br/MLB-1309802556-kit-barra-lg-32ln540-32la613b-32ln5400-32ln570b-a1-a1-a2-_JM?quantity=1#position=1&type=item&tracking_id=27c81c96-7588-41f5-8a9e-6dd5ee2c0596"
        "https://produto.mercadolivre.com.br/MLB-1309802730-kit-3-barras-led-tv-lg-32ln5400-1-c-8-e-2-c-7-leds-a1-a1-a2-_JM?quantity=1#reco_item_pos=5&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1217172170-led-backlight-lg-2835-1w-3v-32ln5400-39ln5400-42ln5400-100un-_JM?variation=35731709738&quantity=1#reco_item_pos=6&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1325937470-kit-200-pcs-led-smd-2835-3v-1w-tv-lg-com-abas-32ln5400-39ln-_JM?variation=43894818623&quantity=1#reco_item_pos=7&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1217154866-kit-barras-leds-lg-32la613b-32ln5400-32ln570b-a1-a1-b1-nova-_JM?quantity=1#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f2ec9c17-a99b-4df1-a6ca-4cda5c8f4031"
        "https://produto.mercadolivre.com.br/MLB-1236263783-kit-3-barras-led-nova-32ln5400-32ln570b-32la613b-32ln540b-_JM?quantity=1#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f2ec9c17-a99b-4df1-a6ca-4cda5c8f4031"
        "https://produto.mercadolivre.com.br/MLB-1191739395-kit-barras-leds-lg-32ln5400-a1-a1-b1-nova-_JM?quantity=1#reco_item_pos=2&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f2ec9c17-a99b-4df1-a6ca-4cda5c8f4031"
        "https://produto.mercadolivre.com.br/MLB-1197062532-100-led-2835-lg-1w-3v-32ln5400-39ln5700-com-abas-_JM?quantity=1#reco_item_pos=3&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f2ec9c17-a99b-4df1-a6ca-4cda5c8f4031"
        "https://produto.mercadolivre.com.br/MLB-1054087205-led-backlight-lg-2835-1w-3v-32ln5400-39ln5400-42ln5400-60un-_JM?variation=32205496302&quantity=1#reco_item_pos=4&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f2ec9c17-a99b-4df1-a6ca-4cda5c8f4031"
        "https://produto.mercadolivre.com.br/MLB-1287116366-kit-barra-led-lg-49lb5500-49lb6200-49lf5200-49lf5500-impor-_JM?quantity=1#reco_item_pos=8&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1197070256-kit-novo-aluminio-c12-barra-led-50ln5400-50la6200-50ln5700-_JM?quantity=1#reco_item_pos=9&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1309802223-kit-barra-lg-32ln540-32la613b-32ln5400-32ln570b-a1-a1-a2-_JM?quantity=1#reco_item_pos=10&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1270454986-kit-4-barras-led-lg-49uj6525-49uj6565-novas-importadas-_JM?quantity=1#reco_item_pos=11&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1197068847-kit-barras-de-led-tv-lg-50ln5400-50ln5700-50la6200-_JM?quantity=1#reco_item_pos=12&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1363165981-kit-3-barra-de-led-tv-lg-32lb550b-32lb560b-32lf550b-32lb5600-_JM?quantity=1#reco_item_pos=13&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1309802061-kit-barra-lg-32ln540-32la613b-32ln5400-32ln570b-a1-a1-a2-_JM?quantity=1#reco_item_pos=14&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1054094789-led-backlight-lg-2835-1w-3v-32ln5400-39ln5400-42ln5400-50un-_JM?variation=32205811757&quantity=1#reco_item_pos=15&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1270453545-kit-4-barras-led-lg-49uj6525-49uj6565-novas-importadas-_JM?quantity=1#reco_item_pos=16&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1495296472-kit-barra-de-led-lg-8-barras-40lf6350-40lf5750-40lf5700-_JM?quantity=1#reco_item_pos=17&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1270450260-kit-4-barras-led-lg-49uj6525-49uj6565-novas-importadas-_JM?quantity=1#reco_item_pos=18&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1197070254-kit-novo-4-barras-aluminio-led-32l2400-dl3244-dl3245i-dl3253-_JM?quantity=1#reco_item_pos=19&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=7c79b61f-f0e0-4b2b-ad33-bb5e5bfc4b4c"
        "https://produto.mercadolivre.com.br/MLB-1333011559-notebook-acer-aspire-5-a515-52g-56uj-core-i5-ssd-256-mx130-_JM?quantity=1#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=2076ab3f-bd43-4e33-bcb1-b7094e82b6af"
        "https://produto.mercadolivre.com.br/MLB-1357559069-notebook-gamer-acer-an515-5771-ci5-8gb-1tb-128gb-1050-endles-_JM#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1333008706-notebook-acer-aspire-5-a515-52g-56uj-intel-core-i5-8265u-8-_JM?quantity=1#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1472267028-notebook-aspire-5-a515-52-57b7-i5-4-gb-1tb-hdd-156-win10-_JM?quantity=1#reco_item_pos=2&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1463243880-notebook-acer-aspire-3-a315-42-r1b0-amd-ryzen-5-12gb-1tb-hdd-_JM?quantity=1#reco_item_pos=3&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1473327231-notebook-acer-aspire-3-a315-r1rj-ryzen-5-12gb-1tb-128gb-ssd-_JM?quantity=1#reco_item_pos=4&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1476251403-notebook-acer-aspire-3-a315-42-r73t-amd-ryzen-3-4gb-1tb-hd-_JM?variation=53639253963&quantity=1#reco_item_pos=5&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1490450486-notebook-acer-aspire-3-a315-54-58h0-intel-i5-4gb-1tb-w10-_JM?quantity=1#reco_item_pos=6&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1501886213-notebook-acer-aspire-3-a315-42g-r6fz-amd-ryzen-5-8gb-1tb-_JM?quantity=1#reco_item_pos=7&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1240955611-notebook-acer-aspire-5-a515-52g-50nt-i5-8-geraco-8gb-ssd-128gb-1tb-nvidia-geforce-mx130-2gb-tela-156-hd-windows-10-_JM?quantity=1#reco_item_pos=8&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1357559061-notebook-acer-aspire-a515-52-79ut-ci7-8gb-1tb-156-win10pro-_JM?quantity=1#reco_item_pos=9&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1357554651-notebook-acer-aspire-a515-52-79ut-ci7-8gb-1tb-156-win10pro-_JM?quantity=1#reco_item_pos=10&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1505465029-notebook-gamer-acer-an515-5771-ci5-8gb-1tb-128gb-1050-endles-_JM#reco_item_pos=11&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1333370952-notebook-gamer-acer-nitro-5-an515-52-i7-16gb-128ssd-gtx-_JM?quantity=1#reco_item_pos=12&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1501938032-notebook-acer-aspire-3-a315-54k-31e8-i3-4gb-ram-1tb-hd-156-_JM?quantity=1#reco_item_pos=13&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1509503586-notebook-acer-aspire-3-a315-53-c2ss-i5-8gb-ram-512gb-ssd-_JM?quantity=1#reco_item_pos=14&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1401793927-mochila-acer-camuflada-para-notebook-156-_JM?quantity=1#reco_item_pos=15&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1240960820-notebook-acer-aspire-5-a515-52g-50nt-i5-8-geraco-8gb-ssd-128gb-1tb-nvidia-geforce-mx130-2gb-tela-156-hd-windows-10-_JM?quantity=1#reco_item_pos=16&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1504108930-notebook-aspire-5-a515-52-57b7-i5-4-gb-1tb-hdd-156-win10-_JM?quantity=1#reco_item_pos=17&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1250380622-acaba-hoje-monitor-gamer-acer-kg241q-236-full-hd-144hz-1m-_JM?quantity=1#reco_item_pos=18&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1250377219-acaba-hoje-monitor-gamer-acer-kg241q-236-full-hd-144hz-1m-_JM?quantity=1#reco_item_pos=19&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=f38e0518-25a6-4b06-b73c-5ff8408a39e0"
        "https://produto.mercadolivre.com.br/MLB-1490212549-monitor-gamer-acer-xb253q-gx-245-240hz-05ms-ips-g-sync-_JM?quantity=1#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-1441908595-mouse-gamer-predator-cestus-300-_JM?quantity=1#reco_item_pos=3&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-1491093617-monitor-gamer-predator-x27-4k-144hz-gsync-_JM?quantity=1#reco_item_pos=4&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-1490044413-monitor-acer-sa270-27-full-hd-75z-1ms-hdmi-vga-_JM?quantity=1#reco_item_pos=6&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-1044440095-monitor-gamer-acer-kg271-27-75hz-1ms-full-hd-_JM?quantity=1#reco_item_pos=9&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-976458864-monitor-gamer-acer-predator-xb241yu-24-wqhd-144hz-g-sync-hd-_JM?quantity=1#reco_item_pos=11&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=a68b1fa7-5fde-4f58-83fc-e8fbb690bb70"
        "https://produto.mercadolivre.com.br/MLB-1291617028-teclado-gamer-acer-nitro-com-suporte-anti-ghosting-e-6-opcoe-_JM?quantity=1#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=bd6a9545-137e-430f-b953-3a241bd0180d"
        "https://produto.mercadolivre.com.br/MLB-1490038736-monitor-gamer-predatos-x34-ips-3440-x-1440-ultrawide-120hz-_JM?quantity=1#reco_item_pos=3&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=bd6a9545-137e-430f-b953-3a241bd0180d"
        "https://produto.mercadolivre.com.br/MLB-1291671112-headset-gamer-acer-nitro-audio-poderoso-com-microfone-p2-_JM?quantity=1#reco_item_pos=13&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=bd6a9545-137e-430f-b953-3a241bd0180d"
        "https://produto.mercadolivre.com.br/MLB-1291671374-mousepad-gamer-acer-nitro-design-de-alta-perfomance-e-excele-_JM?quantity=1#reco_item_pos=14&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=bd6a9545-137e-430f-b953-3a241bd0180d"
        "https://produto.mercadolivre.com.br/MLB-1113389070-receiver-concert-one-raveo-phono-aux-fm-cd-mp3-usb-bluetooth-_JM?quantity=1#position=1&type=item&tracking_id=a6ce1ee4-2a0b-496b-a331-a76e8c9ac9fb"
        "https://produto.mercadolivre.com.br/MLB-1022628615-amplificador-modulo-receiver-som-ambiente-ma-120-mp3-radio-_JM?quantity=1&variation=42445092406#position=2&type=item&tracking_id=a6ce1ee4-2a0b-496b-a331-a76e8c9ac9fb"
        "https://produto.mercadolivre.com.br/MLB-829777839-mini-modulo-amplificador-karaoke-400-watts-com-bluetooth-usb-_JM?quantity=1#reco_item_pos=0&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=1aeb78f1-bbad-48fe-ba19-58eca4e194f9"
        "https://produto.mercadolivre.com.br/MLB-867928387-amplificador-4-canal-som-igreja-casa-loja-som-ambiente-usb-_JM?quantity=1#reco_item_pos=7&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=1aeb78f1-bbad-48fe-ba19-58eca4e194f9"
        "https://produto.mercadolivre.com.br/MLB-1113364347-toca-discos-tr-1000-concert-one-agulha-technica-phono-_JM?quantity=1#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=688d958a-6a8b-4806-a2a8-1ec767108381"
        "https://produto.mercadolivre.com.br/MLB-839056604-amplificador-raveo-pulse-bluetooth-30w-usb-caixa-som-_JM?variation=32289276348&quantity=1#reco_item_pos=2&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=688d958a-6a8b-4806-a2a8-1ec767108381"
        "https://produto.mercadolivre.com.br/MLB-813288285-toca-disco-jazz-harmony-vitrola-cd-gravaco-bluetooth-fm-_JM?variation=39258829235&quantity=1#reco_item_pos=3&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=688d958a-6a8b-4806-a2a8-1ec767108381"
        "https://produto.mercadolivre.com.br/MLB-682541627-toca-discos-raveo-arena-gravador-fm-usb-bluetooth-vitrola-_JM?variation=48881585126&quantity=1#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=12965dd9-0f3d-49af-93d0-7149d280171d"
        ]

scraper = ScraperQuestions()

scraper.run(URLS)
