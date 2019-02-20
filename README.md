# About

cfterminal - codeforces terminal tool

# Functions

1. analyze contest's example in/out

2. test code

3. handin code

# Dependence

bs4/htmlparser

`pip install beautifulsoup4`

request...python default module

time

in test , the code use time instead of default time

`sudo apt install time`

# Usage

1. cp `_config.py` to `config.py` and modify it
2. run `parse.py ` + contestId
3. write code
4. run `test.py/sh`
5. run `submit.py`

对于反复循环使用

1. 运行解析 ./parse.py 比赛id，不带任何其它参数，进入工作目录
2. 进行编码 (分多个目录或者全一个目录)
3. 执行测试./test.sh/.py A (不用关心比赛id) 
4. 提交./submit.py/sh A (不用关心比赛id，文件后缀，语言选择) 并返回结果

用户名密码存最外

当需要换语言时，一个是参数parse.py,配置config（默认语言），support（支持,模板，测试文件，语言选择配置）

# DESIGN

module division 

1. argparse (from args/config.py/default)
2. login && cookie 
3. parse problem example and download
4. test (bash)
5. submit (bash)

DIR:

```
template/
  a.cpp
_id.py
language.json : compiler insuffix(.cpp) outsuffix(.)
cft_parse.py
cft_handin.py
module/
  argparse.py (username / password / contestid / language )
  webwrap.py (login && keep cookie && visit && return result)
  analyser.py (bs4 + problem analyse)
  localgen.py (generate local file test file and so on)
.gitignore
dist/
  contestID/
    language+version/
      A.cpp
      B.cpp
      a.in.1
      a.out.1
      usr.out.1
      ./test.sh X
      makefile :make clean
README.md
makefile :makeclean
```


# ARG 

1. --user --pass
2. config.json

# TODO

实现提交

制作java的template

实现 java,python的template 和测试

加上参数支持 比如 user pass 比赛语言

整理代码结构 命名

全英文

增加错误检查(比如缺少文件等等)

# 相关

关于language.json 的value值 和cf上的select选择框 对应

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

0.0.6 修改了测试shell，目前先写的是C++的，之后可能会看java等等通用的样子再改一改
0.0.5 支持了Div3题目 比如1118中D1 D2，原来解析器解析不了
0.0.4 支持了比赛时提交（原来的项目因为cf的页面设计 不能在外部提交进行中的比赛代码）
0.0.3 把config设计为_config.json,生成的具体比赛代码放入dist,均从版本跟踪中去除
0.0.2 希望从使用最简便的方式反向思考去设计结构,简化了参数 修改目录结构
0.0.1 根据reference的代码 把部分代码进行移动整理

# reference

https://github.com/endiliey/idne

https://misc.flogisoft.com/bash/tip_colors_and_formatting