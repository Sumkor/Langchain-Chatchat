from typing import List

import mammoth
from langchain.document_loaders.unstructured import UnstructuredFileLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from markdownify import markdownify

class Doc2MarkdownLoader(UnstructuredFileLoader):
    def _get_elements(self) -> List:

        def convert_img(image):
            # 转存 Word 文档内的图片
            return {"src": ""}

        def doc2text(filepath):
            # 转化 Word 文档为 HTML
            result = mammoth.convert_to_html(filepath,
                                             convert_image=mammoth.images.img_element(convert_img))
            # 获取 HTML 内容
            html = result.value
            # 转化 HTML 为 Markdown
            md = markdownify(html, heading_style="ATX")
            return md

        text = doc2text(self.file_path)
        from unstructured.partition.text import partition_text
        return partition_text(text=text, **self.unstructured_kwargs)


if __name__ == '__main__':
    loader = Doc2MarkdownLoader(file_path="E:\\LLM\\Data\\图片文档.docx")
    docs = loader.load()
    print(docs)
    for doc in docs:
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
        ]
        text_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on,
                                                   return_each_line=False,
                                                   # strip_headers 为 True 是会将标题从文档内容中剔除
                                                   strip_headers=True)
        texts = text_splitter.split_text(doc.page_content)
        print(texts)
