# -*- coding: utf-8 -*-
"""LVADSUSR183_SajjaTarunTeja_FLab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QEoj5-KfJydX4OiMJqwUkwkjK8X3_S7W
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/Fare prediction.csv")

df.head()

df.info()

df.isna().sum()
# No Null values

df.duplicated().sum()
# No duplicates

df = df.drop(["key","pickup_datetime"],axis=1)

df.head()

#for i in ndf.columns:
#  sns.pairplot(ndf[[i]],kind="box")
#  plt.show()

col = ["fare_amount","pickup_longitude",
       "pickup_latitude","dropoff_longitude","dropoff_latitude",
       "passenger_count"]



# Removing Outliers
for column in col:
  print(column)
  Q1 = df[column].quantile(0.25)
  Q3 = df[column].quantile(0.75)
  IQR = Q3 - Q1
  lb = Q1-1.5*IQR
  ub = Q3+1.5*IQR
  df = df[(df[column] > lb) & (df[column] < ub)]

df.head()

mm = StandardScaler()
sdf = pd.DataFrame(mm.fit_transform(df),columns=col)

sdf.head()

X = sdf.drop(["fare_amount"],axis=1)
y = sdf["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

RF_reg = RandomForestRegressor()
RF_reg.fit(X_train,y_train)
y_pred = RF_reg.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, y_pred)
print("Random Forest \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)
