# Required Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nltk.tokenize import RegexpTokenizer
from nltk import WordNetLemmatizer

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Import model(s) of choice

from sklearn.naive_bayes import MultinomialNB

# Read in training and testing message data



train = pd.read_csv(filepath)
test = pd.read_csv(filepath)

# Dropping columns that will not be used (not well distributed)

train = train.drop(columns = ['id', 'split', 'original', 'tools', 'child_alone', 'PII'])

# Creating a target variable

need_help = []
for row in range(train.shape[0]):
    val = 0
    for i in train.columns[3:35]:
        if train[i][row] == 1 and train['genre'][row] == 'direct':
            val = 1
    need_help.append(val)
print(len(need_help))

train['need_help'] = need_help

# Message processing

def tokenize(x):
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(x)

train['tokens'] = train['message'].map(tokenize)
test['tokens'] = test['message'].map(tokenize)
    
def lemmatize(x):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in x])

train['lemma'] = train['tokens'].map(lemmatize)
test['lemma'] = test['tokens'].map(lemmatize)

# X and Y for modelling (split already done)

X = train['lemma']
y = train['need_help']

X_test = test['lemma']
y_test = test['need_help']


# Modelling and gridsearch (Naive bayed used as an example)

pipe_nb = Pipeline(steps = [('tf', TfidfVectorizer()), ('nb', MultinomialNB())])

pgrid_nb = {
    'tf__max_features' : [2000, 3000, 5000],
    'tf__stop_words' : ['english', None],
    'tf__ngram_range' : [(1,2), (1,2)],
    'tf__use_idf' : [True, False],
    'nb__alpha' : [0.1, 0.5, 1]
}

gs_nb = GridSearchCV(pipe_nb,pgrid_nb,cv=5,n_jobs=-1, verbose=1)

gs_nb.fit(X, y)

gs_nb.score(X, y)

gs_nb.score(X_test, y_test)

# Read in tweets

tweets = pd.read_csv(filepath)

# Tweet Processing

tweets['tokens'] = tweets['tweet'].map(tokenize)
    
tweets['lemma'] = tweets['tokens'].map(lemmatize)

# Predicting tweet labels

X = tweets['lemma']

preds = gs_nb.predict(X)

tweets['need_help'] = preds
