import pandas as pd
import numpy as np

# Load the Excel file
file_path = "C:\\Users\\Nanditha\\Downloads\\Main data.xlsx"
xls = pd.ExcelFile(file_path)

# Load the specific sheet
df = xls.parse('Sheet1')

# Function to clean the dataframe by replacing special characters and 'N/A'
def clean_dataframe(df):
    def clean_cell(cell):
        if isinstance(cell, str):
            if cell.strip().upper() in ['N/A', 'NA']:
                return np.nan
            if any(char in cell for char in ['<', '>', '=', '@', '#', '$', '%', '^', '&', '*', '{', '}', '[', ']', '|', '\\']):
                return np.nan
        return cell
    return df.applymap(clean_cell)

# Clean the dataframe
cleaned_df = clean_dataframe(df)

# Save the cleaned dataframe to a new Excel file
output_path = "Cleaned_Main_data.xlsx"
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    cleaned_df.to_excel(writer, index=False, sheet_name='Sheet1')
