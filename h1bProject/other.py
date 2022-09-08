#这是原来读取文件的程序
#进入页面获取所有公司名称,这个没有用，只是读取csv例子
def read_csvfile():
    csvfilename="Part1_real.csv"
    line_num=0
    company_name = {}
    textarr = []
    id=0
    with open(csvfilename, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        real_data = []
        for row in reader:
            ii=0
            j=1
            for j in [1,12]:
                ii= ii + float(row[j])
            if ii >= 16:
                company_name = {}
                line_num = line_num + 1
                company_name['id'] = id
                company_name['name'] = row[0]
                textarr.append(company_name)
                #print("********************** line_num",line_num,textarr)
                id = id + 1
    return textarr

#通过 ID号查找公司取出10年数据,作废了没有用
def get_sponsor_data(id):
    print("AAAAAAAAAAAAAAAAAAAA  id=",id)
    csvfilename="first100_pred.csv"
    with open(csvfilename) as f:
        reader = csv.reader(f)
        head_row = next(reader)
        priod_data = []
        for row in reader:
            select_id = row[0]
            if select_id == id:
                priod_data= row[2:]
                print("select-data-----------------=",priod_data)
    return priod_data

#通过 ID号查找公司取出10年数据,作废了没有用
def get_sponsor_pre_data(compname):
    csvfilename="Part1_pred.csv"
    with open(csvfilename, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        pred_data = []
        for row in reader:
            select_name = row[1]
            if select_name == compname:
                pred_data= row[2:]
    return pred_data
#通过 公司名称查找公司取出10年数据,作废了没有用
def get_sponsor_real_data1(compname):
    csvfilename="Part1_real.csv"
    line_num=0
    with open(csvfilename, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        real_data = []

        for row in reader:
            ii=0
            j=1
            for j in [1,12]:
                ii= ii + float(row[j])
            if ii >= 6:
                line_num = line_num + 1
            select_name = row[0]
            if row[0] == compname:
                real_data = row[2:]
    return real_data
#作废了没有用
def get_sponsor_company_data1(compname):
    csvfilename="Part1_real.csv"
    with open(csvfilename, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        for row in reader:
            select_id = row[0]
            if select_id == id:
                real_data = row[1]
    return real_data

#通过公司名称取得历史行业工资收入，作废了没有用
def get_sponsor_list_data(compName):
    csvfilename="Part1_list.csv"
    state = []
    soc_name = []
    naics = []
    wage = []
    comp1 = []
    year = []
    with open(csvfilename, encoding='utf-8') as f:
        reader = csv.reader(f)
        head_row = next(reader)
        real_data = []
        i=0
        for row in reader:
            select_name = row[1]
            if select_name == compName:
                state[i] = row[2]
                soc_name[i] = row[3]
                naics[i] = row[3]
                wage[i] = row[3]
                comp1[i] = row[3]
                year[i] = row[3]
                i = i + 1
    return real_data
