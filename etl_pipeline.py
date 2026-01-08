import pandas as pd
from datetime import datetime

def run_pipeline():
    print("Starting ETL Pipeline!")

    try:
        df = pd.read_csv('raw_pos_data.csv')
        print(f"Loaded {len(df)} rows of raw data.")
    except FileNotFoundError:
        print("Error: Input file not found.")
        return
    
    print("Mapping Product Data...")
    
    product_split = df['Product_Info'].str.split('-', expand=True)

    df['Category'] = product_split[0]
    df['Color'] = product_split[1]
    df['Size'] = product_split[2]

    print("Standardizing Dates...")
    df['Clean_Date'] = pd.to_datetime(df['Transaction_Date'], format='mixed').dt.strftime('%Y-%m-%d')

    print("Validating Data Quality...")
    initial_count = len(df)

    valid_df = df[df['Price'] > 0].copy()
    
    dropped_count = initial_count - len(valid_df)
    if dropped_count > 0:
        print(f"Alert: Dropped {dropped_count} invalid transaction(s) due to pricing errors.")

    final_columns = ['Transaction_ID', 'Category', 'Color', 'Size', 'Price', 'Clean_Date', 'Store_Location']
    final_output = valid_df[final_columns]
    
    final_output.to_csv('clean_warehouse_data.csv', index=False)
    print("Pipeline Complete. Clean data saved to 'clean_warehouse_data.csv'")

    print("\nPreview of Clean Data:")
    print(final_output.head())

if __name__ == "__main__":
    run_pipeline()