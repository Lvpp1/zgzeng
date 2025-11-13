# -*- coding: utf-8 -*-
# @Time    : 2024/11/1 10:28
# @Author  : zgzeng
# @File    : wrapper.py



def common(func):
    """
    生成语法的装饰器
    :param func: 被装饰函数
    :return: 返回装饰器内存地址
    """
    def wrapper(self_instance, *args, **kwargs):
        with open(self_instance.target, "r", encoding="utf-8") as fh:
            content = [item.replace("\n", "") for item in fh.readlines()]
        results = []
        for grammer in content:
            result = func(self_instance, grammer)
            results.append(result)

        if func.__name__ == "fofa_domain_garamer" or func.__name__ == "fofa_icp_garamer" or func.__name__=="fofa_ip_garamer" or func.__name__=="fofa_keyword_garamer":
            return "||".join(results)
        if func.__name__ == "hunter_domain_grammer" or func.__name__ == "hunter_icp_grammer" or func.__name__=="hunter_ip_grammer" or func.__name__=="hunter_keyword_grammer":
            return "||".join(results)
        if func.__name__ == "quaker_domain_grammer" or func.__name__ == "quaker_icp_grammer" or func.__name__=="quaker_ip_grammer" or func.__name__=="quaker_keyword_grammer":
            return " OR ".join(results)
        if func.__name__ == "zoomeyes_domain_grammer" or func.__name__=="zoomeyes_icp_grammer" or func.__name__=="zoomeyes_ip_grammer" or func.__name__=="zoomeyes_keyword_grammer":
            return "||".join(results)

    return wrapper