import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

batch_size = 1
epochs = 1
look_back = 16
train_set_rate = 0.8

predict_length = 100

def get_data(xn=733):
    f = open('./days_tripCount')
    dataset = np.zeros((xn, 1))
    ind = 0
    for i in f:
        dataset[ind,0] = int(i.split(' ')[1])
        ind+=1
    return dataset

def build_data(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX), np.array(dataY)

def save_to_file(data, filename, offset):
    f = open(filename, 'w+')
    for i in range(offset):
        f.write('-1\n')
    for i in data:
        f.write(str(i)+'\n')

print('Generating Data')


raw = get_data()
train_set_length = int(len(raw)*train_set_rate)
cos = raw[:train_set_length]
scaler = MinMaxScaler(feature_range=(0, 1))
cos = scaler.fit_transform(cos)
print('Input shape:', cos.shape)

trainX, trainY = build_data(cos, look_back)

print('Output shape')
print(trainY.shape)

print('Creating Model')
model = Sequential()
model.add(LSTM(output_dim=100,
               batch_input_shape=(batch_size, look_back, 1),
               stateful=True))

model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

print('Training')
for i in range(epochs):
    print('Epoch', i, '/', epochs)
    model.fit(trainX,
              trainY,
              batch_size=batch_size,
              verbose=1,
              nb_epoch=1,
              shuffle=False)
    model.reset_states()

#model.save('weights.lstm')

print('Predicting')
predicted_output = model.predict(trainX, batch_size=batch_size)

preX = []
preX.append(trainX[len(trainX) - 1])
preX = np.array(preX)

predictY = []
for i in range(predict_length):
    t = model.predict(preX, batch_size=batch_size)
    predictY.append(t[0])

    for j in range(look_back - 1):
        preX[0,j,0] = preX[0,j+1,0]

    preX[0,look_back - 1,0] = t

print('Plotting Results')

plt.plot(scaler.fit_transform(raw))

plt_p_x = range(look_back, train_set_length - 1)
plt_p_y = predicted_output.flatten()

save_to_file(plt_p_y, 'trainset_prediction', look_back)
save_to_file(np.array(predictY).flatten(), 'true_prediction', train_set_length - 2)

plt.plot(plt_p_x, plt_p_y, color='red')
plt.plot(range(train_set_length - 2,train_set_length + len(predictY) - 2),predictY, color='green')
plt.title('Predicted')
plt.show()