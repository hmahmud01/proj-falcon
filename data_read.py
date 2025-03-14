import os
import pandas as pd
import numpy as np


def read_and_search_excel_files(directory, search_item, column_names):
    consolidated_data = pd.DataFrame()

    # Iterate over all files in the directory
    for file in os.listdir(directory):
        # Check if the file is a CSV file
        if file.endswith(".csv"):
            filepath = os.path.join(directory, file)
            try:
                # Read the CSV file without headers
                data = pd.read_csv(filepath, header=None, names=column_names)
                
                # Filter the rows matching the search item
                filtered_data = data[data['ITEM'] == search_item]
                
                # Append the filtered data to the consolidated DataFrame
                consolidated_data = pd.concat([consolidated_data, filtered_data], ignore_index=True)
            except Exception as e:
                print(f"Error reading file {file}: {e}")
    
    # Sort the consolidated data by date
    if 'DATE' in consolidated_data.columns:
        # consolidated_data['DATE'] = pd.to_datetime(consolidated_data['DATE'], errors='coerce')
        consolidated_data['DATE'] = pd.to_datetime(consolidated_data['DATE'], format='%Y%m%d')
        # consolidated_data['DATE'] = consolidated_data['DATE'].dt.strftime('%Y-%m-%d')
        consolidated_data = consolidated_data.sort_values(by='DATE').reset_index(drop=True)

    return consolidated_data

def data_arrange(c_data):
    print("INSIDE FUNC")
    print(c_data)
    new_data = c_data.rename(columns={
        'DATE': 'Date',
        'OPEN PRICE': 'Open',
        'CLOSE PRICE': 'Close',
        'HIGHEST PRICE': 'High',
        'LOWEST PRICE': 'Low',
        'VOLUME': 'Volume'
    })[['Date', 'Close', 'High', 'Low', 'Open', 'Volume']]

    print("REARRENGIN")
    # print(new_data)
    new_data['Date'] = pd.to_datetime(new_data['Date']).dt.date
    print(new_data)
    print("REARRANGE DONE!")
    return new_data

def execute_reader(item):
    directory_path = ("./data")
    item_to_search = item
    print(f"SELECTED ITEM : {item_to_search}")
    # Define the column names (same for all files)
    column_names = ['ITEM', 'DATE', 'OPEN PRICE', 'HIGHEST PRICE', 'LOWEST PRICE', 'CLOSE PRICE', 'VOLUME', 'TRADE']

    result = read_and_search_excel_files(directory_path, item_to_search, column_names)

    new_result = data_arrange(result)

    return new_result


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
# print(type(c_data))
# print(c_data)



