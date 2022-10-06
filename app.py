import requests
import json
import time
import os
import streamlit as st
import pandas as pd

#st.set_page_config(layout="centered", page_icon="🕵️", page_title="LearnApp Strategy Scanner")

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

st.title("LearnApp Strategy Scanner")

strategy_name = st.selectbox('Select the strategy', ['52 week high strategy', 'Gapup Strategy','Mean Reversion Strategy'])

if st.button('Scan Stocks'):
    with st.spinner('abra-ca-dabra 🎩 ... '):

        if strategy_name == "52 week high strategy":
                
            api_url = "https://je1joyu2ga.execute-api.ap-south-1.amazonaws.com/stocks"
            payload = {}
            headers= {}
            response_mr = requests.request("GET", api_url, headers=headers, data = payload)
            data = json.loads(response_mr.text)
            st.text("")
            df = pd.DataFrame(data['stocks'])
            df.rename(columns = {'tradingSymbol':'Stock Name'}, inplace = True)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.caption("Trade Date: " + data['date'])
            st.table(df['Stock Name'])

            st.write("To understand the rules of the strategy, watch the complete course [here](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
        
        elif strategy_name == "Gapup Strategy":

            api_url = "https://92tkljm29i.execute-api.ap-south-1.amazonaws.com/stocks"
            payload = {}
            headers= {}
            response_mr = requests.request("GET", api_url, headers=headers, data = payload)
            data = json.loads(response_mr.text)
            st.text("")
            df = pd.DataFrame(data['data'])
            df.rename(columns = {'tradingsymbol':'Stock Name'}, inplace = True)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.caption("Trade Date: " + data['data'][0]['trade_date'])
            st.table(df['Stock Name'])
        
            #st.write("To understand the rules of the strategy, watch the complete course [here](https://learnapp.com/courses/price-action-strategy/topics/trailer)")

        elif strategy_name == "Mean Reversion Strategy":

            api_url = "https://a3shethzyl.execute-api.ap-south-1.amazonaws.com/stocks"
            payload = {}
            headers= {}
            response_mr = requests.request("GET", api_url, headers=headers, data = payload)
            data = json.loads(response_mr.text)
            st.text("")
            df = pd.DataFrame(data['data'])
            
            df.rename(columns = {'tradingsymbol':'Stock Name','entry_price':'Entry Price','stoploss':'StopLoss','target':'Target'}, inplace = True)
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.caption("Scan Date: " + data['data'][0]['scan_date']) 
            st.caption("(Trade Date is the next trading day after scan date)")
            st.table(df[['Stock Name','Entry Price','StopLoss','Target']])

            st.write("To understand the rules of the strategy, watch the complete course [here](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")