from __future__ import division
import numpy as np
# import bayesian_changepoint_detection.offline_changepoint_detection as offcd
from functools import partial
import matplotlib.pyplot as plt

import pandas as pd

# Load each CSV file into a DataFrame
df1 = pd.read_csv('./data/local2itens.csv')
df2 = pd.read_csv('./data/propagate2itens.csv')
df3 = pd.read_csv('./data/alternate2itens.csv')
df4 = pd.read_csv('./data/sharding2itens.csv')

df36_2 = pd.read_csv('./data/propagate36itens.csv')
df36_1 = pd.read_csv('./data/local36itens.csv')
df36_3 = pd.read_csv('./data/alternate36itens.csv')
df36_4 = pd.read_csv('./data/sharding36itens.csv')


# Concatenate the DataFrames vertically (one after another)
combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

combined_36df = pd.concat([df36_1, df36_2, df36_3, df36_4], ignore_index=True)

# Optionally, save the combined DataFrame to a new CSV file
combined_df.to_csv('combined_file.csv', index=False)

combined_36df.to_csv('combined_36file.csv', index=False)


# # Filter rows where 'Series' is 'Current Action Time'
# filtered_df = combined_df[combined_df['Series'] == 'Current Action Time']

# # Extract the 'Average Time (ms)' as the signal for changepoint detection
# signal_data = filtered_df['Average Time (ms)'].values

# # Apply Bayesian changepoint detection
# Q, P, Pcp = offcd.offline_changepoint_detection(
#     signal_data,
#     partial(offcd.const_prior, l=(len(signal_data) + 1)),
#     offcd.gaussian_obs_log_likelihood,
#     truncate=-40  # Truncate to improve computational efficiency
# )

# # Extract the changepoints based on a threshold
# changepoints = np.where(Pcp > 0.5)[0]  # You can adjust the threshold

# # Display the changepoints
# print("Detected changepoints at indices:", changepoints)

# # Plot the results
# plt.plot(signal_data, label='Current Action Average Time')
# for cp in changepoints:
#     plt.axvline(cp, color='r', linestyle='--', label=f'Changepoint {cp}')
# plt.legend()
# plt.show()