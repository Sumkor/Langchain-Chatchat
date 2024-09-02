from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter, MarkdownTextSplitter

markdown_document = "# Intro \n\n    ## History \n\n Markdown[9] is a lightweight markup language for creating formatted text using a plain-text editor. John Gruber created Markdown in 2004 as a markup language that is appealing to human readers in its source code form.[9] \n\n Markdown is widely used in blogging, instant messaging, online forums, collaborative software, documentation pages, and readme files. \n\n ## Rise and divergence \n\n As Markdown popularity grew rapidly, many Markdown implementations appeared, driven mostly by the need for \n\n additional features such as tables, footnotes, definition lists,[note 1] and Markdown inside HTML blocks. \n\n #### Standardization \n\n From 2012, a group of people, including Jeff Atwood and John MacFarlane, launched what Atwood characterised as a standardisation effort. \n\n ## Implementations \n\n Implementations of Markdown are available for over a dozen programming languages."

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

# MD header splits
markdown_header_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on, strip_headers=False
)
md_header_splits = markdown_header_splitter.split_text(markdown_document)
for md_header_split in md_header_splits:
    print(md_header_split)
print('==========================================')


# Char-level splits

chunk_size = 250
chunk_overlap = 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

# Split
char_splits = text_splitter.split_documents(md_header_splits)
for char_split in char_splits:
    print(f'{char_split}')
print('==========================================')


# MD splits
markdown_splitter = MarkdownTextSplitter(chunk_size=200, chunk_overlap=0)
md_splits = markdown_splitter.split_text(markdown_document)
for md_split in md_splits:
    print(md_split)
