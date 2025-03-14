import pandas as pd
import os

directory_path = "./data"

def load_items():
# list files
    files = [f for f in os.listdir(directory_path) if f.endswith((".xls", ".csv"))]

    print("Available files")

    # for i, file in enumerate(files):
    #     print(f"{i}. {file}")

    file_index = 0
    selected_file = files[file_index]

    df = pd.read_csv(os.path.join(directory_path, selected_file), header=None)

    # items_array = df["ITEM"].tolist()
    items_array = df.iloc[:, 0].tolist()
    items_tuple = tuple(df.iloc[:, 0])

    # print(type(items_array))
    # print("Extracted items: ", items_array)

    return items_tuple

data = load_items()
print(type(data))
print(data)
