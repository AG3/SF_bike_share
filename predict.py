import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures

infile = open('single_3_tripCount','r')

avr = 0

train_X = []
train_Y = []

ind = 0
for i in infile:
	train_X.append(ind)
	y = int(i.split(' ')[1])
	train_Y.append(y)
	plt.scatter(ind,y)
	ind+=1

X_np = np.array(train_X).reshape(-1,1)
Y_np = np.array(train_Y).reshape(-1,1)


poly = PolynomialFeatures(5)
b = poly.fit_transform(X_np)

regr = linear_model.LinearRegression()

regr.fit(b, train_Y)

print 'Coefficients:\n', regr.coef_
print 'Intercept:\n', regr.intercept_

res = regr.predict(b)

plt.plot(train_X, res, color='blue',linewidth=3)

plt.show()