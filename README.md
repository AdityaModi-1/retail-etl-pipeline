# Retail POS Data Integration Pipeline
This project simulates a real-world **ETL (Extract, Transform, Load)** workflow for a retail environment. It addresses the common business challenge of integrating messy, unstructured Point-of-Sale (POS) data into a clean, structured format suitable for data warehousing (e.g., Snowflake).
The pipeline ingests raw transaction logs, parses complex product strings, validates financial data, and normalizes timestamps for downstream reporting.

Tech Stack:
Python, Pandas, Data Extraction, Tranformation Logic, and Validation.

Key Features:
Automated Data Mapping, Data Quality Validation, Timestamp Normalization

How It Works:
1. Extract: The script reads raw transaction data simulating a legacy POS system export.
2. Transform: splits product metadata into distinct columns, standardizes date formats, renames columns to match the target warehouse schema.
3. Validate: logical checks are applied to remove corrupted records.
4. Load: Clean data is exported to 'clean_warehouse_data.csv', ready for ingestion.

Created by Aditya Modi - https://www.linkedin.com/in/aditya-modi1/
