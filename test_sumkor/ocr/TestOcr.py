from document_loaders import RapidOCRLoader

import os

if not os.path.exists('C:/Users/huang_zebin/Downloads/MX9NF2KLMX.jpeg'):
    print("文件不存在，请检查路径。")
else:
    loader = RapidOCRLoader(file_path="C:/Users/huang_zebin/Downloads/MX9NF2KLMX.jpeg")
    docs = loader.load()
    print(docs)

