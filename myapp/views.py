from django.shortcuts import render
from pandas import read_csv
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from myapp import models
from django.views.decorators.csrf import csrf_exempt
import json
import csv
import codecs
from django.core import serializers
import math
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from myapp import models
import csv
from myapp import getH1bData

# Create your views here.
#点击导航条上的按钮，对应的各个html
def h1b_display(request):
    return render(request, 'h1b_display.html')
def h1b_home(request):
    return render(request, 'h1b-home.html')
def h1b_industry(request):
    return render(request, 'h1b_industry.html')
def h1b_occupation(request):
    return render(request, 'h1b_occupation.html')
def h1b_list(request):
    return render(request, 'h1b_list.html')
def h1b_list_more(request):
    return render(request, 'h1b_list_more.html')



def h1b_index(request):
    print("888888888888888888888 index.html ")
    return render(request, 'index_home.html')
def index_occupation(request):
    return render(request, 'index_occpuation.html')
def index_industry(request):
    return render(request, 'index_industry.html')
def index_sponsor(request):
    return render(request, 'index_sponsor.html')
def index_sponsor_more(request):
    return render(request, 'index_sponsor_more.html')
def contact(request):
    return render(request, 'contact.html')
def dir1(request):
    return render(request, 'dir1.html')
def dir2(request):
    return render(request, 'dir2.html')
def dir3(request):
    return render(request, 'dir3.html')
@csrf_exempt
def get_company(request):
    print("--------------------------into get_company")
    company_name = getH1bData.get_part1_name_mysql()
    response = JsonResponse({"status": '服务器接收成功', 'data': company_name})
    return response

#传图表上的数据给前台
def sponor_chart_data(request):
    """数据统计：构造柱状图数据"""
    data_axis =['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
    data1=[0.468,0.678,0.750,0.715,0.603,0.445,0.27,0.1095,-0.006,-0.048,
           0.0139,0.212,0.5757575,1.1351]
    data2=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,2.0]
    result = {
        "status": True,
        "series": {
            "year": data_axis,
            "pro": data1,
            "real": data2,
        }
    }
   # print(json.dumps(result))
    # return HttpResponse(json.dumps(result))
    return JsonResponse(result)
#取得选中公司的ID
@csrf_exempt
def get_selected_companyID(request):
    print("222222222222222222222222222222      get_selected_companyID")
    data_axis =['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
    if request.method == "POST":
        print("get_selected_companyID:====",request.POST.get('selected'))
        compName = request.POST.get('selected')
        real_data = getH1bData.get_sponsor_real_data(compName)
        pre_data = getH1bData.get_sponsor_pred_data(compName)
        data1 = real_data
        data2 = pre_data

        listData = []
        jsonData={}
        #compName = "DELOITTE CONSULTING LLP"
        listData = getH1bData.getPartlist(compName)
        total_count = len(listData)
        result = {
            "status": True,
            "series": {
                "year": data_axis,
                "pro": data1,
                "real": data2,
            },
            "text":{
                "total": total_count,
                "lists": listData,
            }
        }
    getH1bData.g_listData = listData
    return JsonResponse(result)

#取得选中公司的ID更多的
@csrf_exempt
def get_selected_companyID_more(request):
    print("333333333333      get_selected_companyID_more")
    data_axis =['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
    if request.method == "POST":
        print("get_selected_companyID:====",request.POST.get('selected'))
        compName = request.POST.get('selected')
        real_data = getH1bData.get_sponsor_real_data(compName)
        pre_data = getH1bData.get_sponsor_pred_data(compName)
        data1 = real_data
        data2 = pre_data

        listData = []
        jsonData={}
        #compName = "DELOITTE CONSULTING LLP"
        listData = getH1bData.getPartlist(compName)
        total_count = len(listData)
        result = {
            "status": True,
            "series": {
                "year": data_axis,
                "pro": data1,
                "real": data2,
            },
            "text":{
                "total": total_count,
                "lists": listData,
            }
        }
    getH1bData.g_listData = listData
    return JsonResponse(result)

#列表中选择页数
######################################
#Wage by industry
#####################################

#传图表上的数据给前台
def h1b_industry_chart(request):
    """数据统计：构造柱状图数据"""
    data_axis =['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    compName = "Oilseed and Grain Farming"
    data1 = getH1bData.get_naics_count_data(compName)
    data2 = getH1bData.get_naics_wage_data(compName)
    result = {
        "status": True,
        "series": {
            "year": data_axis,
            "data1": data1,
            "data2": data2,
        },
    }
    print("result-----------",result)
    return JsonResponse(result)

#传递naics_name到前台
@csrf_exempt
def get_naics_company(request):
    company_name = getH1bData.get_naics_name()
    #print("--------------------------into get_naics_company",company_name)
    response = JsonResponse({"status": '服务器接收成功', 'data': company_name})

    return response

@csrf_exempt
def get_selected_naics(request):
    print("222222222222222222222222222222      get_selected_naics")
    data_axis = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    if request.method == "POST":
        print("get_selected_companyID:====", request.POST.get('selected'))
        compName = request.POST.get('selected')
    #    compName = "Oilseed and Grain Farming"
        data1 = getH1bData.get_naics_count_data(compName)
        data2 = getH1bData.get_naics_wage_data(compName)
        result = {
            "status": True,
            "series": {
                "year": data_axis,
                "data1": data1,
                "data2": data2,
            },
        }

    print("---------------------",json.dumps(result))
    # return HttpResponse(json.dumps(result))
    return JsonResponse(result)



######################################
#Wage by occupation  soc
#####################################

#传图表上的数据给前台,初始显示图形
def h1b_occuption_chart(request):
    """数据统计：构造柱状图数据"""
    data_axis =['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    compName = "Chief Executives"
    data1 = getH1bData.get_soc_count_data(compName)
    data2 = getH1bData.get_soc_wage_data(compName)
    result = {
        "status": True,
        "series": {
            "year": data_axis,
            "data1": data1,
            "data2": data2,
        },
    }
    print("result-----------",result)
    return JsonResponse(result)

#传递soc_name到前台
@csrf_exempt
def get_soc_company(request):
    company_name = getH1bData.get_soc_name()
    #print("--------------------------into get_naics_company",company_name)
    response = JsonResponse({"status": '服务器接收成功', 'data': company_name})
    return response
#前台选择后，
@csrf_exempt
def get_selected_soc(request):
    print("222222222222222222222222222222      get_selected_naics")
    data_axis = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    if request.method == "POST":
        print("get_selected_companyID:====", request.POST.get('selected'))
        compName = request.POST.get('selected')
        data1 = getH1bData.get_soc_count_data(compName)
        data2 = getH1bData.get_soc_wage_data(compName)
        result = {
            "status": True,
            "series": {
                "year": data_axis,
                "data1": data1,
                "data2": data2,
            },
        }

    print("---------------------",json.dumps(result))
    # return HttpResponse(json.dumps(result))
    return JsonResponse(result)