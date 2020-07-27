import re
regex = r'^\d+\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'
for _ in range(int(input())):
    if re.match(regex, input()):
        print('VALID')
    else:
        print('INVALID')
