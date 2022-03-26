import pandas as pd
import plotly.express as px

def plot(selected_var, resampling, df):
    mean_per_freq = df[[selected_var,'battery_id']].groupby('battery_id').resample(resampling)[selected_var].agg('mean')
    mean_per_freq = mean_per_freq.reset_index()
    mean_per_freq['timestamp'] = mean_per_freq['timestamp'].dt.date
    mean_per_freq = mean_per_freq.sort_values('timestamp')
    fig = px.box(mean_per_freq, x = 'timestamp', y = selected_var, title = f'Mean {selected_var} per battery per month')
    fig.update_layout(title_x = 0.5, plot_bgcolor = '#d2d9d7')
    return fig