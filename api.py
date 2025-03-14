from fastapi import FastAPI
import pandas as pd
from datetime import date
import json

from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

from data_read import execute_reader
from load_item_name import load_items

app = FastAPI()

data = pd.DataFrame({"item": ["Apple", "Banana"], "price": [100,50]})

def get_data(item):
    period = 7
    company = item
    c_data = execute_reader(item)

    df_train = c_data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Creating a dictionary
    data = {
        "company": company,
        "period": period,
        "actual_data": c_data,
        "train_data": df_train,
        "futore": future,
        "forecast": forecast
    }

    # Convert dictionary to JSON object (string)
    json_object = json.dumps(data, indent=4)

    # Print JSON object
    print(json_object)

    return json_object
    


@app.get("/get_price/")
def get_price(item: str):
    # result = data[data["item"].str.lower() == item.lower()]
    data = get_data(item)
    # if not result.empty:
    #     return result.to_dict(orient="records")[0]

    if not data.empty:
        return data
    return {"error": "Item not found"}

# uvicorn api:app --reload