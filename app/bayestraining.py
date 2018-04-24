#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys,fre,os

ABSPATH = os.path.abspath(sys.argv[0])
ABSPATH = ABSPATH[:-20]
ABSPATH = os.path.dirname(ABSPATH) + '/'
print ABSPATH

#给每一类新闻作词频统计,计算单词在该类新闻中出现的频率
def training(index):
    print 'training : ' + str(index)
    word_num_allClass_path = ABSPATH + 'medfiles/word_num_allClass.txt'
    file_word_num_allClass = open(word_num_allClass_path, 'r')
    info_list = file_word_num_allClass.readlines()
    #所有类中的不同单词个数
    word_num_allClass = int(info_list[0].strip())   #全部样本中单词的类别数
    index_word_num_pre = info_list[index].strip().split(',')
    #index_word_num = int(index_word_num_pre[0])
    print index_word_num_pre
    index_word_pre = int(index_word_num_pre[1])     #每类新闻单词的总个数

    #读入类别index的文件
    index_file_path = ABSPATH + 'medfiles/fre/' + str(index) + '_fre.txt'
    file_index = open(index_file_path, 'r')
    word_fre_list = file_index.readlines()

    word_p_dic = {}
    for word_fre in word_fre_list:
        word_fre = word_fre.strip().split(',')
        word = word_fre[0]
        fre_ = int(word_fre[1])
        #(每个单词在该类别样本新闻中出现的次数+1)/(该类新闻单词的总个数+全部样本中单词的类别数)
        p_index_word = float(fre_ + 1) / (index_word_pre + word_num_allClass)
        word_p_dic[word] = p_index_word
    #排序
    dic_list = sorted(word_p_dic.iteritems(), key=lambda asd: asd[1], reverse=True)
    #每类新闻的词频结果写入文件
    outcome_file_path = ABSPATH + 'bayes_training_outcome/' + str(index) + '_bayestraining.txt'
    file_outcome = open(outcome_file_path, 'w')
    #第一行写入所有单词类别数 以及 每类新闻单词的总个数
    file_outcome.write(str(word_num_allClass) + ',' + str(index_word_pre) + '\n')
    i = 0
    for word_p in dic_list:
        file_outcome.write(word_p[0] + ',' + str(word_p[1]) + '\n')
        i = i + 1
    file_outcome.close

fre.fre()
for i in xrange(1, 8):
    training(i)
