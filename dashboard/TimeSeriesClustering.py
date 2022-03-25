import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import math
from tslearn.clustering import TimeSeriesKMeans
import numpy as np

def cluster(data):
#     ts1_df = pd.read_csv('../data/devices1.csv')
#     ts2_df = pd.read_csv('../data/devices2.csv')
#     ts3_df = pd.read_csv('../data/devices3.csv')
#     ts4_df = pd.read_csv('../data/devices4.csv')
#     data = pd.concat([ts1_df, ts2_df, ts3_df, ts4_df], axis = 0, ignore_index = True)

    variable_to_analyse = "battery_voltage"
    frequency = "weekly"  # Either daily, weekly, monthly or seasonally

    # Converting data timestamp in datetime objects
    data.timestamp = pd.to_datetime(data.timestamp)
    # Keeping only studied variables
    data = data[["timestamp", variable_to_analyse, "battery_id"]]
    # Setting date column as index
    data.set_index("timestamp", inplace=True)

    # TODO selecting specific time intervals
    begin_dt = "2021-05-02 00:00:00"
    end_dt = "2021-05-08 23:59:59"
    # Selecting study time intervals
    data = data.loc[(data.index > pd.Timestamp(begin_dt)) & (data.index < pd.Timestamp(end_dt))]

    bat_df = []  # List to store every battery dataframe
    for i in range(len(data.battery_id.unique())):
        bat_df.append(data.loc[data.battery_id == i][variable_to_analyse])  # Storing specific battery id dataframe

    series_lengths = {len(series) for series in bat_df}  # Serie length of every battery dataframe
    max_len = max(series_lengths)  # max lenght amongst all series
    longest_series = None
    for series in bat_df:
        if len(series) == max_len:
            longest_series = series

    problems_index = []  # Finding battery indexes that need to be re-indexed to the longest time serie
    for i in range(len(bat_df)):
        # Time series that aren't as long as the largest one need to be reindexed
        if len(bat_df[i]) != max_len:
            problems_index.append(i)
            # Values are reindexed to the nearest (1 min tolerance) time index of the longest time serie
            bat_df[i] = bat_df[i].reindex(index=longest_series.index, method='nearest', tolerance='1min')

    # Values who couldn't be reindexed or gaps are filled using interpolation
    for i in problems_index:
        bat_df[i].interpolate(limit_direction="both", inplace=True)

    # Rule of thumb : choosing k as the square root of the number of points
    # cluster_count = math.ceil(math.sqrt(len(bat_df)))
    cluster_count = 6

    # Time series specific clustering algorithm
    km = TimeSeriesKMeans(n_clusters=cluster_count, metric="euclidean")  # dtw metric takes way too long...
    # Predict closest cluster for each time series
    labels = km.fit_predict(bat_df)

    return longest_series, cluster_count, labels, km, bat_df

# # Larger plots showing inline
# plt.rcParams["figure.figsize"] = (20,15)

# fig, axs = plt.subplots(len(set(labels)))
# fig.tight_layout()

# for label in set(labels):
#     for i in range(len(data.battery_id.unique())):
#         if(labels[i]==label):
#             axs[label].set_title("Cluster {}".format(label))
# #             axs[label].set_ylabel(variable_to_analyse)
#             axs[label].plot(bat_df[i], c="gray", alpha=0.4)
#     axs[label].plot(longest_series.index, km.cluster_centers_[label], c="red")
# plt.xlabel("Time")
# plt.subplots_adjust(hspace=0.5)