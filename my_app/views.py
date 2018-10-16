from django.shortcuts import render
from django.http import HttpResponse
def hello():
    return HttpResponse('各位大佬、来瓶洗发水啊！')
def index(request):
    context = '各位大佬、来瓶洗发水啊！'
    return render(request, 'polls/119.htm', {'context': context})

#
# def results(request, question_id):
#     response = "results   You're looking at the results of question %s."
#     return HttpResponse(response % question_id)