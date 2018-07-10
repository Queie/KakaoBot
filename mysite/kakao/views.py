from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("<h1>Kakao 챗봇을 위한 API 입니다.</h1>")

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['장고', '카톡', '시간'],
    })

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

