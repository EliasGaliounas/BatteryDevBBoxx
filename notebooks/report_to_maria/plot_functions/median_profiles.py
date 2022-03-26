import pandas as pd
import numpy as np
import plotly.express as px

def prepare_data(df, resample = True):
    df=df.copy()
    if resample == True:
        df = df.groupby('battery_id').resample('10min').mean()
        df = df.drop('battery_id', axis = 1)

        df = df.reset_index().set_index('timestamp')

    df['hour'] = df.index.hour
    df['minutes'] = df.index.minute
    df['day_n'] = df.index.weekday

    return df

def plot(field, n_batteries, df):
    freq_group_by = ['hour','minutes'] #also ['day_n','hour','minutes']
    agg_method = 'mean'

    DF = prepare_data(df[[field,'battery_id']])
    randoms_ids = np.random.choice(DF.battery_id.unique(), n_batteries)
    subset = DF[DF['battery_id'].isin(randoms_ids)]

    df_median = subset.groupby(['battery_id'] + freq_group_by).agg(agg_method)
    df_plot = df_median.reset_index().set_index(freq_group_by)#[[field]].unstack(level = 0).sort_index()
    df_plot.index = df_plot.index.map('{0[0]}H{0[1]}'.format) 
    fig = px.line(df_plot, y = field, color = 'battery_id', title = f'Median {field} profile')
    fig.update_layout(title_x = 0.5, plot_bgcolor = '#d2d9d7', showlegend=False)
    return fig