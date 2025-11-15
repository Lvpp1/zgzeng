# -*- coding: utf-8 -*-
# @Time    : 2024/11/7 18:51
# @Author  : zgzeng
# @File    : KeyWordGrammer.py


from module.wrapper import common


class GenerationKeyWordGrammer:
    """根据关键字生成搜索语法"""

    def __init__(self, target):
        self.target = target
        self.grammerStr = ""
        self.grammer = ""


    @common
    def fofa_keyword_garamer(self, grammer):
        """
        生成fofa检索域名语法
        :return: 返回检索语法
        """
        grammerStruct = f"body='{grammer}'||title='{grammer}'||cert='{grammer}'||cert.subject.org='{grammer}'"
        return grammerStruct

    @common
    def hunter_keyword_grammer(self, grammer):
        """
        生成hunter空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f"body='{grammer}'||title='{grammer}'||icp.web_name='{grammer}'||icp.name='{grammer}'"
        return grammerStruct

    @common
    def quaker_keyword_grammer(self,grammer):
        """
        生成quaker空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f'body:"{grammer}" OR title:"{grammer}" OR cert:"{grammer}" OR icp_keywords:"{grammer}"'

        return grammerStruct

    @common
    def zoomeyes_keyword_grammer(self, grammer):
        """
        生成zoomeye空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerStruct = f'icp.name="{grammer}"||"body={grammer}"||title="{grammer}"'
        return grammerStruct
