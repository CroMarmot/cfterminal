# About cfterminal 

> Codeforces terminal tool

python3 only !

- [x] analyze contest's example in/out

- [x] test code

- [x] submit code

- [x] multiple language support [c++11/14/17 java8 supported now!]

# Usage


0. Install Dependency `pip3 install -r requirements.txt`
1. Install `time`, `sudo apt install time`, this `time` is powerful than linux built-in `time` check is `which time` returns `/usr/bin/time`
2. copy `_config.json` to `config.json` and modify it
3. run `parse.py <contestId>`
4. write code
5. run `test.sh <problemId>` (different testfile for different language)
6. run `submit.py <problemId>`

# Folder

```
├── _config.json
├── config.json
├── dist
│   └── <contestId>_<language>
├── languagecontestparse.py
├── language.json
├── LICENSE
├── Makefile
├── parse.py
├── README.md
├── requirements.txt
├── submit.py
├── template
│   ├── Main.cpp
│   ├── Main.go
└── testfile
    ├── README.md
    ├── testc++11.sh
    └── testc++17.sh
```

# TODO

implement java/python/golang 's template and testfile

add some error check (such as if file exist)

# About language.json

value in language.json is according to the option on codeforces' webpage

**Attention value is String in language.json instead of Number**

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

# Thinking and log

|history||
|---|---|
|0.0.7| remove click dependency , replace with argparse and print|
|0.0.6| rewrite test.sh (now only support c++17 and c++11)|
|0.0.5| support Div3's problem name such as D1 D2 in 1118|
|0.0.4| supporting handing during the contest [here also](https://github.com/endiliey/idne/issues/5)|
|0.0.3| replace config design with `_config.json`, and put generated code into `dist`, remove both from git track|
|0.0.2| design for ez use, reduce some argument|
|0.0.1| according to idne's code, remanage &fix |

# Reference

[idne](https://github.com/endiliey/idne)

[colors](https://misc.flogisoft.com/bash/tip_colors_and_formatting)

[robobrowser](https://robobrowser.readthedocs.io/en/latest/readme.html)
