from sentence_transformers import SentenceTransformer, util

# Download model
# model = SentenceTransformer('E:\\LLM\\Model\\bge-base-zh-v1.5')
# model = SentenceTransformer('E:\\LLM\\Model\\text2vec-base-chinese')
model = SentenceTransformer('E:\\LLM\\Model\\acge-large-zh')

# Corpus of documents and their embeddings
# corpus = ['Python在各个编程语言中比较适合新手学习。',
#     'Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。',
#     '一只棕色的狐狸跳过了一只躺着的懒狗。']
corpus = ['#补单状态 补单的单据有很多状态。  \n## 待审核  \n单据已经创建， 保存。  \n## 已拆单  \n单据已经进行拆单操作。  \n## 审核通过  \n单据已经审核。  \n## 已接单  \n工厂已接单或MES已接单。  \n## 工厂已拆单  \n工厂已经进行了拆单操作。  \n## 排产中  \n工厂排产中。  \n## 生产中  \n工厂生产中。  \n## 包装中  \n工厂仓库包装中。  \n## 已包装  \n工厂仓库已经包装完成。  \n## 入库中  \n工厂包件正在入库。  \n## 已入库',
          '#补单状态 工厂仓库已经包装完成。  \n## 入库中  \n工厂包件正在入库。  \n## 已入库  \n工厂包件已经入库。  \n## 预约配送  \n售后人员已经跟客户预约配送时间。  \n## 出库中  \n工厂包件出库中。  \n## 已出库  \n工厂包件已经出库。  \n## 配送中  \n物流公司配送中。  \n## 已配送  \n物流公司已配送。  \n## 安装中  \n安装公司安装中。  \n## 已安装  \n安装公司安装结束。',
          '#售后单来源 售后单的新增有三个来源。分别来自好居， 至装宝和售后专员手工新增。']
corpus_embeddings = model.encode(corpus)

# Queries and their embeddings
# queries = ["Python是什么？", "狐狸在做什么？"]
queries = ["补单状态有什么"]
queries_embeddings = model.encode(queries)

# Find the top-2 corpus documents matching each query
hits = util.semantic_search(queries_embeddings, corpus_embeddings, top_k=3)

# Print results of first query
print(f"Query: {queries[0]}")
for hit in hits[0]:
    print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
# Query: What is Python?
# Python is an interpreted high-level general-purpose programming language. (Score: 0.6759)
# Python is dynamically-typed and garbage-collected. (Score: 0.6219)

# Print results of second query
# print(f"Query: {queries[1]}")
# for hit in hits[1]:
#     print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))
# Query: What did the fox do?
# The quick brown fox jumps over the lazy dog. (Score: 0.3816)
# Python is dynamically-typed and garbage-collected. (Score: 0.0713)
