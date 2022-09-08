import pymysql
import json
import math
##############################
#通过数据库表Part1_pred获取公司名称列表
############################
g_textarr=[]
g_listData = []  #用于存放sponsor列表数据
def get_part1_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  Part1_real ')
    result = cursor.fetchall()
    company_name = {}
    i = 0
    line_num=0
    for row in result:
        ii=0
        for j in [1, 12]:
            ii = ii + float(row[j])
        if ii >= 12:
            line_num = line_num + 1
            company_name = {
            }
            company_name = {
                "id": i,
                "name": row[0],
            }
            i=i+1
            g_textarr.append(company_name)
    print("000000000000000get_part1_name i=", i)
    return g_textarr

def get_part1_name_mysql():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from part1_name order by name')
    result = cursor.fetchall()
    company_name = {}
    textarr = []
    i = 0
    line_num=0
    for row in result:
        company_name = {
            }
        company_name = {
            "id": row[0],
            "name": row[1],
        }
        textarr.append(company_name)
    print("--------------",len(textarr))
    return textarr

#根据公司名称取sponor_real_data
def get_sponsor_real_data(compname):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from Part1_real where COMP1=%s ', compname)
    result = cursor.fetchall()
    count = []
    i = 0
    j = 1
    for row in result:
        j = 1
        for k in range(10, 22):
            bb = row[j]
            if row[j] == '':
                bb = '0'
            count.append(float(bb))
            j = j + 1
    return count

#根据公司名称取sponor_pred_data
def get_sponsor_pred_data(compname):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from Part1_pred where COCOMPANY=%s ', compname)
    result = cursor.fetchall()
    count = []
    i = 0
    j = 2
    for row in result:
        j = 2
        for k in range(10, 24):
            bb = row[j]
            if row[j] == '':
                bb = '0'
            count.append(float(bb))
            j = j + 1
    return count

# 根据公司名称从part_list中取相关表格信息，返回json串
def getPartlist(companyName):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    name ="18 ADVISORS LLC"
    cursor.execute('select * from part_list_import where COMPANY_NAME=%s ',(companyName))
    result = cursor.fetchall()
    listData = []
    jsonData = {}
    i=0
    for row in result:
        jsonData = {}
        jsonData = {
                "state": row[1],
                "soc_name": row[2],
                "naics": row[3],
                "wage": row[4],
                "comp1": row[5],
                "year": row[6],
        }
        listData.append(jsonData)
        i = i + 1
    #print("00000000000000000000000000000000000000", i,listData)
    return listData

#if __name__ == '__main__':
#    listData =[]
#    listData = getPartlist("UNIVERSITY OF NEVADA RENO")
#    print("000000000000000",listData)


#从表NAICS_term_count中取所有行业名称
def get_naics_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  NAICS_term_count ')
    result = cursor.fetchall()
    company_name = {}
    textarr2 = []
    i = 0
    for row in result:
        company_name = {
        }
        company_name ={
            "id": row[2],
            "name": row[1],
        }
        textarr2.append(company_name)
        i = i + 1
    print("000000000000000", i, textarr2)
    return textarr2

#从表NAICS_term_count按公司名称中取出数据
def get_naics_count_data(title):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    print("  into get_naics_count_data",title)
    cursor.execute('select * from  NAICS_term_count where name = %s',title)
    result = cursor.fetchall()
    count = []
    i = 0
    j=3
    for row in result:
        j=3
        for k in range(10,22):
            bb = row[j]
            if row[j] == '':
                bb = '0'
            count.append(float(bb))
            j = j + 1
    return count

#从表NAICS_term_wage按公司名称中取出数据
def get_naics_wage_data(title):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  NAICS_term_wage where name = %s',title)
    result = cursor.fetchall()
    count = []
    j = 2
    for row in result:
        j=2
        for k in range(10,22):
            bb = row[j]
            if row[j] == '':
                bb ='0'
            count.append(float(bb))
            j = j + 1
    return count

#########################
#取soc的名称
###########################
def get_soc_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  SOC_term_count order by name ')
    result = cursor.fetchall()
    company_name = {}
    textarr = []
    i = 0
    for row in result:
        company_name = {
        }
        company_name ={
            "id": row[1],
            "name": row[14],
        }
        textarr.append(company_name)
        i = i + 1
    print("000000000000000", i, textarr)
    return textarr

#从表SOC_term_count按公司名称中取出数据
def get_soc_count_data(title):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    print("  into get_soc_count_data",title)
    cursor.execute('select * from  SOC_term_count where name = %s',title)
    result = cursor.fetchall()
    count = []
    j = 2
    for row in result:
        j=2
        for k in range(10,22):
            bb = row[j]
            if row[j] == '':
                bb = '0'
            count.append(float(bb))
            j = j + 1
    return count

#从表SOC_term_wage按公司名称中取出数据
def get_soc_wage_data(title):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  SOC_term_wage where name = %s',title)
    result = cursor.fetchall()
    count = []
    i = 0
    j = 2
    for row in result:
        j=2
        for k in range(10,22):
            bb = row[j]
            if row[j] == '':
                bb ='0'
            count.append(float(bb))
            i = i + 1
            j = j + 1
    return count






