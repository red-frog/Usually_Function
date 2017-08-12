# -*- coding:utf-8 -*-
# 用户登录后返回以前访问的url,使用中间件，注意得注册中间件


class UrlPathRecordMiddleware(object):
    '''记录用户访问地址'''
    # 不记录的url地址
    exclude_path = ['/user/login/', '/user/logic_check/']

    def process_view(self, request):
        # 此方法在url匹配后视图函数调用前使用
        # request.path 获取url地址，不含参数
        url_path = request.path
        if url_path not in UrlPathRecordMiddleware.exclude_path:
            # 记录url地址, request.get_full_path():获取带参数路径
            request.session['url_pre_login'] = request.get_full_path()
            