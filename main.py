import pandas as pd

# Corrected file path
file_path = r"C:\Users\Nanditha\Downloads\MG1CA770-5.10_Valt_Load_Sheet_V5_.xlsm (2).xls"

# Load the "Main Data" sheet
df_main_data = pd.read_excel(file_path, sheet_name='Main Data')

# Clean data: remove rows and columns with all NaNs
df_cleaned = df_main_data.dropna(how='all').dropna(axis=1, how='all')

# Replace known error strings and special characters
errors_to_replace = ['#N/A', 'N/A', 'NaN', '#DIV/0!', '#REF!', '#VALUE!', '∞', '�', '�']
df_cleaned = df_cleaned.replace(errors_to_replace, pd.NA)

# Replace remaining NA values with empty string
df_cleaned = df_cleaned.fillna("")

# Save to new Excel file
output_file_path = r"C:\Users\Nanditha\Downloads\Cleaned_Main_Data.xlsx"
df_cleaned.to_excel(output_file_path, index=False)

print("Cleaned file saved to:", output_file_path)
df_cleaned.to_csv("Cleaned_Main_Data.csv", index=False)