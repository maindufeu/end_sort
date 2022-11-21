import streamlit as st
import requests
import json
import subprocess
from datetime import date
import numpy as np
import pandas as pd

DATA_URL = ('https://waop.s3.amazonaws.com/sort.csv')
st.title('Sorteo de fin de año')
st.dataframe(pd.read_csv(DATA_URL))
