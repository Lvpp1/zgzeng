# -*- coding: utf-8 -*-
# @Time    : 2024/10/10 15:04
# @Author  : zgzeng
# @File    : IcpGrammer.py

from module.wrapper import common

class GenerationICPGrammer:
    """根据ICP备案号生成搜索语法"""

    def __init__(self, target):
        self.target = target
        self.grammerStr = ""
        self.grammer = ""

    def process_icp_number(self, grammer):
        """处理icp号"""
        return grammer.split("-")[0]


    @common
    def fofa_icp_garamer(self, grammer):
        """
        生成fofa检索域名语法
        :return: 返回检索语法
        """
        icp_number_Process = self.process_icp_number(grammer)
        grammerStruct = f"icp='{icp_number_Process}'"
        return grammerStruct

    @common
    def hunter_icp_grammer(self, grammer):
        """
        生成hunter空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f"icp.number='{grammer}'"
        return grammerStruct

    @common
    def quaker_icp_grammer(self,grammer):
        """
        生成quaker空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        icp_number_Process = self.process_icp_number(grammer)
        grammerStruct = f'icp:"{icp_number_Process}"'
        return grammerStruct

    @common
    def zoomeyes_icp_grammer(self, grammer):
        """
        生成zoomeye空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f'icp.number="{grammer}"'
        return grammerStruct