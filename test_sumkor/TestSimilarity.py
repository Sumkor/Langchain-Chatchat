from sentence_transformers import SentenceTransformer, util


def get_similarity(model, sentences_1, sentences_2):
    # 获得句子嵌入向量
    embeddings_1 = model.encode(sentences_1, normalize_embeddings=True)
    embeddings_2 = model.encode(sentences_2, normalize_embeddings=True)
    # 余弦相似度
    cos_sim = util.pytorch_cos_sim(embeddings_1, embeddings_2)
    # 表示将 embeddings_2 矩阵转置 (T) 后与 embeddings_1 进行矩阵乘法。
    # similarity = embeddings_1 @ embeddings_2.T
    # print(f'{similarity}')
    return cos_sim


if __name__ == "__main__":
    sentences = ['手机使用卡顿了应该怎么处理？',
                 '手机卡顿了怎么办？',
                 '手机运行变慢了，有什么解决方法？',
                 '如何解决手机使用时的卡顿问题？',
                 '手机反应迟钝，应该如何处理？',
                 '遇到手机卡顿，我该如何快速修复？',
                 '手机不流畅怎么回事，如何优化？',
                 '手机操作延迟，有没有好的处理技巧？',
                 '为什么我的手机会卡顿，该如何改善？',
                 '手机响应慢了，有哪些提速技巧？',
                 '手机经常卡顿，有没有简单的解决方案？',
                 '一只棕色的狐狸跳过了一只躺着的懒狗',
                 ]

    model1 = SentenceTransformer('E:\\LLM\\Model\\bge-base-zh-v1.5')
    model2 = SentenceTransformer('E:\\LLM\\Model\\text2vec-base-chinese')
    # model3 = SentenceTransformer('E:\\LLM\\Model\\bert-base-chinese')
    # model4 = SentenceTransformer('E:\\LLM\\Model\\acge-large-zh')


    similarity1 = model1.encode(sentences, normalize_embeddings=True)
    similarity2 = model2.encode(sentences, normalize_embeddings=True)
    # similarity3 = model3.encode(sentences, normalize_embeddings=True)
    # similarity4 = model4.encode(sentences, normalize_embeddings=True)

    for i in range(len(similarity1)):
        if i != 0:
            cos_sim1 = util.pytorch_cos_sim(similarity1[0], similarity1[i])
            cos_sim2 = util.pytorch_cos_sim(similarity2[0], similarity2[i])
            # cos_sim4 = util.pytorch_cos_sim(similarity4[0], similarity4[i])
            # print(f'[0]与[{i}]相似度: bge: {cos_sim1}, acge: {cos_sim4}')
            print(f'[0]与[{i}]相似度: bge: {cos_sim1}, text2vec: {cos_sim2}')
    print("---------------------------")


