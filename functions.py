import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# RQ1
def parsedate(time_as_a_unix_timestamp):
  return pd.to_datetime(time_as_a_unix_timestamp, unit = 's')

# RQ3
def orario(lista):
    dataset_sub = pd.read_csv("steam_reviews.csv",
                      index_col=0,
                      usecols=[0,6],
                      parse_dates=['timestamp_created'],
                      date_parser=parsedate)
    time_col = np.array(dataset_sub["timestamp_created"].dt.time)
    list_time = [datetime.strptime(t, '%H:%M:%S').time() for t in lista]
    number_review = []
    for i in range(0, len(list_time), 2):
        number_review.append(len((time_col[(time_col >= list_time[i]) & (time_col <= list_time[i + 1])])))
    xx = []
    for i in range(0, len(list_time), 2):
        xx.append(str(list_time[i].hour))
    #xx = ['6am', '11am', '2pm', '5pm', '8pm', '12am', '3am']
    plt.bar(xx, number_review, color = 'salmon')
    plt.yscale('log')
    plt.yticks([2000000, 2500000, 3000000, 3500000, 4000000])
    plt.title('Number of review for each interval of time')
    plt.xlabel('Intervals')
    plt.ylabel('Number of review')
    plt.show()

# RQ4
def get_reviews_by_languages(data, lingue):
    return data[data.language.isin(lingue)]
