# -*- coding: utf-8 -*-


import os
import csv
from staff import Staff
from gui import msgbox

# 数据存储在staff.csv，UTF-8编码

staff_file = f"{os.path.abspath('.')}/staff.csv"
codec = "UTF-8"


def read_file(staff_list):  # 将文件的内容读出并返回长度（读取失败返回0）
    f = None
    try:
        f = open(staff_file, "r", encoding=codec)
        reader = csv.reader(f)  # 读取csv文件中的数据
        for row in reader:  # 遍历每一行数据
            one_taff = Staff(
                row[0],
                row[1],
                row[2],
                {1: row[3], 2: row[4], 3: row[5], 4: row[6]},
                row[7],
                row[8],
            )
            staff_list.append(one_taff)
        return len(staff_list)  # 返回长度
    except FileNotFoundError as e:
        msgbox.error("员工数据文件不存在", "请检查文件是否存在")
        return 0
    except PermissionError as e:
        msgbox.error("没有读取员工数据文件的权限", "请检查文件权限")
        return 0
    except Exception as e:
        msgbox.error("读取员工数据文件时发生错误", f"错误信息：{e}")
        return 0
    finally:
        if f:
            f.close()


def save_file(staff_list):  # 将数据写入文件（写入失败返回错误信息）
    f = None
    try:
        f = open(staff_file, "w", encoding=codec, newline="")
        writer = csv.writer(f)  # 创建一个写入对象
        for one_sta in staff_list:  # 遍历员工数据
            writer.writerow(
                [
                    one_sta.getNum(),
                    one_sta.getName(),
                    one_sta.getGender(),
                    str(one_sta.getScore()[1]),
                    str(one_sta.getScore()[2]),
                    str(one_sta.getScore()[3]),
                    str(one_sta.getScore()[4]),
                    str(one_sta.getTotal()),
                    str(one_sta.getRank()),
                ]
            )  # 将数据写入文件
        return None
    except PermissionError as e:
        msgbox.error("没有写入员工数据文件的权限", "请检查文件权限")
        return e
    except IOError:
        msgbox.error("打开员工数据文件时发生错误", "")
        return e
    except Exception as e:
        msgbox.error("写入员工数据文件时发生错误", f"错误信息：{e}")
        return e
    finally:
        if f:
            f.close()
