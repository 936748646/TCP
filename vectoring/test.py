import csv

'''
f = open('test.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow([1, 2, 3])
csv_writer.writerow([2, 5, 4])
csv_writer.writerow([3, 4, 6])
csv_writer.writerow([4, 5, 1])
csv_writer.writerow([2, 2, 0])
f.close()
'''
'''
f = open('testcase_name.csv', 'r', encoding='utf-8', newline="")
reader = csv.reader(f)
with open(csv) as table_file:
    print(table_file)
    reader = csv.reader(table_file)
'''
'''
import numpy as np

if __name__ == '__main__':
    x = np.random.random(10)
    y = np.random.random(10)
    print(type(x))
    print(y)

    # 根据公式求解曼哈顿距离
    d1 = np.sum(np.abs(x - y))
    print(d1)
    sum1 = 0.078947368 + 0.913157895 + 0.004651163*3 + 0.002631579*3 + 0.493023256*2
    sum2 = 0.001984127 + 0.08234127-0.078947368 + 0.913157895 + 0.004960317 + 0.002631579*3 + 0.000992063 + 0.906746032 + 0.00297619
    print(sum1)
    print(sum2)
'''

import os

dir_list = os.listdir('./derby/v5/pre')
f = open('./derby/v5/thomas_result_derbyv5.csv', 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f, dialect='excel')
print(dir_list)
for i in dir_list:
    csv_writer.writerow([i])
'''

import os

path = 'derby/v5/topics'

# 获取该目录下所有文件，存入列表中
file_list = os.listdir(path)

for i in file_list:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + i  # os.sep添加系统分隔符
    print(oldname)
    # 设置新文件名
    newname = path + os.sep + i.split('.')[0] + '.csv'

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)
'''
'''
distance1 = 0.078947368-0.06124604+0.753959873+0.913157895+0.053854277-0.002631579+0.002631579+0.002631579+0.13093981
distance2 = 0.078947368+0.913157895+0.004651163+0.004651163+0.004651163+0.002631579+0.493023256+0.002631579+0.002631579+0.493023256
print(distance1)
print(distance2)
'''