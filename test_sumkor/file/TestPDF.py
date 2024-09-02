from spire.pdf.common import *
from spire.pdf import *

# # 创建一个PdfDocument类的对象
# doc = PdfDocument()
#
# # 加载一个PDF文档
# doc.LoadFromFile("E:\\LLM\\Data\\mysql设计规范01.pdf")

# # 将文档转换为HTML
# doc.SaveToFile("E:\\LLM\\Data\\PDF转HTML.html", FileFormat.HTML)
# doc.Close()
#
#
# # 将文档保存到HTML流
# fileStream = Stream("E:\\LLM\\Data\\PDF转HTML.html")
# doc.SaveToStream(fileStream, FileFormat.HTML)


# # 创建一个字符串对象来存储文本
# extracted_text = ""
# for i in range(doc.Pages.Count):
#     page = doc.Pages.get_Item(i)
#     text = page.ExtractText(True)
#     extracted_text += text
# print(extracted_text)
#
#
# extractOptions = PdfTextExtractOptions()
# extractOptions.IsExtractAllText = True


# import fitz
# from tqdm import tqdm
#
# html_content = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Title</title></head><body style=\"display: flex;justify-content: center;flex-direction: column;background: #0e0e0e;align-items: center;\">"
#
# doc = fitz.open("E:\\LLM\\Data\\mysql设计规范01.pdf")
# for page in tqdm(doc):
#     html_content += page.get_text('html')
#
# html_content += "</body></html>"
# print(html_content)

