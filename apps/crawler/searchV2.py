# -*- coding:utf-8 -*-
"""本模块功能：利用selenium爬取企查查中企业信息

:copyright: (c) 2021 by Zhichao Xia
:modified: 2021-06-1
"""
import re
import time
import xlrd
from selenium import webdriver

start = time.time()
firstURL = "http://www.googleui.com/so/"
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
drive = webdriver.Chrome(options=option)
drive.get(firstURL)  # 输入网站
print("================正在打开【%s】网站================" % firstURL)


def search(idx, company):
    # 定位输入文本框->输入文本->单击元素
    if idx == 0:
        drive.find_element_by_id("kw").send_keys(company)
        drive.find_element_by_id("btn").click()
        element = drive.find_element_by_id('result')
        if "官网" in element.text:
            text = element.text.replace('\n', '')
            textNew = text[text.rfind('官网'):]
            url = re.search(
                '((H|h)(T|t)(T|t)(P|p)[S|s]?(:|：)//)?([a-zA-Z0-9$\-_&,!* ]+\.)+(([a-zA-Z0-9$\-_&,!:*]+[ /]?)+\.?)+([a-zA-Z0-9/\?=# ]+)',
                textNew)
            return url.group()
    else:
        drive.find_element_by_id('kw').clear()
        drive.find_element_by_id("kw").send_keys(company)
        drive.find_element_by_id("btn").click()
        element = drive.find_element_by_id('result')
        if "官网" in element.text:
            text = element.text.replace('\n', '')
            textNew = text[text.rfind('官网'):]
            url = re.search(
                '((H|h)(T|t)(T|t)(P|p)[S|s]?(:|：)//)?([a-zA-Z0-9$\-_&,!* ]+\.)+(([a-zA-Z0-9$\-_&,!:*]+[ /]?)+\.?)+([a-zA-Z0-9/\?=# ]+)',
                textNew)
            return url.group()
    return "-"

# print(search(idx=0, company="成都圭目机器人有限公司"))

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


white_path = open("../../../title_processed/data/company_spider_sousuo.txt", 'w', encoding='utf-8')
filepath = "../../../title_processed/data/四川AI产业链企业.xls"
DataList = readExcel(filepath, ["Sheet1"])
for idx, each_data in enumerate(DataList[1:]):
    each_company = each_data[0]
    print(idx, each_company)
    result = each_company + " " + each_data[1] + " " + search(idx, each_company)
    white_path.write(result)
    white_path.write('\n')
end = time.time()
print("共计耗时%s秒！！！" % round(end - start, 2))





