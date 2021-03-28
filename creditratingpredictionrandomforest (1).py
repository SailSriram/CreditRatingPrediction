# -*- coding: utf-8 -*-
"""CreditRatingPredictionRandomForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AG-Iae864qKGKe2OMUvKV-E_bRUkMbXp
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

col_desc = pd.read_csv("columns_description.csv")
for i in range(122,160):
  print(col_desc["Description"].iloc[i])

"""# Trained on few features"""

app_data_0 = pd.read_csv("X_train(num1).csv")
app_data_0.head()

y_0 = app_data_0['TARGET']
ids_0 = app_data_0['SK_ID_CURR']
X_0 = app_data_0.drop(columns=['TARGET','SK_ID_CURR','Unnamed: 0'])

X_train_0, X_test_0, y_train_0, y_test_0 = train_test_split(X_0, y_0, test_size = 0.2)

forest_0 = RandomForestClassifier(n_estimators = 50, verbose=1)
forest_0.fit(X_train_0, y_train_0)

y_trainset_pred_0 = forest_0.predict(X_train_0)
y_pred_0 = forest_0.predict(X_test_0)

print("Forest Train Accuracy: ", metrics.accuracy_score(y_train_0, y_trainset_pred_0))
print("Forest Test Accuracy: ", metrics.accuracy_score(y_test_0, y_pred_0))

"""# Trained on higher number of features


"""

app_data_1 = pd.read_csv("X_train(num2).csv")
app_data_1.head()

y_1 = app_data_1['TARGET']
ids_1 = app_data_1['SK_ID_CURR']
X_1 = app_data_1.drop(columns=['TARGET','SK_ID_CURR'])

X_11, X_eval, y_11, y_eval = train_test_split(X_1, y_1, test_size = .00005, random_state=32)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X_11, y_11, test_size = 0.2)
pd.pandas.set_option("display.max_columns", None)
print(X_eval)
y_eval

forest_1 = RandomForestClassifier(n_estimators = 50, verbose=1)
forest_1.fit(X_train_1, y_train_1)

y_trainset_pred_1 = forest_1.predict(X_train_1)
y_pred_1 = forest_1.predict(X_test_1)

print("Forest Train Accuracy: ", metrics.accuracy_score(y_train_1, y_trainset_pred_1))
print("Forest Test Accuracy: ", metrics.accuracy_score(y_test_1, y_pred_1))

