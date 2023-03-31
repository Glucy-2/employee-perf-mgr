# -*- coding: utf-8 -*-


import os
import csv
from gui import msgbox

# 数据存储在staff.csv，UTF-8编码

staff_file = f"{os.path.abspath('.')}/staff.csv"
codec = "UTF-8"

# 读取函数返回的数据和写入函数传入的数据都是字典，都按照以下格式：
{
    "工号1": {
        "name": "姓名",
        "gender": "性别",
        "quarter1": "第一季度的业绩",
        "quarter2": "第二季度的业绩",
        "quarter3": "第三季度的业绩",
        "quarter4": "第四季度的业绩",
        "total": "四个季度的总业绩",
        "rank": "依据总业绩的排名",
    },
    "工号2": {
        "name": "姓名",
        "gender": "性别",
        "quarter1": "第一季度的业绩",
        "quarter2": "第二季度的业绩",
        "quarter3": "第三季度的业绩",
        "quarter4": "第四季度的业绩",
        "total": "四个季度的总业绩",
        "rank": "依据总业绩的排名",
    },
}


def read_file():  # 将文件的内容读出并返回（读取失败返回None）
    f = None
    try:
        f = open(staff_file, "r", encoding=codec)
        staff_data = {}  # 创建一个字典用于存储数据
        reader = csv.reader(f)  # 读取csv文件中的数据
        for row in reader:  # 遍历每一行数据
            staff_data[row[0]] = {}  # 为每个键创建一个空字典
            staff_data[row[0]]["name"] = row[1]
            staff_data[row[0]]["gender"] = row[2]
            staff_data[row[0]]["quarter1"] = row[3]
            staff_data[row[0]]["quarter2"] = row[4]
            staff_data[row[0]]["quarter3"] = row[5]
            staff_data[row[0]]["quarter4"] = row[6]
            staff_data[row[0]]["total"] = row[7]
            staff_data[row[0]]["rank"] = row[8]
        return staff_data  # 返回数据
    #except FileNotFoundError as e:
    #    msgbox.error("员工数据文件不存在", "请检查文件是否存在")
    #    return None
    #except PermissionError as e:
    #    msgbox.error("没有读取员工数据文件的权限", "请检查文件权限")
    #    return None
    #except Exception as e:
    #    msgbox.error("读取员工数据文件时发生错误", f"错误信息：{e}")
    #    return None
    finally:
        if f:
            f.close()


def save_file(staff_data):  # 将数据写入文件（写入失败返回错误信息）
    f = None
    try:
        f = open(staff_file, "w", encoding=codec, newline="")
        writer = csv.writer(f)  # 创建一个写入对象
        for staff in staff_data.items():  # 遍历员工数据
            data = [staff[0]]  # 将工号添加到列表中
            data.extend(list(staff[1].values()))  # 将员工数据添加到列表中
            writer.writerow(data)  # 将数据写入文件
        return None
    except PermissionError as e:
        msgbox.error("没有写入员工数据文件的权限", "请检查文件权限")
        return e
    #except Exception as e:
    #    msgbox.error("写入员工数据文件时发生错误", f"错误信息：{e}")
    #    return e
    finally:
        if f:
            f.close()
