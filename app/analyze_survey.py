
from db_connection import connect_to_db

import pandas as pd
import numpy as np
from scipy.stats import norm


############# Functions #################

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
    # calculate z-stat
    merged_df["z"] = (merged_df["PercentA_low"] - merged_df["PercentA_high"]) / np.sqrt(
        merged_df["PCT_SE_low"]**2 + merged_df["PCT_SE_high"]**2
    )
    # Calculate p-value
    merged_df["pval"] = 2 * (1 - norm.cdf(abs(merged_df["z"])))
    
    # They defined significant difference between low and high performing students to be p < 0.05
    # So let there be a "significant" column that is "True" if p < 0.05 and False otherwise
    merged_df["significant"] = merged_df["pval"] < 0.05
    
    return merged_df

def order_by_significance(df_sig):
    # sort by p-value
    return df_sig[[
        "Question", "CategoryL_low","CategoryL_high",
        "PercentA_low", "PercentA_high", "pval", "significant"
    ]].sort_values("pval")

######## Driver Function #################

def analyze():
    conn = connect_to_db()
    
    # avoid code duplication by looping through subjects
    subjects = ["math", "reading"]
    
    # store resulting files here when complete
    rf_paths = {}
    
    for subject in subjects:
        # pull data into data frame
        q = "SELECT * FROM "+ subject + "_TB"
        df = pd.read_sql(q, con=conn)
        
        # export to CSV
        filepath = "output/" + subject + ".csv"
        df.to_csv(filepath, index=False)

        merged = merge_groups(assign_performance_groups(filepath))
        sig_ordered = order_by_significance(calculate_significance(merged))
        
        rf_path = "output/"+subject+"_by_sig.csv" # store new file path 
        sig_ordered.to_csv(rf_path, index=False)            
        rf_paths[subject] = str(rf_path) # store associated resulting file path
    
    # Finally, dispose connection 
    conn.dispose()
    
    return rf_paths

