# -*- coding: utf-8 -*-
"""LVADSUSR183_SajjaTarunTeja_FLab2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mdSVLQUYTGDOFeW7T3_hurFUF7IaZmDw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("/content/penguins_classification.csv")

df.head()

df.info()

df.isna().sum()
# 8 Null values in bill_depth_mm

df.species.unique()

df.island.unique()

rc = []
for i in df["species"]:
  if i=="Adelie":
    rc.append(1)
  else:
    rc.append(0)

rc = np.array(rc)
df["nspecies"] = rc

df.head()

df.duplicated().sum()
# No duplicates

df = df.drop(["species"],axis=1)

X = df.drop(["nspecies"],axis=1)
y = df["nspecies"]

nX = pd.get_dummies(X["island"],columns=["island"])

nX = nX.applymap(lambda x: 1 if x>0 else 0)

X = X.drop(["island"],axis=1)

X = X.fillna(0,axis=1)
X = pd.concat([X,nX],axis=1)

X = pd.DataFrame(X)

X.head()

X.isna().sum()

col = X.columns

X.info()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

RF_clf = RandomForestClassifier()
RF_clf.fit(X_train,y_train)
y_pred = RF_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("RandomForest  Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

xgb_clf = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
xgb_clf.fit(X_train, y_train)
y_pred = xgb_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("XGB Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

