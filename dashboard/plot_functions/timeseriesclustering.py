from plotly.subplots import make_subplots
import pandas as pd

def plot(var, multi_time_cluster_wk):
    cluster_count = 4
    timestamp_10min = timestamp_10min = pd.date_range(start='2021-03-01', end='2021-03-08', freq="10min")[:-1]

    fig = make_subplots(rows=cluster_count, cols=1, subplot_titles=('Cluster 0',  'Cluster 1', 'Cluster 2', 'Cluster 3'))
    graph_id = 1
    for clu_id in range(len(multi_time_cluster_wk.cluster_id.unique())):
        fig.add_scatter(x=timestamp_10min, 
                        y=multi_time_cluster_wk[multi_time_cluster_wk.cluster_id==clu_id][var], 
                        row=graph_id, col=1)
        graph_id += 1
    
    # edit axis labels
    fig['layout']['xaxis']['title']='time'
    fig['layout']['xaxis2']['title']='time'
    fig['layout']['xaxis3']['title']='time'
    fig['layout']['xaxis4']['title']='time'
    fig['layout']['yaxis']['title']='Battery Voltage (V)'
    fig['layout']['yaxis2']['title']='Battery Voltage (V)'
    fig['layout']['yaxis3']['title']='Battery Voltage (V)'
    fig['layout']['yaxis4']['title']='Battery Voltage (V)'

    fig.update_layout(
        height=1000,
        width=1000
    )
    return fig