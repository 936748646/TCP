###############################################################
# (C) 2020 Hirohisa Aman <aman@ehime-u.ac.jp>
# A shell script running the preprocessing of a Java test case
###############################################################
# (1) erase non-alphabetical characters
# (2) tokenize the content of the test case
# (3) erase Java language keywords
# (4) split camelCase identifiners
# (5) decapitalize all tokens, then perform the stemming and the stop-word elimination
############################################################################################

############################################################################################
# settings
#
python="python3"
#
step1="$python non_alphabet_eraser.py"
step2="$python simple_tokenizer.py"
step3="$python java_keywords_eraser.py"
step4="$python camel_splitter.py"
step5="$python stemmer_and_stopwords_eraser.py"
############################################################################################
# execution
#
testcase=$1
cat $testcase |
$step1 |
$step2 |
$step3 |
$step4 |
$step5
