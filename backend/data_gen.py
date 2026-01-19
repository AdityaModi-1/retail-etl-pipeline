import pandas as pd

def generate_csv():
    data = {
        'Transaction_ID': ['TXN_001', 'TXN_002', 'TXN_003', 'TXN_004', 'TXN_005'],
        'Product_Info': ['Tshirt-Red-M', 'Jeans-Blue-32', 'Hoodie-Black-L', 'Tshirt-White-S', 'Socks-White-OneSize'],
        'Price': [19.99, 49.99, 35.00, -19.99, 9.99],  # Note the negative price (Error)
        'Transaction_Date': ['01/05/2026', '2026-01-06', 'Jan 07, 2026', '01/08/2026', '01/09/2026'],
        'Store_Location': ['Anaheim_001', 'Chino_002', 'Irvine_003', 'Anaheim_001', 'Chino_002']
    }

    df = pd.DataFrame(data)
    
    # Save it to the folder
    df.to_csv('raw_pos_data.csv', index=False)
    
    return {"status": "success", "message": "Raw data file (raw_pos_data.csv) created successfully."}