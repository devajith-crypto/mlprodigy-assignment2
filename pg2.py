import joblib
model=joblib.load("modelwind.pkl")
windspeed=float(input("Enter wind speed:"))
bladeangle=float(input("Enter blade angle:"))
rotorspeed=float(input("Enter rotor speed:"))
predicted_power=model.predict([[windspeed,bladeangle,rotorspeed]])
print("predicted power output:",predicted_power[0],"kW")
