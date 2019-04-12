#!-*- coding:utf-8 -*-
#__author__:"irving"

from django.shortcuts import HttpResponse
from stark.service.v1 import site
from app01 import models


class HostHandler(object):

    def __init__(self, model_class):
        self.model_class = model_class

    def changelist_view(self, request):
        """
        主机页面
        :param request:
        :return:
        """
        return HttpResponse("主机列表页面")

    def add_view(self, request):
        """
        添加页面
        :param request:
        :return:
        """
        pass

    def change_view(self, request):
        """
        编辑页面
        :param request:
        :return:
        """
        pass

    def delete_view(self, request):
        """
        删除页面
        :param request:
        :return:
        """
        pass


site.register(models.Depart, HostHandler)


# class UserInfoHandler(object):
#
#     def __init__(self, model_class):
#         self.model_class = model_class
#
#     def changelist_view(self, request):
#         """
#         列表页面
#         :param request:
#         :return:
#         """
#         return HttpResponse("用户列表页面")
#
#     def add_view(self, request):
#         """
#         添加页面
#         :param request:
#         :return:
#         """
#         pass
#
#     def change_view(self, request):
#         """
#         编辑页面
#         :param request:
#         :return:
#         """
#         pass
#
#     def delete_view(self, request):
#         """
#         删除页面
#         :param request:
#         :return:
#         """
#         pass
#
#
# site.register(models.UserInfo, UserInfoHandler)
