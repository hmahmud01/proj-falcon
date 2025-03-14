import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

from data_read import execute_reader
from load_item_name import load_items

print("ALL 👍 ")

START = "2020-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('STOCK Forecast App TEST')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select Dataset for prediction', stocks)

st.write(selected_stock)

# n_years = st.slider('Years of prediction:', 1, 4)
# period = n_years * 365
# timeline = "Years"

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 7
timeline = "Days"

@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY, multi_level_index=False)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Loading data ...')
data = load_data(selected_stock)
data_load_state.text('Loading data ... done!')

print(type(data))
print(data)

st.subheader('Yfinanace Data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()

df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader('Forecast data')
st.write(forecast.tail())

# future data rule:
# yhat=trend+seasonality effects+other components
st.write("yhat=trend+seasonality effects+other components")
st.write(f'Forecast plot for {period} {timeline}')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

# st.write("Forecast components")
# fig2 = m.plot_components(forecast)
# st.write(fig2)

# item_to_search = ""

# item_input = input("PLEASE SELECT AN ITEM FOR DATA PREDICTION (Enter In Number) : \n1. ABBANK\n2. ACI\n3. APEXFOOT\n4. BANGAS\n5. CITYBANK\n")

# if int(item_input) is 1:
#     item_to_search = "ABBANK"
# elif int(item_input) is 2:
#     item_to_search = "ACI"
# elif int(item_input) is 3:
#     item_to_search = "APEXFOOT"
# elif int(item_input) is 4:
#     item_to_search = "BANGAS"
# elif int(item_input) is 5:
#     item_to_search = "CITYBANK"
# else:
#     item_to_search = "ABBANK"

# print(f"SELECTED ITEM : {item_to_search}")

# c_data = execute_reader(item_to_search)

# print("printing c_DATA")
# print(c_data)


# st.title(f"LOCAL COMPANY DATA: {item_to_search} ")

local_stocks = load_items()
selected_local_stock = st.selectbox('Select Dataset for prediction', local_stocks)

st.title(f"LOCAL COMPANY DATA: {selected_local_stock} ")
c_data = execute_reader(selected_local_stock)

print("printing c_DATA")
print(c_data)

print(type(selected_local_stock))
print(selected_local_stock)

st.subheader('Local Data')
st.write(selected_local_stock)
st.write(c_data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=c_data['Date'], y=c_data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=c_data['Date'], y=c_data['Close'], name='stock_close'))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)



plot_raw_data()

df_train2 = c_data[['Date', 'Close']]
df_train2 = df_train2.rename(columns={"Date": "ds", "Close": "y"})

m2 = Prophet()
m2.fit(df_train2)
future2 = m2.make_future_dataframe(periods=period)
forecast2 = m2.predict(future2)

st.subheader('Forecast data')
st.write(forecast2.tail())

st.write(f'Forecast plot for {period} {timeline}')
fig2 = plot_plotly(m2, forecast2)
st.plotly_chart(fig2)

# st.write("Forecast components")
# fig3 = m2.plot_components(forecast2)
# st.write(fig3)