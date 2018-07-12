from django.http import HttpResponse

# Create your views here.
def index(request):
    content = """
    <h1>Python Anywhere </h1>
    <h3>메인 페이지 입니다</h3>
    <a href='https://erdos.pythonanywhere.com/kakao/'> > Kakao Bot</a><br>
    |<a href='https://www.pythonanywhere.com/user/erdos/'> Python Anywhere </a>|<br>
    """
    return HttpResponse(content)