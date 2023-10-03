import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# filepaths = glob.glob("invoices/*.xlsx")
# list_title = []
# # pd =pd.read_excel('invoices/')
# print(filepaths)
#
# for filepath in filepaths:
#     # df = pd.read_excel(filepath, sheet_name="Sheet 1")
#     # pdf = FPDF(orientation='P' , unit='mm', format='A4')
#     # pdf.add_page()
#     invoice_title = (filepath.strip(f"invoices\ ")[:5])
#     invoice_title = invoice_title
#     list_title.append(invoice_title)
#     print(list_title)
#     for title in list_title:
#             df = pd.read_excel(filepath, sheet_name="Sheet 1")
#             pdf = FPDF(orientation='P', unit='mm', format='A4')
#             pdf.add_page()
#             pdf.set_font(family='Times', style='B', size=20)
#             # height h in pdf.cell should be as h for pdf.set-font()
#             pdf.cell(w=0, h=12, txt=f" Invoice nr.{ title}", align="L", border=0)
#             pdf.output(f"PDF/invoice-{title}-2023.pdf")


# # mince Code
# filepaths = glob.glob('*invoices/*.xlsx')
# lis_file = []
# lis_invoice_number = []
# for filepath in filepaths:
#     file_name =(Path(filepath).stem)
#     print(file_name)
#     lis_file.append(file_name)
#     lis_invoice_number.append(file_name[:5])
# print(lis_file)
# print(lis_invoice_number)
# for file in lis_file:
#     pdf = FPDF(orientation='P', unit='mm', format='A4')
#
#     pdf.set_auto_page_break(auto=True, margin=10)
#     pdf.add_page()
#     pdf.set_font(family='Times', style='B', size=20)
#     pdf.cell(w=0 ,h=20,align='L', txt=f"Invoice nr.{file[:5]}")
#     pdf.ln(12)
#     pdf.cell(w=0, h=16, align='L', txt=f"Date {file[6:]}")
#     pdf.ln(15)
#     pdf.output(f"pdf2/invoice{file[:10]}.pdf")


filepaths = glob.glob('*invoices/*.xlsx')
for filepath in filepaths:
    file_name = (Path(filepath).stem)
    invoice_nr, date = file_name.split("-")
    print(invoice_nr, date)
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=20)
    pdf.cell(w=0 ,h=20,align='L', txt=f"Invoice nr.{invoice_nr}")
    pdf.ln(12)
    pdf.cell(w=0, h=16, align='L', txt=f"Date {date}")
    pdf.ln(15)
    pdf.output(f"pdf2/invoice-{file_name}.pdf")
