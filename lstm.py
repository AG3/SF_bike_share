from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Flatten
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv("./cleaned_data/complete_trip.csv")
labels = data.trips
data.drop(['trips'], 1)

X_tr, X_te, y_train, y_test = train_test_split(data, labels, test_size=0.33, shuffle=False)
SubLen = 64

def MakeSamples(raw):
    raw = np.asarray(raw)
    d = []
    l = len(raw)
    # print(raw)
    for i in range(0, l - SubLen):
        d.append(raw[i:i+SubLen])
        #print(d[-1])
    # print(len(d))
    return np.asarray(d)

X_test = MakeSamples(X_te)
X_train = MakeSamples(X_tr)

y_test = np.asarray(y_test[SubLen:])
y_train = np.asarray(y_train[SubLen:])

print(X_test.shape,y_test.shape)
print(X_train.shape,y_train.shape)
# X_test = np.asarray()
# X_test = X_test.reshape(-1, 1, 5)
# print(X_test.shape)
# X_train = np.asarray(MakeSamples(X_tr))
# X_train = X_train.reshape(-1, 1, 5)
# print(X_train.shape)


model = Sequential()
# model.add(LSTM(units=32, input_shape=(None, 5)))
model.add(Dense(units=32, input_shape=(SubLen, 5)))
model.add(Dense(units=1))

model.add(Activation("softmax"))
model.add(Flatten())
model.add(Dense(units=1))


model.compile(loss='mean_squared_error',
              optimizer='sgd',
              metrics=['accuracy'])

model.summary()
model.fit(X_train, y_train, epochs=5000, batch_size=32)


#scores = model.evaluate(X_test, y_test, verbose=0)
#print("Model Accuracy: %.2f%%" % (scores[1]*100))
