# -*- coding:utf-8 -*-
from hashlib import sha1


def get_hash(a, salt=None):
    # 字符串前后加入特殊符号
    a = "$#@%%^!*" + a + "!@#$%"
    if salt:
        a = a + salt
    # 获得哈希值并返回
    sh = sha1()
    a = a.encode()
    sh.update(a)
    return sh.hexdigest()


if __name__ == "__main__":
    secret = get_hash('python')
    print(secret)