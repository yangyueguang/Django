from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from apps.models.models import Student
import json
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from apps.service import task

def index(request):
    result = {'ds': '中国'}
    request_params = request.GET
    print(request_params)
    # return  render(request,'index.html')
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")


def upload(request):
    if request.method == "POST":
        f1 = request.FILES['pic']
        file_name = '%s/static/%s' % (settings.BASE_DIR, f1.name)
        with open(file_name, 'w') as f:
            for c in f1.chunks():
                f.write(c)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")


# 分页
def student_list(request):
    nums = request.GET['nums']  # 每页显示多少个
    index = request.GET['page']
    items = Student.objects.all()
    paginator = Paginator(items, nums)
    page = paginator.page(int(index))
    return HttpResponse(page.object_list)


# 缓存请求10分钟
@cache_page(60 * 10)
def get_all(request):
    # 设置：cache.set(键, 值, 有效时间)
    # 获取：cache.get(键)
    # 删除：cache.delete(键)
    # 清空：cache.clear()
    return HttpResponse('hello1')

#celery异步
def celeryTest(request):
    task.say_something.delay('hello')
    return HttpResponse('ok')

