import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay
from sklearn.metrics import mean_squared_error, median_absolute_error
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from pandas.tseries.holiday import USFederalHolidayCalendar
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeRegressor


train = pd.read_csv("./cleaned_data/merged_trip.csv")


calendar = USFederalHolidayCalendar()
holidays = calendar.holidays(start=train.date.min(), end=train.date.max())
us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
business_days = pd.DatetimeIndex(start=train.date.min(), end=train.date.max(), freq=us_bd)
business_days = pd.to_datetime(business_days, format='%Y/%m/%d').date
holidays = pd.to_datetime(holidays, format='%Y/%m/%d').date

train['business_day'] = train.date.isin(business_days)
train['holiday'] = train.date.isin(holidays)

train.business_day = train.business_day.map(lambda x: 1 if x == True else 0)
train.holiday = train.holiday.map(lambda x: 1 if x == True else 0)

train['year'] = pd.to_datetime(train['date']).dt.year
train['month'] = pd.to_datetime(train['date']).dt.month
train['weekday'] = pd.to_datetime(train['date']).dt.weekday

labels = train.trips
train = train.drop(['trips', 'date'], 1)


X_train, X_test, y_train, y_test = train_test_split(train, labels, test_size=0.33, shuffle=False)

def scoring(clf):
    scores = cross_val_score(clf, X_train, y_train, cv=15, n_jobs=1, scoring = 'neg_median_absolute_error')
    print (np.median(scores) * -1)


# rfr = RandomForestRegressor(n_estimators = 55,
#                             min_samples_leaf = 3,
#                             random_state = 2)

rfr = GradientBoostingRegressor(learning_rate = 0.12,
                                n_estimators = 150,
                                max_depth = 8,
                                min_samples_leaf = 1,
                                random_state = 2)
scoring(rfr)


rfr = rfr.fit(X_train, y_train)
rfr_preds = rfr.predict(X_test)



print ("Daily error of trip count:", median_absolute_error(y_test, rfr_preds))

y_test.reset_index(drop = True, inplace = True)

fs = 16
plt.figure(figsize=(8,5))
plt.plot(rfr_preds)
plt.plot(y_test)
plt.legend(['Prediction', 'Acutal'])
plt.ylabel("Number of Trips", fontsize = fs)
plt.xlabel("Predicted Date", fontsize = fs)
plt.title("Predicted Values vs Actual Values", fontsize = fs)
plt.show()
