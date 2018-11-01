import pandas as pd
def clean_station(file):
    df = pd.read_csv("./dataset/"+file)

    print(df.head())

clean_station("test_station.csv")