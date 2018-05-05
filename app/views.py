# coding:utf-8
import os
import json
import classifier
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("nihaozxx")


def index(request):
    return render(request, "index.html")


def upload(request):
    return render(request, "upload.html",)


def home(request, a):
    if int(a) == 1:
        type = "财经"
    elif int(a) == 2:
        type = "科技"
    elif int(a) == 3:
        type = "汽车"
    elif int(a) == 4:
        type = "房产"
    elif int(a) == 5:
        type = "体育"
    elif int(a) == 6:
        type = "娱乐"
    elif int(a) == 7:
        type = "其他"
    index_training_path = "E:\\ideaWorkplace\\bayes_classifier\\medfiles\\fre\\"+str(a)+"_fre.txt"
    file_index_training = open(index_training_path, 'r')
    training_word_p_list = file_index_training.readlines()
    worlds_li = []
    for i in xrange(1, len(training_word_p_list)):
        word_p = training_word_p_list[i].strip().split(',')
        if i < 100:
            worlds_li.append(training_word_p_list[i])
        else:
            break
    index_training_path = "E:\\ideaWorkplace\\bayes_classifier\\bayes_training_outcome\\"+str(a)+"_bayestraining.txt"
    file_index_training = open(index_training_path, 'r')
    training_word_p_list = file_index_training.readlines()
    world_list = []
    for i in xrange(1, len(training_word_p_list)):
        word_p = training_word_p_list[i].strip().split(',')
        if i < 100:
            world_list.append(training_word_p_list[i])
        else:
            break
    return render(request, 'home.html', {'worlds_li': worlds_li, 'world_list': world_list, 'type': type, 'a': a})


def highchart(request, a):
    index_training_path = "E:\\ideaWorkplace\\classifier_web\\bayes_training_outcome\\"+str(a)+"_bayestraining_new.txt"
    file_index_training = open(index_training_path, 'r')
    training_word_p_list = file_index_training.readlines()
    worlds_li = []
    for i in xrange(1, len(training_word_p_list)):
        word_p = training_word_p_list[i].strip().split(',')
        word_p[0] = int(word_p[0])
        word_p[1] = float(word_p[1])
        worlds_li.append(word_p)
    return HttpResponse(json.dumps(worlds_li), content_type='application/json')


def uploadfile(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            returnHttpResponse("no files for upload!")
        destination = open(os.path.join("E:\\", myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        file_analyse = open("E:\\"+myFile.name, 'r')
        content = file_analyse.read()
        cutword_list = classifier.handle_text(content)
        a = classifier.bayes(content)
        if int(a) == 1:
            type = "财经"
        elif int(a) == 2:
            type = "科技"
        elif int(a) == 3:
            type = "汽车"
        elif int(a) == 4:
            type = "房产"
        elif int(a) == 5:
            type = "体育"
        elif int(a) == 6:
            type = "娱乐"
        elif int(a) == 7:
            type = "其他"
        return render(request, 'upload.html', {'content': content, 'cutword_list': cutword_list, 'type': type})