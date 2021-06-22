# coding: utf-8
"""read_excel.py
~~~~~~~~~~~~~
本模块主要负责读写Excel文件
提供两种读取Excel文件方式：xlrd方式、pandas方式
提供一种写入Excel文件方式：xlwt方式

:copyright: (c) 2021 by Zhichao Xia
:modified: 2021-05-06
"""
import re
import pandas as pd
import xlrd, xlwt


def readExcel(filePath, sheets):
    """
    Args:
        filePath: (:str), 文件存放路径
        sheets: (:list), 表名列表

    Returns:
        result: (:list), excel数据嵌套列表
    """
    result = []
    file = xlrd.open_workbook(filePath)
    for each_sheet in sheets:
        sheet = file.sheet_by_name(each_sheet)
        nrows = sheet.nrows  # 获取行数
        for i in range(0, nrows):
            data = sheet.row_values(i)
            result.append(data)
    return result


def writeExcel(filePath, data):
    """将数据一次性写入excel文件，data为嵌套列表
    Args:
        filePath: (:str), 文件存放路径
        data: (:list), 结果列表，样例：[[第一行数据列], [第二行数据列],..., [第N行数据列]]


    Returns:
        result
    """
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    n = -1  # n表示行，m表示列
    for i in data:
        m = -1
        n += 1
        for j in i:
            m += 1
            worksheet.write(n, m, j)
    workbook.save(filePath)
    print("已成功将数据写入{}文件，请对应查看！！！".format(filePath))
    return


def read_excel_pd(filePath):
    """
    Args:
        filePath: (:str), 文件存放路径

    Returns:
        result: (:pandas.core.frame.DataFrame), excel所有数据
    """
    global result
    if "csv" in filePath:
        result = pd.read_csv(filePath)
    elif "xlsx" or "xls" in filePath:
        result = pd.read_excel(filePath)
    return result


if __name__ == '__main__':
    # filePath = "D:/公司文件/WXWork/1688854147514924/Cache/File/2021-06/qcc_all_info.xlsx"
    # filePath2 = "D:/公司文件/WXWork/1688854147514924/Cache/File/2021-06/tyc_all_info.csv"
    # result = read_excel_pd(filePath)
    # # print(result)
    # writeFile = "C:/Users/xzc/Desktop/IScompany-all.xls"
    # writeFile2 = "C:/Users/xzc/Desktop/IScompany-qcc-other.xls"
    # writeFile3 = "C:/Users/xzc/Desktop/IScompany-tyc.xls"
    # writeFile4 = "C:/Users/xzc/Desktop/IScompany-tyc-other.xls"
    # industry = ["电信、广播电视和卫星传输服务", "互联网和相关服务", "软件和信息技术服务业", "研究和试验发展", "专业技术服务业", "科技推广和应用服务业",
    #             "信息传输、软件和信息技术服务业", '科学研究和技术服务业']
    # status = ['存续', '仍注册', '正常', '在业', '核准设立', '开业', '-']
    # company = []
    # companydata = [['企业名称', '所属行业', '网址', '经营范围']]
    # companydataOther = [['企业名称', '所属行业', '网址', '经营范围']]
    # companydata_t = [['企业名称', '所属行业', '网址', '经营范围']]
    # companydataOther_t = [['企业名称', '所属行业', '网址', '经营范围']]
    # num = 0
    # other_num = 0
    # for idx, data in enumerate(zip(result['企业名称'], result['登记状态'], result['所属行业'], result['网址'], result['经营范围'])):
    #     if data[1] in status:  # 判断企业状态
    #         if data[2] in industry:  # 判断所属行业
    #             if re.search("信息安全|区块链|互联网安全服务|安全咨询|互联网安全|网络安全", data[4]):
    #                 num += 1
    #                 print("正类样本数>>>", num)
    #                 if data[0] not in company:
    #                     company.append(data[0])
    #                 lists = [str(data[0]), str(data[2]), str(data[3]), str(data[4])]
    #                 companydata.append(lists)
    #             else:
    #                 other_num += 1
    #                 print("负类样本数>>>", other_num)
    #                 lists = [str(data[0]), str(data[2]), str(data[3]), str(data[4])]
    #                 companydataOther.append(lists)
    # # writeExcel(writeFile, companydata)
    # # writeExcel(writeFile2, companydataOther)
    # with open(filePath2, 'r', encoding='utf-8') as f:
    #     data = f.readlines()
    #     for i, each in enumerate(data):
    #         each_data = each.split('\t')
    #         if len(each_data) > 5:
    #             if each_data[6] in status:
    #                 if each_data[11] in industry:
    #                     if re.search("信息安全|区块链|互联网安全服务|安全咨询|互联网安全|网络安全", each_data[-1]):
    #                         num += 1
    #                         print("正类样本数>>>", num)
    #                         if each_data[0] not in set(company):
    #                             companydata.append([str(each_data[0]), str(each_data[11]), str(each_data[-3]), str(each_data[-1])])
    #                     else:
    #                         other_num += 1
    #                         print("负类样本数>>>", other_num)
    #                         companydataOther_t.append([str(each_data[0]), str(each_data[11]), str(each_data[-3]), str(each_data[-1])])
    # # writeExcel(writeFile3, companydata_t)
    # # writeExcel(writeFile4, companydataOther_t)
    # writeExcel(writeFile, companydata)
    filepath = "C:/Users/xzc/Desktop/IScompany-qcc-other.xls"
    filepath2 = "C:/Users/xzc/Desktop/IScompany-tyc-other.xls"
    data = read_excel_pd(filepath)
    data2 = read_excel_pd(filepath2)
    companys = [company for company in data["企业名称"]]
    for com in data2["企业名称"]:
        if com not in set(companys):
            companys.append(com)
    print("待筛选企业数>>>", len(companys))
    test_set = ["食品", "茶", "酒", "农业", "水泥", "建材", "地产", "纺", "鞋", "化工", "能源", "材料", "门业", "陶瓷", "砖厂",
                "仪表", "冶金", "矿", "畜", "粮油", "石油", "包装", "玻璃", "电缆", "电力", "饮品", "装饰", "纸业", "药", "机械",
                "仪器", "机床", "油漆", "肥料", "服装", "塑", "纤维", "泵", "硅业", "皮革", "物流", "电梯", "管道", "风电", "铝",
                "钢铁", "盐", "置业", "合作", "工艺", "饲料", "旅游", "厂", "实业", "煤", "建设", "环保", "集团", "设备", "制造",
                "齿轮", "资源", "冶", "日化", "液压", "起重机", "光缆", "薯", "文化", "刀具", "瓶盖", "丝绸", "业", "重工", "天然气",
                "油脂", "电路", "电气", "胶", "剂", "农", "制品", "桥梁", "锅炉", "钢", "稀土", "建筑", "印染", "制", "微波", "汽配",
                "商贸", "激光", "钻头", "调味品", "金属", "光电", "工贸", "生物科技", "印务"]
    candidate = []
    for keyword in test_set:
        for idx, company in enumerate(companys):
            if keyword in company:
                print("检测到第[{}]需要删除的企业>>>{}".format(idx, company))
                companys.remove(company)
            # else:
            #     if company not in candidate:
            #         candidate.append(company)
    # print("过滤掉企业数>>>", len(companys) - len(candidate))
    # print("候选企业数>>>", len(candidate))
    print(len(companys))
    for i in companys:
        candidate.append([i])
    filepath3 = "C:/Users/xzc/Desktop/IScompany-candidate.xls"
    writeExcel(filepath3, candidate)
