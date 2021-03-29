import sys
import csv
import math
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
'''
args = sys.argv

dir = args[2]
vec_dir = args[3]
'''
name_dir = 'testcase_name.csv'
dir = 'preprocessed_result'
vec_dir = 'test_result'

print("Reading preprocessed test cases ...", file=sys.stderr)
texts = []
with open(name_dir) as table_file:
    reader = csv.reader(table_file)
    for row in reader:
        with open(dir + "/" + row[0] + ".txt") as txt_file:
            token_list = []
            for token in txt_file:
                token = token.replace('\n','')
                token = token.replace('\r','')
                token_list.append(token)
            texts.append(token_list)

print("Making Doc2Vec model ...", file=sys.stderr)
documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(texts)]

dim = math.floor(len(texts)/2.5)
if ( dim - len(texts)/2.5) >= 0.5:
    dim = dim + 1

print("Computing vectors of test cases ...", file=sys.stderr)
for cnt in range(30):
    print("[" + str(cnt) + "]", file=sys.stderr)
    #model = Doc2Vec(documents, vector_size=dim, dm=0, min_count=1, epochs=20)
    model = Doc2Vec(documents, vector_size=dim, dm=0, seed=cnt)
    with open(vec_dir + "/" + str(cnt) + ".csv", mode='w') as vec_file:
        for i in range(len(texts)):
            is_first = True
            for elem in model.docvecs[i]:
                if is_first:
                    is_first = False
                else:
                    vec_file.write(",")
                vec_file.write(str(elem))
            vec_file.write("\n")
