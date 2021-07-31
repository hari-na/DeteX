import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from math import sqrt
from sklearn.metrics import mean_squared_error
from joblib import Parallel, delayed
import sys

df_test = pd.read_csv("TestData.csv")
print(df_test.head)

df_test = df_test.fillna(0)


df_test.Week = df_test/100


x_test = df_test.drop('Inflow', axis = 1)
y_test = df_test['Inflow']


scaler = MinMaxScaler(feature_range=(0, 1))
x_test_scaled = scaler.fit_transform(x_test)
x_test = pd.DataFrame(x_test_scaled)

knn_model = joblib.load('knn_model')


print("Size of KNN Model" + str(sys.getsizeof(knn_model)))
pred = knn_model.predict(x_test)


error = sqrt(mean_squared_error(y_test,pred))
print(pred)


results = pd.DataFrame()

results['pred'] = pred
results['true'] = y_test.values

plt.plot(range(results.shape[0]), results.pred, label = "PREDICTION")
plt.plot(range(results.shape[0]), results.true, label = "TRUE")
plt.show()