from langchain.document_loaders import UnstructuredMarkdownLoader, UnstructuredFileLoader, TextLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter, MarkdownTextSplitter
from configs import (
    text_splitter_dict,
)
from text_splitter import ChineseRecursiveTextSplitter

dataSet = []

# fileLoader = UnstructuredFileLoader("E:\\LLM\\Data\\ASM售后系统说明文档.md")
# dataSet.append(fileLoader.load())

# txtLoader = UnstructuredFileLoader("E:\\LLM\\Data\\ASM售后系统说明文档2.txt")
# dataSet.append(txtLoader.load())

textLoader = TextLoader("E:\\LLM\\Data\\ASM售后系统说明文档3.md", encoding='utf8')
dataSet.append(textLoader.load())

# markdownLoader = UnstructuredMarkdownLoader("E:\\LLM\\Data\\intro.md")
# dataSet.append(markdownLoader.load())

# 分词器
headers_to_split_on = text_splitter_dict['MarkdownHeaderTextSplitter']['headers_to_split_on']
text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                           return_each_line=False,
                                           # strip_headers 为 True 是会将标题从文档内容中剔除
                                           strip_headers=True)


for data in dataSet:
    print(f'原始文档：{data}')
    texts = text_splitter.split_text(data[0].page_content)

    # 进一步分词
    text_splitter = ChineseRecursiveTextSplitter(chunk_size=250, chunk_overlap=10)
    docs = text_splitter.split_documents(texts)

    # Markdown 标题恢复
    for doc in docs:
        for header in reversed(headers_to_split_on):
            if doc.metadata.get(header[1]):
                doc.page_content = header[0] + doc.metadata.get(header[1]) + " " + doc.page_content

        print(f'{doc}')

    print('------------------------------------------')



