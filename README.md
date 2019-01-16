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


# DEP

bs4/htmlparser

request...python default module

# ARGMENT 

1. --user --pass
2. config.py
3. default



config.py
language = ""


