######################################################################
# (C) 2019 Hirohisa Aman <aman@computer.org>
#
# java_keywords_eraser.py
# version 1.0
#
# This script reads a list of tokens,
# and prints the tokens other than Java keywords.
# The list of Java keywords is obtained from
#    https://docs.oracle.com/javase/specs/jls/se11/html/jls-3.html#jls-3.9
# The following three literals are treated as spcial keywords: true, false, null
#
# [useage]
# python java_keywords_eraser.py < word_list.txt > filtered_word_list.txt
#
######################################################################
import sys

keywords = ['abstract', 'assert', 'boolean', 'break', 'byte',
            'case', 'catch', 'char', 'class', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extends',
            'final', 'finally', 'float', 'for', 'if', 'goto',
            'implements', 'import', 'instanceof', 'int', 'interface',
            'long', 'native', 'new', 'package', 'private', 'protected',
            'public', 'return', 'short', 'static', 'strictfp', 'super',
            'switch', 'synchronized', 'this', 'throw', 'throws',
            'transient', 'try', 'void', 'volatile', 'while', '_',
            'true', 'false', 'null']

for line in sys.stdin:
    line = line.replace('\n','')
    line = line.replace('\r','')
    if line not in keywords:
        print(line)