import pandas as pd
import requests
import streamlit as st
import numpy as np
import datetime as dt
from matplotlib import pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly
from get_data import get_data

HOURLY = 'HOURLY'
#WEEKLY = 'WEEKLY'

@st.cache(allow_output_mutation=True)
def make_forecast(selection):
    """Takes a name from the selection and makes a forecast plot."""

    if selection == HOURLY:

        cumulative_series_name = "hourly_power"
        title = "Hourly Power"
        x_label = "Time (Hourly)"
        y_label = "Power mWh"

    model = Prophet(interval_width=0.95,
    yearly_seasonality=True,
    daily_seasonality=True,
    seasonality_prior_scale=1)
    model.fit(get_data())
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    fig = model.plot(forecast, uncertainty=True)
    plt.ylim(bottom=0, top=30000)
    plt.xlim([dt.date(2021,10,1), dt.date(2021,11,1)])
    plt.title("Hourly Data with Forecast", fontsize=20)
    plt.xlabel("Date (Hourly)", fontsize=16)
    plt.ylabel("Power Output (Hourly)", fontsize=16)
    
    return fig, forecast
st.write("# Texas Wind Power Generation")

selected_series = st.sidebar.selectbox("Select a timeframe:", [HOURLY])
fig, forecast = make_forecast(selected_series)

st.pyplot(fig)

st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].iloc[-90:])