from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
import pandas as pd


train = pd.read_csv("./cleaned_data/merged_trip.csv")
train.date = pd.to_datetime(train.date, format='%Y/%m/%d')

calendar = USFederalHolidayCalendar()
holidays = calendar.holidays(start=train.date.min(), end=train.date.max())
us_bd = CustomBusinessDay(calendar=USFederalHolidayCalendar())
business_days = pd.DatetimeIndex(start=train.date.min(), end=train.date.max(), freq=us_bd)
business_days = pd.to_datetime(business_days, format='%Y/%m/%d').date
holidays = pd.to_datetime(holidays, format='%Y/%m/%d').date

# If the day is not business day, its holiday.
train['business_day'] = train.date.isin(business_days)

# Pretty much useless according to common sense. Because it does not include weekend.
# train['holiday'] = train.date.isin(holidays)

# I guess put -1 rather than 0 is better for indicating the attribute of holidays
train.business_day = train.business_day.map(lambda x: 1 if x is True else -1)

train['year'] = pd.to_datetime(train['date']).dt.year
train['month'] = pd.to_datetime(train['date']).dt.month
train['weekday'] = pd.to_datetime(train['date']).dt.weekday
# Get rid of zeros, makes me feel better
train.weekday = train.weekday + 1

train = train.drop(['date'], 1)

train.to_csv("./cleaned_data/complete_trip.csv", index=False)
