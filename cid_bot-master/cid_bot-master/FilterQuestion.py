import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import cross_val_score
# from sklearn.multiclass import OneVsRestClassifier
# from sklearn.svm import LinearSVC
# from sklearn.multiclass import OneVsOneClassifier
# from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('dbTrain.csv')

msgSeller = df['body']

separate_words = msgSeller.str.lower().str.replace('?','').str.split()

global dictionary
dictionary = set()
for list_w in separate_words:
    if len(list_w) < 22:
        dictionary.update(list_w)


total_words = len(dictionary)

word_position= dict(zip(dictionary, range(total_words)))

# def vecto_pres_words(questions, word_position):
#     vector = [0] * len(word_position)
#     for word in questions:
#         if word in word_position:
#             position = word_position[word]
#             vector[position] += 1
#     return vector
# questions = separate_words[0]

def vecto_pres_words(questions, word_position):
    vector = [0] * len(word_position)
    for word in questions:
        if word in word_position:
            position = word_position[word]
            vector[position] += 1
    return vector
vectores_questions = [vecto_pres_words(questions, word_position) for questions in separate_words]

class_question = df['classe']

x = np.array(vectores_questions)
y = np.array(class_question)

percentage_train = 0.8

train_len = int(percentage_train * len(y))
valid_len = len(y) - train_len

train = x[0:train_len]

train_y = y[0:train_len]

test = x[train_len:]
test_y = y[train_len:]

classifier = AdaBoostClassifier()

classifier.fit(train, train_y)

def pever_msg(msg):
    newmsg = msg.lower().replace('?',' ?').split()
    new_question = vecto_pres_words(newmsg,word_position)
    predictions = classifier.predict([new_question])
    
    if predictions == [0]:
        return 0
    else:
        return 1
    