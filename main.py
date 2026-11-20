import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("Dataset-SolarTechLab.csv", sep=";")

df = df.dropna()

# convert time to numeric
df['Time'] = pd.to_datetime(df['Time'])
df['Time'] = df['Time'].astype('int64') // 10**9

X = df[['Time','PV_Power','T_air','G_h','G_tilt','W_s','W_d']]
y = df['PV_Power']

model = LinearRegression()
model.fit(X, y)

with open("model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model trained successfully")