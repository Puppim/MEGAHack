# Extraction API

## Setup

Instala o geckodriver + webdriver do Firefox, após isso aponte o caminho do seu driver no argumento "executable_path" do instanciador de webdriver.

`webdriver.Firefox(executable_path={seu_path_aqui})`

Para rodar o projeto, crie um enviroment com o venv usando (fora da pasta do projeto):

`python -m venv extraction`

Instale as dependências com:

`pip install -r requirements.txt`

## Executando

Para executar o projeto, rode:

`python {nome_do_scraper}.py`
