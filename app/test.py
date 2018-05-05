import json
import classifier
from pyspark import SparkContext, SparkConf


def test():
    a = 1
    index_training_path = "E:\\ideaWorkplace\\classifier_web\\bayes_training_outcome\\"+str(a)+"_bayestraining_new.txt"
    file_index_training = open(index_training_path, 'r')
    training_word_p_list = file_index_training.readlines()
    worlds_li = []
    for i in xrange(1, len(training_word_p_list)):
        word_p = training_word_p_list[i].strip().split(',')
        word_p[0] = int(word_p[0])
        word_p[1] = float(word_p[1])
        if i < 100:
            worlds_li.append(word_p)
            #print training_word_p_list[i]
        else:
            break

    training_word_p_list = json.dumps(worlds_li)
    print training_word_p_list
# test()


def spark_test():
    sc = SparkContext("local", "myApp")
    index_training_path = "E:\\4_761.txt"
    file_index_training = open(index_training_path, 'r')
    content = file_index_training.read()
    word_list = classifier.handle_text(content)
    text_file = sc.parallelize(word_list)
    counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    as_map = counts.collect()
    for i in as_map:
        print i[0],i[1]

spark_test()