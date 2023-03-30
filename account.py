#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 账户模块，用于登录/修改密码

import os
from hashlib import sha256

logged_in = False # 是否已登录，用于其他模块判断和设置是否已登录

# 密码文件路径和编码
password_file = f"{os.path.abspath('.')}/password.txt"
codec = 'UTF-8'

# SHA256 加密
def encrypt(content):
    return sha256(content.encode(codec)).hexdigest() # 先将字符串解码为字节流（encode），再进行加密，然后将加密后的字节流进行摘要（hexdigest）


# 初始化，检查账户文件是否存在，不存在则写入默认账户，返回值为发生的错误信息和是否尝试创建了默认账户
def init():
    if not os.path.isfile(password_file) or not os.path.getsize(password_file): # 账户文件对应的路径不是文件（是文件夹或者不存在）或文件为空
        result = write(encrypt('admin')) # 默认密码为admin，加密后写入文件并获取结果
        return result, True
    else: # 账户文件对应的路径是文件
        return None, False


# 检查密码是否正确，传入加密后的密码，返回错误信息和密码是否正确
def check(encrypted_password):
    f = None
    try:
        f = open(password_file, 'r+', encoding = codec)
        f.seek(0)
        file_password = f.read() # 读取文件中的密码
        if file_password == encrypted_password: # 密码正确
            return None, True
        else: # 密码错误
            return None, False
    except FileNotFoundError: # 文件不存在
        return '密码文件不存在', None
    except PermissionError: # 没有权限
        return '没有读取密码文件的权限', None
    except Exception as e: # 发生其他错误
        return e, None
    finally:
        if f: # 如果文件已经打开，则关闭文件
            f.close()


# 写入账户信息，传入加密后的密码，返回错误信息
def write(encrypted_password):
    f = None
    try:
        f = open(password_file, 'w', newline='', encoding=codec)
        f.write(encrypted_password)
        return None
    except PermissionError: # 没有权限
        return '没有写入密码文件的权限'
    except Exception as e:
        return e
    finally:
        if f:
            f.close()
