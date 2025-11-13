# Grammar 项目

这是一个用来生成网络安全空间搜索引擎的检索语法，用于安服生成检索公网暴漏面的搜索语法

生成fofa, hunter, quake, zoomeye的检索语法

## 项目概述

用于自己在安全服务工作中，做暴漏面检测的时候，直接生成搜索语法

## 目录结构

```
grammar/
├── src/
│   ├── module/                    # 模块包
│   │   ├── __init__.py
│   │   ├── DomainGrammar.py       # 通过域名生成检索语法的类
│   │   ├── IcpGrammar.py          # 通过icp备案生成检索语法的类
│   │   ├── IpGrammar.py           # 通过ip生成检索语法的类
│   │   ├── KeyWordGrammar.py      # 通过关键字生成检索语法的类
│   │   └── wrapper.py             # 装饰器，用于避免代码冗余，修饰其他模块中的类方法
│   ├── __init__.py
│   └── Grammar.py                 # 主入口文件
├── README.md
└── 其他文件...
```

## 使用说明
exe压缩包：
grammer.exe -d -f 域名存放文件 --fofa           # 生成fofa检索语法
grammer.exe -i -p icp本案号存放文件 --fofa      # 生成icp的fofa检索语法
grammer.exe -a -s ip存放路径  --fofa           # 生成ip的fofa检索语法
grammer.exe -k -w 关键字存放路径 --fofa         # 生成关键字的fofa检索语法

python源码：
python grammer.py -d -f 域名存放文件 --fofa           # 生成fofa检索语法
python grammer.py -i -p icp本案号存放文件 --fofa      # 生成icp的fofa检索语法
python grammer.py -a -s ip存放路径  --fofa           # 生成ip的fofa检索语法
python grammer.py -k -w 关键字存放路径 --fofa         # 生成关键字的fofa检索语法
