
import string

import pymysql
import csv
#读NAICS_term_wage.csv文件入数据库
def csvToMyql(fileName):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='website', charset='utf8')
    cursor = conn.cursor()
    sql =()
    if fileName == "/Volumes/My_data/1H1B/analysis_data/source/Part1_list.csv":
        sql = ('insert into part_list(ID,COMPANY_NAME,STATE,SOC_NAME,NAICS,WAGE,COMP1,YEAR) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/Part1_real.csv":
        sql = ('insert into Part1_real(COMP1,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/Part1_pred.csv":
        sql = ('insert into Part1_pred(id,COCOMPANY,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021,y2022,y2023) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/NAICS_term_wage.csv":
        sql = ('insert into NAICS_term_wage(id,NAICS,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021,`index`,SeqNo,name) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/NAICS_term_count.csv":
        sql = ('insert into NAICS_term_count(id,NAICS,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021,`index`,SeqNo,name) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/SOC_term_count.csv":
        sql = ('insert into SOC_term_count(id,SOC,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021,name) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    elif fileName == "/Volumes/My_data/1H1B/analysis_data/source/SOC_term_wage.csv":
        sql = ('insert into SOC_term_wage(id,SOC,y2010,y2011,y2012,y2013,y2014,y2015,y2016,'
               'y2017,y2018,y2019,y2020,y2021,name) '
               'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')

    list = []
    with open(fileName, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        i = 0
        for row in reader:
            list = []
            list.append(row)
            print(list)
            cursor.executemany(sql, list)

    conn.commit()
    print(cursor.rowcount, '插入成功.\n')
    cursor.close()
    conn.close()
    return

def get_part1_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='1h1b', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  Part1_real ')
    result = cursor.fetchall()
    company_name = {}
    i = 0
    line_num=0
    textarr=[]
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
            textarr.append(company_name)
    print("000000000000000i=", i)
    return textarr

########
#提高效率
#将取出get_part1_name中公司放入part_list_import
def insertImportPart(list):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='1h1b', charset='utf8')
    cursorInsert = conn.cursor()
    insertSql = ()
    insertSql = ('insert into part_list_import(COMPANY_NAME,STATE,SOC_NAME,NAICS,WAGE,COMP1,YEAR,ID) '
                 'values(%s,%s,%s,%s,%s,%s,%s,%s)')
    #cursorInsert.execute(insertSql, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    cursorInsert.executemany(insertSql, list)
    conn.commit()
    print(cursorInsert.rowcount, '插入成功.\n')
    cursorInsert.close()

def importPartlist():
    part1_name=get_part1_name()
    print(part1_name)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='1h1b', charset='utf8')
    cursor = conn.cursor()
    sql =()
    item ={}
    i=0
    while i< len(part1_name):
        item = part1_name[i]
        print("------------------",item["name"])
        #sql = ('select * from  Part_list where COMPANY_NAME=%s'),"HITACHI CONSULTING CORPORATION")#item["name"])
        #print("+++++++++++++++++++++",sql)
        cursor.execute('select * from  Part_list where COMPANY_NAME=%s',item['name'])
        result = cursor.fetchall()
        count = []
        j=0
        list = []
        for row in result:
            print("++++++++++++++++++",row)
            list.append(row)
            j=j+1
        if j>0:
            insertImportPart(list)
        print("jjjjjjjjjjjjjjjjjjjj",j)
        i = i+1
    cursor.close()
    conn.close()

#将取出part1_real表中h1b公司大于10 放入part1_name
def insert_part1_name_detail(textarr):
    conn1 = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='1h1b',charset='utf8')
    cursorInsert = conn1.cursor()
    insertSql = ('insert into part1_name(id, name) values(%s,%s)')
    cursorInsert.executemany(insertSql, textarr)
    conn1.commit()
    cursorInsert.close()
    conn1.close()

def insert_part1_name():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='Jessica102321%', port=3306, database='1h1b', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from  Part1_real ')
    result = cursor.fetchall()
    company_name = {}
    i = 0
    line_num=0
    textarr=[]
    for row in result:
        ii=0
        for j in [1, 12]:
            ii = ii + float(row[j])
        if ii >= 12:
            line_num = line_num + 1
            company_name = []
            company_name.append(i)
            company_name.append(row[0])
            i=i+1
            textarr.append(company_name)
    print("000000000000000i=", textarr)
    insert_part1_name_detail(textarr)
    cursor.close()
    conn.close()
    return

'''读取excel'''
def readExcel(fileName):
    fr=open(fileName)
    reader1=csv.reader(fr)
    list=[]
    for row in reader1:
        list.append(row)

    return  list

'''连接数据库并向mysql表进行写入'''
def writeToMysql(list):
    conn=pymysql.connect(host='127.0.0.1',user='root',password='Jessica102321%',port=3306,database='1h1b',charset='utf8')
    cursor=conn.cursor()
    sql=('insert into csv(year,quarter,realgdp,realcons,realinv,realgovt,realdpi,cpi,m1,m2,m3,m4,m5,realint) '
         'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)')
    list1=[]
    for i in list[1:6]:
        tuple1=tuple(i)
        list1.append(tuple1)
    cursor.executemany(sql,list1)
    conn.commit()
    print(cursor.rowcount,'插入成功.\n')
    cursor.close()
    conn.close()
'''读取mysql数据库，将读取的数据写入csv文件'''
def mysqlToCsv():
    conn=pymysql.connect(host='127.0.0.1',user='root',password='Jessica102321%',port=3306,database='dbtest',charset='utf8')
    cursor=conn.cursor()
    sql1=('select * from csv')
    cursor.execute(sql1)
    result1=cursor.fetchall()
    sql2=('select column_comment from information_schema.Columns where table_name="csv"and table_schema="dbtest"')
    cursor.execute(sql2)
    result2=cursor.fetchall()
    file=open('/Volumes/My_data/1H1B/analysis_data/source/stata33333.csv','w')
    writer=csv.writer(file)
    list=[]
    for i in result2:
        list.append(i)
    writer.writerow(list)
    for j in result1:
        writer.writerow(j)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    #fileName='C:\\Users\Administrator\PycharmProjects\\test\\1030\lianxi\stata3.csv'
    #print(readExcel(fileName))
    #writeToMysql(readExcel(fileName))
    #mysqlToCsv()
    fileName = "/Volumes/My_data/1H1B/analysis_data/source/Part1_list.csv"
    csvToMyql(fileName)

    #importPartlist()
   # insert_part1_name()