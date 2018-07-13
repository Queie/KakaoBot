from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, './kakao/index.html')


def keyboard(request):
    content ={
        'type':'buttons',
        'buttons':['장고', '카톡', '시간'],
            }
    return JsonResponse(content)


@csrf_exempt
def answer(request):
    content = {
        'message':{
            'text':'공사중 입니다',
            },
        'keyboard':{
            'type':'buttons',
            'buttons':['장고', '카톡', '시간'],
            }
        }
    return JsonResponse(content)