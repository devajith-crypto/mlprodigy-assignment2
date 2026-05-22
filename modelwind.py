import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

data=pd.read_csv("dataset.csv")
x=data[["Wind_Speed","Blade_Angle","Rotor_Speed"]]
y=data["Power_Output"]

model=LinearRegression()
model.fit(x,y)
print("coefficients:",model.coef_)
print("intercept:",model.intercept_)

joblib.dump(model,"modelwind.pkl")
print("training completed and model has been saved as modelwind.pkl")
