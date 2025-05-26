
from db_connection import connect_to_db

import pandas as pd
import numpy as np
from scipy.stats import norm


import seaborn as sb # I may not need this in this file



def analyze():
    """"""
    pass

############# helper functions below #################


def assign_performance_groups(filepath):
    df = pd.read_csv(filepath)
    
    # Extract overall average from TOTAL row
    total_avg_score = df[df["CategoryL"].str.strip() == "TOTAL"]["Avg_score"].values[0]
    
    low_ceiling = total_avg_score - 1
    high_floor = total_avg_score + 1
    
    # Assign performance groups
    def label_group(score):
        if score < low_ceiling:
            return "Low" 
        elif score > high_floor:
            return "High"
        else:
            return None  # Ignore average scores

    df["Group"] = df["Avg_score"].apply(label_group)
    
    return df

def merge_groups(df):
    df = df[df["Group"].isin(["Low", "High"])]
    
    low = df[df["Group"] == "Low"]
    high = df[df["Group"] == "High"]

    merged = pd.merge(
        low,
        high,
        on=["Question"],
        suffixes=("_low", "_high")
    )
    return merged


def calculate_significance(merged_df):
    merged_df["z"] = (merged_df["PercentA_low"] - merged_df["PercentA_high"]) / np.sqrt(
        merged_df["PCT_SE_low"]**2 + merged_df["PCT_SE_high"]**2
    )
    merged_df["pval"] = 2 * (1 - norm.cdf(abs(merged_df["z"])))
    merged_df["significant"] = merged_df["pval"] < 0.05
    return merged_df

def order_by_significance(df_sig):
    return df_sig[[
        "Question", "CategoryL_low","CategoryL_high",
        "PercentA_low", "PercentA_high", "pval", "significant"
    ]].sort_values("pval")

################## Calls ###########################

conn = connect_to_db()

# pull data into data frames
df_r = pd.read_sql("SELECT * FROM reading_TB", con=conn)
df_m = pd.read_sql("SELECT * FROM math_TB", con=conn)

# export to CSV
df_m.to_csv("output/math.csv", index=False)
df_r.to_csv("output/reading.csv", index=False)

merged = merge_groups(assign_performance_groups("output/math.csv"))
merged.to_csv("output/merged.csv", index=False)
sig = order_by_significance(calculate_significance(merged))
sig.to_csv("output/sig.csv", index=False)


######## END ############
conn.dispose()
"""
^ this will either be the last command in this file or the 
last command in the visuals file if we need to work with the 
actual SQL for visuals. hopefully I can just take out what I need
as some kind of python objects and create visuals with those.
"""
    
#########################