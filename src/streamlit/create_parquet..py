from typing import List

import pandas as pd

if __name__ == "__main__":
    d = pd.read_json(
        "/Users/loic.caminale/Workspace/formation/dataguru/webinar-python-borne-electrique/src/streamlit/data.json"
    )
    d["timestamp"] = pd.to_datetime(d["timestamp"], format="%Y-%m-%dT%H:%M:%S%z")
    d.to_parquet("data.parquet")
