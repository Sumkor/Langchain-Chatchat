from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('E:\\LLM\\Model\\bge-base-zh-v1.5')

corpus = [
    'Python是一种代表简单主义思想的语言。阅读一个良好的Python程序就感觉像是在读英语一样。',
    '售后系统是为了方便进行售后流程而开发的，其内部连接了订单系统、MES系统、配送安装系统等。通过售后系统，可以实现对售后单据的流通，保障用户的使用体验。']
corpus_embeddings = model.encode(corpus)

queries = ["售后系统是什么？"]
queries_embeddings = model.encode(queries)


hits = util.semantic_search(queries_embeddings, corpus_embeddings, top_k=3)

for hit in hits[0]:
    print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))

