import streamlit as st
import requests
import json
import subprocess
from datetime import date
import numpy as np
import pandas as pd
#import plotly.figure_factory as ff
#import graphviz as graphviz
######################################################################################################################################
DATE_COLUMN = 'daily'
DATA_URL = ('https://waop.s3.amazonaws.com/sort.csv')
#datastreams_id = [6,63,101,89,98,97,99]
datastreams_id = []
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
######################################################################################################################################
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

######################################################################################################################################

st.title('Sorteo de fin de año')

st.dataframe(data.style.highlight_max(axis=0))

st.write('última actualización de datos')
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")
######################################################################################################################################
if st.button('Raw data'):
    st.subheader('Raw data')
    st.write(data)
