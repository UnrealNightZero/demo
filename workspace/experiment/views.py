from django.shortcuts import render
from django.http import HttpResponse
from .models import USER_DATA
from django.http import JsonResponse
from django.core.cache import cache
import concurrent.futures

def auto_data(request):
    if request.method == "GET":
        data_list = []
        for i in range(9000000,10000001):
            data_list.append(USER_DATA(
                name=f'User {i}',
                address=f'Address {i}',
                email=f'email{i}@example.com',
                phone=f'123456789{i:06}'
            ))

        USER_DATA.objects.bulk_create(data_list)
        return HttpResponse("成功")

def exper(request):
    if request.method == "GET":
        return render(request,"show_data.html")

def search(request):
    if request.method == "POST":
        search_term = request.POST.get('search_term')
        user_id = search_term.split(' ')
        names = "Address "+user_id[1]
        print(user_id[1])
        try:
            results = USER_DATA.objects.filter(address=names,name=search_term)
        except:
            print("error")
        print(results)
        response = [{'name': result.name} for result in results]
        return JsonResponse(response, safe=False)

def search_2(request):
    if request.method == "POST":
        search_term = request.POST.get('search_term')

        results = cache.get(search_term)

        if not results:
            user_id = search_term.split(' ')
            names = "Address "+user_id[1]
            print(user_id[1])
            try:
                results = list(USER_DATA.objects.filter(address=names, name=search_term).values())

                cache.set(search_term, results, 180)
            except:
                print("error")

        response = [{'name': result['name']} for result in results if 'name' in result]
        return JsonResponse(response, safe=False)

def search_3(request):
    if request.method == "POST":
        search_term = request.POST.get('search_term')

        results = cache.get(search_term)

        if not results:
            user_id = search_term.split(' ')
            names = "Address "+user_id[1]

            try:
                # 并行查询
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    # 将查询任务拆分成多个子任务
                    tasks = [
                        executor.submit(USER_DATA.objects.filter(address=names, name=search_term).values)
                    ]

                    # 获取子任务的结果
                    results = [task.result() for task in tasks]

                # 设置缓存
                cache.set(search_term, results, 180)
            except:
                print("error")
                results = []  # 在异常情况下为 results 变量赋一个默认值

        response = [{'name': result['name']} for result in results if 'name' in result]
        return JsonResponse(response, safe=False)
def data(request):
    chart_data = {
        'chart1Data': [1080, 750, 680, 130],
        'chart2Data': [1080, 750, 680, 130],
        'chart3Data': [1080, 750, 680, 130],
    }
    return JsonResponse(chart_data)