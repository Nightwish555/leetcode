from PyPDF2 import PdfReader, PdfWriter

output = PdfWriter()

reader = PdfReader(r"D:\CU_76a18490a1c94c20bda9ccfc81acabd6 (1).pdf")
# 获取总页数
page_count = reader.getNumPages()

# with open(,'rb') as pf:
#     pin = PdfReader(pf)
#     for i in range(2):
#         page = pin.getPage(pin.pages[0])
#         print(page)
#     #     output.addPage(page)
#     # with open("XXXX/out.pdf",'wb') as ouf:
#     #     output.write(ouf)