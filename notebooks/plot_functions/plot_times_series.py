import numpy as np
import plotly.express as px

def plot(n_batteries, selected_var, rolling, df):
    randoms_ids = np.random.choice(df.battery_id.unique(), n_batteries)
    df_plot = df[df['battery_id'].isin(randoms_ids)].sort_index()
    df_plot = df_plot.groupby('battery_id')[selected_var].resample(rolling).mean()
    line_fig = px.line(df_plot.reset_index(), x = 'timestamp', y = selected_var, color = 'battery_id', title = 'Raw time series')
    line_fig.update_layout(title_x = 0.5)
    #, plot_bgcolor = '#d2d9d7')
    return line_fig