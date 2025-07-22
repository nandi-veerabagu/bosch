# bosch
Task Summary:
Load an Excel file.

Remove special characters and invalid values (N/A, NA, <, >, =, etc.).

Save the cleaned file with the same format.

Push everything to a GitHub repository.
-------------------------------------------------------------------------------------------
Folder Structure:
css
Copy
Edit
excel-cleaner/
│
├── main.py
├── requirements.txt
├── Main data.xlsx       ← (Place original Excel here)
├── .gitignore
└── README.md
---------------------------------------------------------------------------------------------
main.py – Python Code:
python
Copy
Edit
import pandas as pd
import numpy as np

def clean_dataframe(df):
    def clean_cell(cell):
        if isinstance(cell, str):
            if cell.strip().upper() in ['N/A', 'NA']:
                return np.nan
            if any(char in cell for char in ['<', '>', '=', '@', '#', '$', '%', '^', '&', '*', '{', '}', '[', ']', '|', '\\']):
                return np.nan
        return cell
    return df.applymap(clean_cell)

def main():
    input_file = "Main data.xlsx"
    output_file = "Cleaned_Main_data.xlsx"
    
    xls = pd.ExcelFile(input_file)
    df = xls.parse('Sheet1')
    cleaned_df = clean_dataframe(df)
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        cleaned_df.to_excel(writer, index=False, sheet_name='Sheet1')

    print(f"Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    main()
-----------------------------------------------------------------------------------------------------------------
    requirements.txt:
nginx
Copy
Edit
pandas
openpyxl
------------------------------------------------------------------------------------------------------------------
.gitignore:
markdown
Copy
Edit
__pycache__/
*.pyc
*.xlsx

--------------------------------------------------------------------------------------------------------------------
README.md:
markdown
Copy
Edit
--------------------------------------------------------------------------------------------------------------------
#  Excel Cleaner

This Python script removes special characters and invalid values (like `N/A`, `<`, `>`, `=`) from an Excel file while preserving its original structure and formatting.
--------------------------------------------------------------------------------------------------------------------
## Features
- Cleans `Sheet1` of the Excel file.
- Removes:
  - Special characters like `<`, `>`, `=`, etc.
  - Strings like `N/A` or `NA`
- Saves the cleaned Excel file using `openpyxl`.
------------------------------------------------------------------------------------------------------------------------
##  Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/excel-cleaner.git
cd excel-cleaner
-----------------------------------------------------------------------------------------------------------------------

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your original Excel file:
Place Main data.xlsx in the root of the folder.
------------------------------------------------------------------------------------------------------------------------
Usage
bash
Copy
Edit
python main.py

--------------------------------------------------------------------------------------------------------------------------
### 🔄 GitHub Push Instructions:

```bash
git init
git add .
git commit -m "Initial commit - Excel cleaner"
git branch -M main
git remote add origin https://github.com/your-username/excel-cleaner.git
git push -u origin main
