import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures

infile = open('single_3_tripCount','r')

avr = 0

train_X = []
train_Y = []
test_X = []
ind = 0
for i in infile:
	train_X.append(ind)
	test_X.append(ind)
	y = int(i.split(' ')[1])
	train_Y.append(y)
	plt.scatter(ind,y)
	ind+=1


for i in range(ind, ind+20):
	test_X.append(i)

X_np = np.array(train_X).reshape(-1,1)
Y_np = np.array(train_Y).reshape(-1,1)
test_np = np.array(test_X).reshape(-1,1)

poly = PolynomialFeatures(5)
b = poly.fit_transform(X_np)z
test_b = poly.fit_transform(test_np)

regr = linear_model.LinearRegression()

regr.fit(b, train_Y)

print 'Coefficients:\n', regr.coef_
print 'Intercept:\n', regr.intercept_

res = regr.predict(test_b)

plt.plot(test_X, res, color='blue',linewidth=3)

plt.show()