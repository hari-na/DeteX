import pandas as pd, numpy as np, art
from scipy.sparse.construct import random
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from math import sqrt
from xgboost.sklearn import XGBRegressor
from externalModules import isitanint, severityCheck
from art import tprint

df = pd.read_excel("CAT_Training_Dataset_V3 File.xlsx")
tprint("Data\tLoaded")
df = df.drop(['ID'], axis = 1)
print(df.head())
a = len(df)
print(len(df))

## Cleaning Candidate Column

df['candidate'] = df['candidate'].str[5:]
df['candidate'] = df['candidate'].apply(np.int64)

## Cleaning Date Column

df = df[df.date.apply(lambda x: isitanint(x))]
df['date'] = df['date'].apply(np.int64)

## Cleaning Units Column

df = df[df.units.apply(lambda x: isitanint(x))]
df['units'] = df['units'].apply(np.int64)

## Creating Sub Events Column

df['subEvent'] = df.event.apply(lambda x: pd.Series(str(x).split("_")[-1]))
df = pd.get_dummies(df, columns=["subEvent"])

## Cleaning Events Column

df['event'] = df['event'].str[9:]
df['event'] = df.event.apply(lambda x: pd.Series('_'.join(str(x).split("_")[0:2])))
df = pd.get_dummies(df, columns=["event"])

## Cleaning Occur Count Column

df = df[df.occur_count.apply(lambda x: isitanint(x))]
df['occur_count'] = df['occur_count'].apply(np.int64)

## Cleaning Severity Level

df = df[df.svrty_level.apply(lambda x: isitanint(x))]
df = df[df.svrty_level.apply(lambda x: severityCheck(x))]
df['svrty_level'] = df['svrty_level'].apply(np.int64)

print(df.head())


x = df.drop('date', axis = 1)
y = df['date']
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state = 32)

print(x.shape, y.shape, X_train.shape, Y_train.shape)

clf = XGBRegressor(verbosity = 3)
clf = clf.fit(X_train, Y_train)
pred = clf.predict(X_test)
error = sqrt(mean_squared_error(Y_test, pred))
print(error)

# model = neural_network
# model.fit(x_train, y_train)  #fit the model
# joblib.dump(model,'knn_model')