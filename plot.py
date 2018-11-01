import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv("./cleaned_data/train_trip.csv")

print(train.head())
fs = 16
plt.figure(figsize=(8,5))
plt.plot(train.index)
plt.plot(train.trips)
plt.legend(['Prediction', 'Acutal'])
plt.ylabel("Number of Trips", fontsize = fs)
plt.xlabel("Predicted Date", fontsize = fs)
plt.title("Predicted Values vs Actual Values", fontsize = fs)
plt.show()
