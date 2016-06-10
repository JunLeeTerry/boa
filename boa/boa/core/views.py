#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect

from boa.core.models import Answer
from boa.core.forms import AnswerForm

def question(req):
    answerform = AnswerForm()

    return render_to_response('question.html',{"answerform":answerform,})
    
def result(req):
    try:
        question = req.GET.get('question')
    except:
        questoin = ""

    try:
        name = req.GET.get('name')
    except:
        name = ""

    result = Answer.objects.order_by('?')[1]

    return render_to_response('result.html',{"name":name,
                                             "question":question,"result":result})
