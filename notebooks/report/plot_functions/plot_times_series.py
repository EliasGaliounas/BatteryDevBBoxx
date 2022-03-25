import numpy as np
import plotly.express as px

def plot(n_batteries, selected_var, resampling, df):
    randoms_ids = np.random.choice(df.battery_id.unique(), n_batteries)
    df_plot = df[df['battery_id'].isin(randoms_ids)].sort_index()
    df_plot = df_plot.groupby('battery_id').resample(resampling).mean()[selected_var]
    line_fig = px.line(df_plot.reset_index(), x = 'timestamp', y = selected_var, color = 'battery_id')

    return line_fig