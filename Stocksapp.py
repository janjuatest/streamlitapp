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
start=datetime(2021,03,01)
end=datetime(2021,04,01)

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

myBasket=['SGLB','BIOC','PHUN']

sglb=yf.download('SGLB',start=start,end=end)
bioc=yf.download('BIOC',start=start,end=end)
phun=yf.download('PHUN',start=start,end=end)

netChangeR=(sglb['Close'].iloc[-1]-sglb['Close'].iloc[0])/sglb['Close'].iloc[0]*100 
st.write('The net gain in the Sigma Labs stock is ',netChangeR,'%')
if netChangeR>1.5:
    st.header("SELL")
else:
    st.header("HOLD")  
st.line_chart(sglb['Close'])

netChangeR=(bioc['Close'].iloc[-1]-bioc['Close'].iloc[0])/bioc['Close'].iloc[0]*100
st.write('The net gain in the BIOCEPT Labs stock is ',netChangeR,'%')
if netChangeR>1.5:
    st.header("SELL")
else:
    st.header("HOLD")  
st.line_chart(bioc['Close'])


netChangeR=(phun['Close'].iloc[-1]-phun['Close'].iloc[0])/phun['Close'].iloc[0]*100
st.write('The net gain in the PhunWare Labs stock is ',netChangeR,'%')
if netChangeR>1.5:
    st.header("SELL")
else:
    st.header("HOLD")  
st.line_chart(phun['Close'])


