# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 9:46
# @Author  : zgzeng
# @File    : DomainGrammer.py


from module.wrapper import common


class GenerationDomainGrammer:
    """根据域名生成搜索语法"""

    def __init__(self, target):
        self.target = target
        self.grammerStr = ""
        self.grammer = ""

    def process_domain(self, grammer):
        """处理域名，提取出对应的cert的根"""
        if grammer.endswith(".com.cn"):
            grammer = grammer.split(".")[-3]
        elif grammer.endswith(".cn") or grammer.endswith(".com"):
            grammer = grammer.split(".")[-2]
        else:
            grammer = grammer

        return grammer

    @common
    def fofa_domain_garamer(self, grammer):
        """
        生成fofa检索域名语法
        :return: 返回检索语法
        """
        grammerProcess = self.process_domain(grammer)
        grammerStruct = f"domain='{grammer}'||host='{grammer}'||cert='{grammer}'||cert='{grammerProcess}'||cert.subject.cn='{grammer}'||cert.domain='{grammer}'"
        return grammerStruct

    @common
    def hunter_domain_grammer(self, grammer):
        """
        生成hunter空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerProcess = self.process_domain(grammer)
        grammerStruct = f"domain.suffix='{grammer}'||domain='{grammerProcess}'||cert='{grammerProcess}'||cert.subject='{grammer}'||cert.subject.suffix='{grammer}'"
        return grammerStruct

    @common
    def quaker_domain_grammer(self,grammer):
        """
        生成quaker空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerProcess = self.process_domain(grammer)
        grammerStruct = f'domain:"{grammer}" OR hostname:"{grammer}" OR cert:"{grammer}" OR host:"{grammer}" OR cert:"{grammerProcess}"'

        return grammerStruct

    @common
    def zoomeyes_domain_grammer(self, grammer):
        """
        生成zoomeye空间搜索引擎检索语法
        :return: 返回语法字符串
        """
        grammerProcess = self.process_domain(grammer)
        grammerStruct = f'domain="{grammer}"||"hostname={grammer}"||ssl="{grammerProcess}"||ssl.cert.issuer.cn="{grammer}"||ssl.cert.subject.cn="{grammer}"'
        return grammerStruct





