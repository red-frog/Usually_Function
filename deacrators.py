# -*- coding:utf-8 -*-
from django.shortcuts import redirect
# 装饰器装饰判断用户是否登录, django项目中


def login_required(view_funciton):
    '''验证是否登录'''
    def wrapper(request, *args, **kwargs):
        if 'islogin' in request.session:
            return view_funciton(request, *args, **kwargs)
        else:
            # 跳转到登录或注册页面
            return redirect('/')
    return wrapper


@login_required
def view_function():
    pass


if __name__ == '__main__':
    view_function()