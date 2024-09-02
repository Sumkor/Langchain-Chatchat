import mammoth
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import *
from markdownify import markdownify

from configs import text_splitter_dict
from document_loaders import RapidOCRDocLoader
from text_splitter import ChineseRecursiveTextSplitter

# 将 doc 文档转换成 html，再转换为 markdown

def convert_img(image):
    # 转存 Word 文档内的图片
    return {"src": ""}


# 转化 Word 文档为 HTML
# result = mammoth.convert_to_html("E:\\LLM\\Data\\mysql设计规范01.docx",
result = mammoth.convert_to_html("E:\\LLM\\Data\\图片文档.docx",
                                 convert_image=mammoth.images.img_element(convert_img))
# 获取 HTML 内容
html = result.value
# 转化 HTML 为 Markdown
md = markdownify(html, heading_style="ATX")
# print(md)

# 分词器
headers_to_split_on = text_splitter_dict['MarkdownHeaderTextSplitter']['headers_to_split_on']
text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                           return_each_line=False,
                                           # strip_headers 为 True 是会将标题从文档内容中剔除
                                           strip_headers=True)

texts = text_splitter.split_text(md)
for text in texts:
    print(text)