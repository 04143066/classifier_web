# coding=utf-8
import math
import jieba
import os, sys

ABSPATH = os.path.abspath(sys.argv[0])
ABSPATH = ABSPATH[:-5]
ABSPATH = os.path.dirname(ABSPATH) + '/'
print ABSPATH


def getPofClass(index, word_list):
    # 输入类index的贝叶斯训练结果文件
    index_training_path = ABSPATH + 'bayes_training_outcome/' + str(index) + '_bayestraining.txt'
    file_index_training = open(index_training_path, 'r')
    dic_training = {}  # 存储 index_bayestraining.txt 中的 (单词：P)
    training_word_p_list = file_index_training.readlines()
    allwords_fre_allwords_num = training_word_p_list[0].strip()  # index_bayestraining.txt的第一行
    allwords_fre = int(allwords_fre_allwords_num[1])  # 该类新闻样本所有单词个数
    allwords_num = int(allwords_fre_allwords_num[0])  # 所有类别样本的所有单词种数
    for i in xrange(1, len(training_word_p_list)):
        word_p = training_word_p_list[i].strip().split(',')
        dic_training[word_p[0]] = float(word_p[1])

    # 遍历测试样本的wordlist，求每个Word的p
    p_list = []
    for word in word_list:
        word = word.strip()
        if word in dic_training:
            p_list.append(str(dic_training[word]))
        else:
            p_list.append(str(1.0 / (allwords_fre + allwords_num)))
    # 计算P
    p_index = 0
    for p in p_list:
        p = math.log(float(p), 2)
        p_index = p_index + p
    return -p_index


# 文本去停用词处理
def handle_text(text):
    # rightIndex = int(filename.split('_')[0])
    # 分词
    text = text.replace('腾讯科技', '')
    text = text.replace('腾讯财经', '')
    text = text.replace('腾讯体育', '')
    text = text.replace('腾讯汽车', '')
    text = text.replace('腾讯娱乐', '')
    text = text.replace('腾讯房产', '')
    text = text.replace('人民网', '')
    text = text.replace('新华网', '')
    text = text.replace('中新网', '')
    text = text.replace(' ', '')
    text = "".join(text.split())
    word_list = jieba.cut(text, cut_all=False)
    # 停用词
    stopword_path = ABSPATH + 'data/stop.txt'
    file_stopword = open(stopword_path, 'r')
    stopword_list = file_stopword.readlines()
    for i in xrange(0, len(stopword_list)):
        word = stopword_list[i].strip()
        stopword_list[i] = word

    # 去停用词
    word_list_nostop = []
    for word in word_list:
        word = word.strip().encode('utf-8')
        if word in stopword_list:
            pass
        else:
            word_list_nostop.append(word)
    return word_list_nostop

# 贝叶斯算法核心
def bayes(text):
    word_list_nostop = handle_text(text)
    # 求每个类index的p
    max = 0
    maxIndex = 0
    for index in xrange(1, 8):
        y = getPofClass(index, word_list_nostop)
        # print str(index) + ':' + str(y)
        if y != float("inf") and y > max:
            max = y
            maxIndex = index
    return maxIndex