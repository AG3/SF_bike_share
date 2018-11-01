import pandas as pd

def cleanData(file):
    train_trip = pd.read_csv("./dataset/"+file)
    # Convert Second to Minute
    train_trip.duration /= 60

    # print(train_trip.duration.describe())

    train_trip.start_date = pd.to_datetime(train_trip.start_date, format='%m/%d/%Y %H:%M')
    # New col to store date only
    train_trip['date'] = train_trip.start_date.dt.date

    # Count trips by date
    dates = {}
    for d in train_trip.date:
        if d not in dates:
            dates[d] = 1
        else:
            dates[d] += 1

    # Create Dataframe, one record per row (orient index)
    fullTrainData = pd.DataFrame.from_dict(dates, orient="index", columns=['trips'])
    fullTrainData['date'] = fullTrainData.index
    fullTrainData = fullTrainData.sort_values(by=['date'])
    fullTrainData.reset_index(drop=True, inplace=True)
    print(fullTrainData)

    f = open("./cleaned_data/"+file, "w+")

    fullTrainData.to_csv(f, index=False)
    f.close()


cleanData("train_trip.csv")
