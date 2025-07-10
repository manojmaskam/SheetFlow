import pandas as pd
from sheetflow.config import get_config

def read_excel():
    config = get_config()
    file_path = config.get("EXCEL", "file_path")

    print(f"📄 Reading Excel from: {file_path}")
    df = pd.read_excel(file_path)
    print(f"📊 Loaded Excel: {len(df)} rows")
    print(df.head())

    return df
