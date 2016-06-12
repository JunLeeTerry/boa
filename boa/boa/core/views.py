#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect

from boa.core.models import Answer
from boa.core.forms import AnswerForm
import random

def question(req):
    answerform = AnswerForm()

    id = random.randint(1,172)

    return render_to_response('question.html',{"answerform":answerform,"id":id})
    
def result(req):
    try:
        question = req.GET.get('question')
    except:
        questoin = ""

    try:
        name = req.GET.get('name')
    except:
        name = ""

    try:
        id = req.GET.get('id')
    except:
        id = "1"

    result = Answer.objects.get(id=int(id))

    return render_to_response('result.html',{"name":name,
                                             "question":question,"result":result})
