# -*- coding:utf-8 -*-
import copy
from django.db import models


class BaseModelManager(models.Manager):

    def get_all_valid_fields(self):
        # 获取模型类的属性列表
        # 1.获取模型类
        cls = self.model
        # 2.获取属性列表，django中方法__meta.get_fields()
        attr_list = cls.__meta.get_fields()
        attr_str_list = []
        for attr in attr_list:
            if isinstance(attr, models.ForeignKey):
                # 获取外键字段，修改其属性名
                attr = '%s_id' % attr.name
                attr_str_list.append(attr)
            else:
                attr_str_list.append(attr.name)
        return attr_str_list

    def create_one_object(self, **kwargs):
        # 创建对象
        # 1.获取属性列表
        valid_fields = self.get_all_valid_fields()
        # 拷贝列表，解决for循环删除问题
        kws = copy.copy(kwargs)
        for k in kws:
            if k not in valid_fields:
                kwargs.pop(k)
        # 获取所在模型类
        cls = self.model
        obj = cls(**kwargs)
        obj.save()
        return obj
