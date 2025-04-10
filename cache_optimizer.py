from cachetools import TTLCache
import pandas as pd
import Analyzer
import hashlib

session_cache = TTLCache(maxsize=15, ttl=240)
session_results = {}

def get_dataframe_hash(df: pd.DataFrame) -> str:
    df_sorted = df.sort_index(axis=1).sort_values(by=list(df.columns)).reset_index(drop=True)
    df_string = df_sorted.to_json()
    return hashlib.md5(df_string.encode()).hexdigest()

def perform_calculation(session_id: str, df: pd.DataFrame):
    df_hash = get_dataframe_hash(df)
    key = f"{session_id}:{df_hash}"

    if key in session_cache:
        return {"result": session_cache[key]}

    # Expensive calculation here
    start_location = df['LSA']
    end_location = df['LSA']
    op1Analysis = Analyzer.analyze_payments(start_location,end_location)
    if(op1Analysis=="Digital Payments"):
        op2Analysis = Analyzer.predict_speed(df)
        if(op2Analysis>4):
            result = {"response":"Can rely on Digital Payments"}
        else:
            result = {"response":"Digital Payments are accepted, but your mobile network network signals are poor!"}
    else:
        result = {"response":"Use Cash!"}

    # Cache result
    session_cache[key] = result
    return {"result": result}
