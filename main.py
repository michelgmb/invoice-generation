import pandas as pd
import glob

filepaths =glob.glob("invoices/*.xlsx")

#pd =pd.read_excel('invoices/')
print(filepaths)
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
