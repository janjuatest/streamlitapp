# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:16:48 2021

@author: DELL
"""
import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
st.write("""
# This is my first app for following Stocks. The suggestions are RANDOM and should not be followed
Select your reference to compare with my selected stocks
""")
start=datetime(2021,3,1)
end=datetime(2021,4,1)

ticker = st.select_slider(
     'Select a Reference from Tesla, Apple, Bitcoin or Nasdaq',
     options=['TSLA','AAPL','BTC-USD','^IXIC'])

st.write('My Reference is', ticker)

stock=yf.download(ticker,start=start,end=end)

st.write("""
## Closing Value of Reference
""")
st.subheader(ticker)
st.line_chart(stock['Close'])

netChangeR=(stock['Close'].iloc[-1]-stock['Close'].iloc[0])/stock['Close'].iloc[0]*100
st.write('The net gain in the reference stock is ',netChangeR,'%')


st.write("""
## These are my stocks
""")

myBasket=['SGLB','BIOC','ATOS','GNUS','VNTR','GEVO','LXRX']

for ticker in myBasket:
    df=yf.download(ticker,start=start,end=end)
    netChangeR=(df['Close'].iloc[-1]-df['Close'].iloc[0])/df['Close'].iloc[0]*100
    st.write('The net gain for ', ticker ,' ',netChangeR,'%')
    if netChangeR>200:
        st.header("SELL")
    else:
        st.header("HOLD")  
    st.line_chart(df['Close'])




