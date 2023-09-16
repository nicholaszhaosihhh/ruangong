import jieba
import gensim
import re
import os
from line_profiler import LineProfiler

# 获取指定路径的文件内容
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str

def filter(str):
    # 将读取到的文件内容先进行jieba分词，
    str = jieba.lcut(str)
    result = []
    # 把标点符号、转义符号等特殊符号过滤掉
    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result

# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1, text2):
    texts = [text1, text2]
    # 形成词典
    dictionary = gensim.corpora.Dictionary(texts)
    # 形成向量
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


def main(path1, path2):
    save_path = 'E:\\homework_test\\answer.txt'  # 输出结果绝对路径
    str1 = get_file_contents(path1)
    str2 = get_file_contents(path2)
    text1 = filter(str1)
    text2 = filter(str2)
    similarity = calc_similarity(text1, text2)
    # print(text1)
    print("文章相似度： %.2f" % similarity)
    # 将相似度结果写入指定文件
    f = open(save_path, 'w', encoding="utf-8")
    f.write("文章相似度： %.2f" % similarity)
    f.close()




if __name__ == '__main__':
    path1 = "E:\\homework_test\\orig.txt"  # 论文原文的文件的绝对路径（作业要求）
    path2 = "E:\\homework_test\\orig_0.8_add.txt"  # 抄袭版论文的文件的绝对路径
    if not os.path.exists(path1):
        print("论文原文文件不存在！")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文文件不存在！")
        exit()

    main(path1, path2)

# 性能测试
    p = LineProfiler()
    p.add_function(get_file_contents)
    p.add_function(filter)
    p.add_function(calc_similarity)
    p_wrap = p(main)
    p_wrap(path1,path2)
    p.print_stats()  # 控制台打印相关信息
    p.dump_stats('saveName.Iprof')  # 当前项目根目录下保存文件
