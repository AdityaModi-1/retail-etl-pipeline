import pandas as pd
from datetime import datetime
import os

def run_pipeline():
    if not os.path.exists('raw_pos_data.csv'):
        return {"error": "Input file 'raw_pos_data.csv' not found. Please click 'Generate Data' first."}

    print("Starting ETL Pipeline...")
    
    df = pd.read_csv('raw_pos_data.csv')
    

    product_split = df['Product_Info'].str.split('-', expand=True)
    df['Category'] = product_split[0]
    df['Color'] = product_split[1]
    df['Size'] = product_split[2]

    df['Clean_Date'] = pd.to_datetime(df['Transaction_Date'], format='mixed').dt.strftime('%Y-%m-%d')

    initial_count = len(df)
    valid_df = df[df['Price'] > 0].copy()
    dropped_count = initial_count - len(valid_df)

    final_columns = ['Transaction_ID', 'Category', 'Color', 'Size', 'Price', 'Clean_Date', 'Store_Location']
    final_output = valid_df[final_columns]
    
    final_output.to_csv('clean_warehouse_data.csv', index=False)
    print("Pipeline Complete. Saved to 'clean_warehouse_data.csv'")

    return {
        "status": "success",
        "dropped_rows": dropped_count,
        "total_rows": len(final_output),
        "data": final_output.to_dict(orient='records')
    }