import mammoth
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.document_loaders import *
from markdownify import markdownify

from configs import text_splitter_dict
from document_loaders import RapidOCRDocLoader
from text_splitter import ChineseRecursiveTextSplitter

dataSet = []

docLoader = RapidOCRDocLoader("E:\\LLM\\Data\\图片文档.docx")

dataSet.append(docLoader.load())

for data in dataSet:
    print(f'原始文档：{data}')
    text_splitter = ChineseRecursiveTextSplitter(chunk_size=250, chunk_overlap=10)
    docs = text_splitter.split_documents(data)
    for doc in docs:
        print(f'{doc}')

    print('------------------------------------------')

