from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import json
import requests

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# github token
token = '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'
headers = {'Authorization' : 'token ' + token }
url = 'https://raw.githubusercontent.com/shrayv/test/main/company_tickers.json?token=GHSAT0AAAAAACEIPXINF56ZV2F2IUESRYTKZE2YJAA'
response = requests.get(url, headers=header)
companylist=pd.json_normalize(list(response.json().values()))


option = st.selectbox(
    'Select Company',
    (data['ticker']))

st.write('You selected:', option)
