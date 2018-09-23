import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")# project_name 项目名称
django.setup()
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
class Json_view(View):
    def get(self,request):
        list = []
        from data_deal.json1 import makeJson
        from data_deal.clearText import clearText
        clearText('E:\\360Downloads\\Vue.D3.tree-master\\data\\data.json')
        str = makeJson('东营华为工程项目管理有限公司', '2018/09/20 21:52:10', '')
        list.append(str)
        from django.http import JsonResponse, HttpResponse
        import json
        return HttpResponse(json.dumps(list), content_type='application/json')


def get(request):
        from data_deal.json1 import makeJson
        from data_deal.clearText import clearText
        clearText('E:\\360Downloads\\Vue.D3.tree-master\\data\\data.json')
        if request.method == 'GET':
            return render(request, 'index.html')
        else:
            name = request.POST.get('text')
            time = request.POST.get('time')
            str = {'cont': makeJson(name, time, ''),
                   'type': type(name)}
            file_name = open('E:\\360Downloads\\Vue.D3.tree-master1\\data\\data.json', 'w',encoding='utf-8')
            file_name.write(makeJson(name, time, ''))
            return render(request, 'tree.html', context=str)
def get1(request):
    return render(request, 'index.html')
