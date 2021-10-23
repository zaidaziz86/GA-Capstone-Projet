import pandas as pd
import requests
import streamlit as st
import numpy as np
from datetime import date
from matplotlib import pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly

@st.cache
def get_data():
    """
    This function will load the dataset from the 
    EIA API, resample the Dataframe based on the timeframe
    and retrun a dataframe in the way FB Prophet
    Can use.
    """
    api_key = 'b2feda39010110d402b5f247671cd0f6'
    url = 'http://api.eia.gov/series/?api_key='+ api_key +'&series_id=EBA.TEX-ALL.NG.WND.HL'
    r = requests.get(url)
    json_data = r.json()
    prof_df = pd.DataFrame(json_data['series'][0]['data'], columns=['ds', 'y'])
    prof_df.ds = pd.to_datetime(prof_df.ds, utc=True)
    prof_df['ds'] = prof_df['ds'].dt.tz_localize(None)
    return prof_df

HOURLY = 'HOURLY'
WEEKLY = 'WEEKLY'


@st.cache(allow_output_mutation=True)
def make_forecast(selection):
    """Takes a name from the selection and makes a forecast plot."""

    if selection == HOURLY:

        cumulative_series_name = "hourly_power"
        title = "Hourly Power"
        x_label = "Time (Hourly)"
        y_label = "Power mWh"

    
    prophet_df = get_data()
    model = Prophet().fit(prophet_df)
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    fig = model.plot(forecast, uncertainty=True)
    #fig.update_layout(title=title, yaxis_title=y_label , xaxis_title=x_label)


    return fig

st.write("# Texas Wind Power Generation")
selected_series = st.selectbox("Select a timeframe:", (HOURLY, WEEKLY))

plotly_fig = make_forecast(selected_series)
st.line_chart(plotly_fig)