# About

cfterminal - codeforces terminal tool

python3 only !

[x] 1. analyze contest's example in/out

[x] 2. test code

[x] 3. submit code

[ ] 4. multiple language support(C++17 C++11 ...)

# Usage

0. Install Dependency `pip3 install -r requirements.txt`
1. cp `_config.py` to `config.py` and modify it
2. run `parse.py ` + contestId
3. write code
4. run `test.py/sh` (考虑中 目前的感觉还是不要合并成一种？)
5. run `submit.py`

# DESIGN

```
./
├── color.py
├── _config.json
├── handin.py
├── language.json
├── LICENSE
├── Makefile
├── myparse.py
├── parse.py
├── README.md
├── requirements.txt
├── submit.py
├── template
│   ├── Main.cpp
│   ├── Main.go
│   └── Main.java
└── testfile
    ├── README.md
    ├── testc++11.sh
    ├── testc++17.sh
    └── testjava.sh
```

# TODO

实现 java,python的template 以及 测试

全英文

增加错误检查(比如缺少文件等等)

# 相关

language.json 的value值 和cf上的select选择框 对应

**注意配置language.json时这一项是字符串不是数字**

|compiler|value|
|---|---|
|GNU GCC C11 5.1.0|43|
|Clang++17 Diagnostics| 52|
|GNU G++11 5.1.0| 42|
|GNU G++14 6.4.0| 50|
|GNU G++17 7.3.0| 54|
|Microsoft Visual C++ 2010| 2|
|Microsoft Visual C++ 2017| 59|
|C# Mono 5.18| 9|
|D DMD32 v2.083.1| 28|
|Go 1.11.4| 32|
|Haskell GHC 7.8.3 (2014.2.0.0)| 12|
|Java 1.8.0_162| 36|
|Kotlin 1.3.10| 48|
|OCaml 4.02.1| 19|
|Delphi 7| 3|
|Free Pascal 3.0.2| 4|
|PascalABC.NET 3.4.2| 51|
|Perl 5.20.1| 13|
|PHP 7.2.13| 6|
|Python 2.7.15| 7|
|Python 3.7.2| 31|
|PyPy 2.7 (6.0.0)| 40|
|PyPy 3.5 (6.0.0)| 41|
|Ruby 2.0.0p645| 8|
|Rust 1.31.1| 49|
|Scala 2.12.8| 20|
|JavaScript V8 4.8.0| 34|
|Node.js 9.4.0| 55|

# 编写思考+进度

0.0.7 移除了Click(原来只用于解析 两个参数和print)，这里直接用argparse+print实现
0.0.6 修改了测试shell，目前先写的是C++的，之后可能会看java等等通用的样子再改一改
0.0.5 支持了Div3题目 比如1118中D1 D2，原来解析器解析不了
0.0.4 支持了比赛时提交（原来的项目因为cf的页面设计 不能在外部提交进行中的比赛代码）
0.0.3 把config设计为_config.json,生成的具体比赛代码放入dist,均从版本跟踪中去除
0.0.2 希望从使用最简便的方式反向思考去设计结构,简化了参数 修改目录结构
0.0.1 根据idne的代码 把部分代码进行移动整理 修复一些设计 修复空格tab混用

# 工作流程

0. 用户先配置config.json (用户名，密码，语言(所有语言支持见language.json))
1. 运行parse.py+比赛id，通过URL获取比赛页面
2. 通过HTML分析出所有题目的名字
3. 通过题目名字得到URL，获取题目页面，分析HTML，得到样例输入输出
4. 根据语言配置建立文件夹，并复制模板程序，测试程序，提交程序，生成state.json(比赛id，语言value，程序后缀)，和上面分析得到的样例
5. 测试[可选]自己运行测试代码
6. 提交[可选]根据state.json（比赛id，语言，后缀）和最外层的config.json（用户名和密码）,和用户传递的题号(如A)，直接提交
7. 通过codeforces提供的api查询提交结果并显示

# Reference

[idne](https://github.com/endiliey/idne)

[colors](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

[robobrowser](https://robobrowser.readthedocs.io/en/latest/readme.html)