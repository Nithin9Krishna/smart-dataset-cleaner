# src/load_data.py

import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def basic_info(df):
    info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "dtypes": df.dtypes.to_dict()
    }
    return info
