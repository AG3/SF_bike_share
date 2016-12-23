database.sqlite 		--- All data from 2013 to 2015
demo.py 				--- Sample in python
exclude_variance.py 	--- Drop data which variance lower/higher than 5% of the highest variance
view_by_weekday.py 		--- Do statistics on trip count of weekday
correct_date_format.py 	--- Convert date format from m/d/y to yyyy-mm-dd in database
view_by_station.py 		--- Do statistics on each station's trip count of weekday

********************************

Output file naming format:
[col1_name]_[col2_name]_[etc].[condition]

********************************

Abbreviation:
How many trip took place -> tripCount
Mon,Tue,Wed... -> weekday
The index of stations -> stationId

julian day offset: 2456533