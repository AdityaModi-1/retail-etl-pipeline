Retail ETL Pipeline Dashboard
- A full-stack Data engineering platform that simulates a real-world Retail Data Pipeline.
- This application allows users to generate "messy" data, trigger a Python ETL process to clean/transform it, and visualize the results in a React dashboard.

Tech Stack:
  Backend: Python, Pandas, Flask, Flask-CORS, CSV Files
  Frontend: React.js

How It Works:
  The user clicks "Generate Data", which creates a 'raw_pos_data.csv' file containing simulated transaction records with dirty data.
  Transform: The user clicks "Run ETL."
  The Python Script:
    Splits the 'Product_Info' column into 'Category', 'Color' and 'Size'.
    Normalizes inconsistent date formats into "yyyy-mm-dd"
    Validates data logic (dropping transactions with negative prices).
  Loads the clean data to 'clean_warehous_data.csv', and the JSON response is sent to the frontend for display.
