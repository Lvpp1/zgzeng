# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 18:36
# @Author  : zgzeng
# @File    : IpGrammer.py

from module.wrapper import common

class GenerationIPGrammer:
    """根据IP备案号生成搜索语法"""

    def __init__(self, target):
        self.target = target
        self.grammerStr = ""
        self.grammer = ""

    @common
    def fofa_ip_garamer(self, grammer):
        """
        生成fofa检索域名语法
        :return: 返回检索语法
        """
        grammerStruct = f"ip='{grammer}'"
        return grammerStruct

    @common
    def hunter_ip_grammer(self, grammer):
        """
        生成hunter空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f"ip='{grammer}'"
        return grammerStruct

    @common
    def quaker_ip_grammer(self,grammer):
        """
        生成quaker空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f'ip:"{grammer}"'
        return grammerStruct

    @common
    def zoomeyes_ip_grammer(self, grammer):
        """
        生成zoomeye空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f'ip="{grammer}"'
        return grammerStruct
