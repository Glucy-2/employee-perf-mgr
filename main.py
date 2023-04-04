#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import account
from gui import account_form
from gui import msgbox


def run():  # 运行函数，用于运行程序
    init_result, init_created = account.init()  # 初始化账户，获取初始化结果和是否创建了默认账户
    try:
        if init_result:  # 如果初始化出错
            msgbox.error("初始化出错", f"错误信息：{init_result}")  # 显示错误对话框
            exit()  # 退出程序
        elif init_created:  # 如果创建了默认账户
            msgbox.info("已创建默认账户", "用户名为admin，密码为admin")  # 输出提示信息
        account_form.show()  # 显示登录窗口
    except Exception as e:
        print(e)
    # finally:


if __name__ == "__main__":  # 如果是直接运行本文件，则执行 run() 函数
    run()
