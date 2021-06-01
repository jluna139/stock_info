from yahoo_fin import stock_info as si
from yahoo_fin import  news
import matplotlib


import pandas as pd
import streamlit as st
st.title("Enter company symbol to retrieve data")


st.set_option('deprecation.showPyplotGlobalUse', False)

######################## Side BAr
st.sidebar.subheader("Top Cryptos by market-cap")
top_crypt = si.get_top_crypto()[1:10].drop(["Name", "% Change", "Change","Volume in Currency (24Hr)", "Market Cap", "Circulating Supply", "Volume in Currency (Since 0:00 UTC)", "Total Volume All Currencies (24Hr)"], axis=1)
st.sidebar.table(top_crypt)



st.sidebar.subheader("Top Gainers Today ")
top_gain = si.get_day_gainers()[:10].drop(["Name", "Change", "Volume", "Market Cap", "PE Ratio (TTM)", "Avg Vol (3 month)"], axis=1)
st.sidebar.table(top_gain)

st.sidebar.subheader("Top Loosers Today")
top_loss = si.get_day_losers()[:10].drop(["Name", "Change", "Volume", "Market Cap", "PE Ratio (TTM)", "Avg Vol (3 month)"], axis=1)
st.sidebar.table(top_loss)
##########################################



###########################################################
selected_companies_input = st.text_input( label="Separete symbol by coma and space", value="fb, amzn, aapl, nflx").split(', ')
st.subheader("Stocks price since 2019")
companies_list = []
for key in range(len(selected_companies_input)):
    lowCase = selected_companies_input[key].lower()
    retrun_info_data = pd.DataFrame(si.get_data(lowCase, start_date="01/01/2010"))["close"]
    retrun_info_data = retrun_info_data.rename(lowCase)
    companies_list.append(retrun_info_data)
    data_list_company_graph = pd.DataFrame(companies_list).transpose()



data_list_company_graph.plot.line()
st.line_chart(data_list_company_graph)


st.header(" ")
st.header("Current Prices")

for key in range(len(selected_companies_input)):
    cols1, cols2 = st.beta_columns([1,3])

    lowCase = selected_companies_input[key].lower()
    retrun_info_data = si.get_live_price(lowCase)
    cols1.write(lowCase.upper())
    cols2.write(retrun_info_data)





################################################################
st.header(" ")
st.header(" ")
###########################################################



for key in range(len(selected_companies_input)):
    lowCase = selected_companies_input[key].lower()
    st.header("Recent %s news "%lowCase.upper())
    cols1, cols2 = st.beta_columns([1,3])


    newwww = news.get_yf_rss(lowCase)
    var1 = newwww[1]["summary"][:150]
    link1 = newwww[1]["link"]
    var2 = newwww[2]["summary"][:150]
    link2 = newwww[2]["link"]
    var3 = newwww[3]["summary"][:150]
    link3 = newwww[3]["link"]

    st.write("%s..............[link](%s)" % (var1, link1))
    st.write("%s..............[link](%s)" % (var2, link2))
    st.write("%s..............[link](%s)" % (var3, link3))

