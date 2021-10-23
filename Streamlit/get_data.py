import pandas as pd
import streamlit as st
import requests
from datetime import date

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
