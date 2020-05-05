from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from unidecode import unidecode
from FilterQuestion import pever_msg
import pandas as pd

app = Flask(__name__)

### bot configuration ###
# degree of confidence in the response
trust = 0.5
##### FIM bot configuration ##############

bot = ChatBot('Naive')
bot = ChatBot(
    'Naive',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

f = open('offense.txt', 'r')
palavroestxt = f.readlines()

conversa = ListTrainer(bot)
df = pd.read_csv('question_answers.csv', sep=',', names=['question'], header=0)

def tolist(df):
    new_list = []
    for index, row in df.iterrows():
        new_list.append(df.loc[index,'question'])
    return new_list

new_list = tolist(df)

conversa.train(new_list)

def openFile( nome_arquivo : 'palavroes.txt' ):
    f = open(nome_arquivo, 'r')
    palavroestxt = f.readlines()

    list = []
    for w in palavroestxt:
        new = w.rstrip()
        list.append(new)
    return list

def offense(frase):
    offense = openFile('offense.txt')
    palavras = frase.split(" ")
    for x in palavras:
        for palavrao in offense:
            if x.upper() == palavrao.upper():
                return 'offense'

    return frase

@app.route('/predict', methods=['POST'])
def predict():
  dados = request.get_json(force=True)
  predicao = dados
  
  resposta = botresponse(dados['msg'],dados['confidence'],dados['flag_offense']) 

  return jsonify(resposta)



def botresponse(msg, trust:0.5, flag_offense:1):
    try:
        if flag_offense:
            result = offense(msg)
        else:
            result = msg
        if result != 'offense':
            predictions = pever_msg(result)
            answer = bot.get_response(result)

            if float(answer.confidence) > trust:
                # print('Naive: ', resposta, resposta.confidence)
                answer = {'answer': str(answer), 'confidence': str(answer.confidence), 'relevant':predictions}
                return answer
            else:
                # print("Eu não entendi :(")
                answer = {'answer': 'Eu não entendi a pergunta', 'confidence': str(answer.confidence), 'relevant':predictions} 
                return answer
        else:
            # print('Naive: boca suja')
            answer = {'answer': 'invalida', 'confidence': '0', 'relevant': 0 } 
            return answer

    except(KeyboardInterrupt, EOFError, SystemExit):
        return {'answer': 'ERROR', 'confidence': '0' ,'relevant':0} 



if __name__ == "__main__":
    app.run(debug=True)
