import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")
list_title = []
# pd =pd.read_excel('invoices/')
print(filepaths)
for filepath in filepaths:
    # df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # pdf = FPDF(orientation='P' , unit='mm', format='A4')
    # pdf.add_page()
    invoice_title = (filepath.strip(f"invoices\ ")[:5])
    invoice_title = invoice_title
    list_title.append(invoice_title)
    print(list_title)
    for title in list_title:
            df = pd.read_excel(filepath, sheet_name="Sheet 1")
            pdf = FPDF(orientation='P', unit='mm', format='A4')
            pdf.add_page()
            pdf.set_font(family='Times', style='B', size=20)
            # height h in pdf.cell should be as h for pdf.set-font()
            pdf.cell(w=0, h=12, txt=f" Invoice nr.{ title}", align="L", border=0)
            pdf.output(f"PDF/invoice-{title}-2023.pdf")
