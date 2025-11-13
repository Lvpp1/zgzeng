# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 10:12
# @Author  : zgzeng
# @File    : Grammer.py


import argparse
from module.DomainGrammer import GenerationDomainGrammer
from module.IcpGrammer import GenerationICPGrammer
from module.IpGrammer import GenerationIPGrammer
from module.KeyWordGrammer import GenerationKeyWordGrammer



def main():

    print("""
    
    =======================================================================
    空间搜索引擎检索语法:fofa---hunter---quake---zoomeye
    =======================================================================
    
    grammer.exe -d -f 域名存放文件 --fofa           # 生成fofa检索语法
    grammer.exe -i -p icp本案号存放文件 --fofa      # 生成icp的fofa检索语法
    grammer.exe -a -s ip存放路径  --fofa           # 生成ip的fofa检索语法
    grammer.exe -k -w 关键字存放路径 --fofa         # 生成关键字的fofa检索语法
    
    """)

    parser = argparse.ArgumentParser(description='搜索引擎语法生成工具')

    # 输入类型和文件参数
    input_group = parser.add_argument_group('输入类型')
    input_group.add_argument('-d', '--domain', action='store_true', help='通过域名生成语法')
    input_group.add_argument('-f', '--file', help='域名文件路径')

    input_group.add_argument('-i', '--icp', action='store_true', help='通过ICP备案号生成语法')
    input_group.add_argument('-p', '--icp-file', help='ICP备案号文件路径')

    input_group.add_argument('-a', '--ip', action='store_true', help='通过IP地址生成语法')
    input_group.add_argument('-s', '--ip-file', help='IP文件路径')

    input_group.add_argument('-k', '--keyword', action='store_true', help='通过关键词生成语法')
    input_group.add_argument('-w', '--keyword-file', help='关键词文件路径')

    # 搜索引擎选择
    search_group = parser.add_argument_group('搜索引擎')
    search_group.add_argument('--fofa', action='store_true', help='生成FOFA语法')
    search_group.add_argument('--hunter', action='store_true', help='生成Hunter语法')
    search_group.add_argument('--quaker', action='store_true', help='生成Quaker语法')
    search_group.add_argument('--zoomeye', action='store_true', help='生成ZoomEye语法')

    args = parser.parse_args()

    # 验证参数组合
    input_types = [args.domain, args.icp, args.ip, args.keyword]
    if sum(input_types) != 1:
        parser.error('必须且只能指定一种输入类型（-d/-i/-a/-k）')

    if not any([args.fofa, args.hunter, args.quaker, args.zoomeye]):
        parser.error('必须指定至少一个搜索引擎')

    # 确定输入文件和生成器类型
    if args.domain:
        if not args.file:
            parser.error('使用-d时必须指定-f参数')
        target_file = args.file
        generator_class = GenerationDomainGrammer
        grammar_type = "domain"

    elif args.icp:
        if not args.icp_file:
            parser.error('使用-i时必须指定-p参数')
        target_file = args.icp_file
        generator_class = GenerationICPGrammer
        grammar_type = "icp"

    elif args.ip:
        if not args.ip_file:
            parser.error('使用-a时必须指定-s参数')
        target_file = args.ip_file
        generator_class = GenerationIPGrammer
        grammar_type = "ip"

    elif args.keyword:
        if not args.keyword_file:
            parser.error('使用-k时必须指定-w参数')
        target_file = args.keyword_file
        generator_class = GenerationKeyWordGrammer
        grammar_type = "keyword"

    # 创建生成器实例
    generator = generator_class(target_file)
    results = []


    if args.fofa:

        method_name = f"fofa_{grammar_type}_garamer"
        if hasattr(generator, method_name):
            results.append(("FOFA", getattr(generator, method_name)()))
        else:
            print(f"警告: {generator_class.__name__} 没有 {method_name} 方法")

    if args.hunter:

        method_name = f"hunter_{grammar_type}_grammer"
        if hasattr(generator, method_name):
            results.append(("Hunter", getattr(generator, method_name)()))
        else:
            print(f"警告: {generator_class.__name__} 没有 {method_name} 方法")

    if args.quaker:

        method_name = f"quaker_{grammar_type}_grammer"
        if hasattr(generator, method_name):
            results.append(("Quaker", getattr(generator, method_name)()))
        else:
            print(f"警告: {generator_class.__name__} 没有 {method_name} 方法")

    if args.zoomeye:

        method_name = f"zoomeyes_{grammar_type}_grammer"
        if hasattr(generator, method_name):
            results.append(("ZoomEye", getattr(generator, method_name)()))
        else:
            print(f"警告: {generator_class.__name__} 没有 {method_name} 方法")


    for engine_name, query in results:
        print(f"\n=== {engine_name} 语法 ===")
        print(query)


if __name__ == '__main__':
    main()