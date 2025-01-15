# 引入测试用例 excel地址
from common import util

excel_path = '../testdata/raw.xlsx'
# 引入测试用例 excel的表名
excel_outside = 'Sheet1'
raw_list = []
raws = util.read_data(excel_path, excel_outside)
for raw in raws:
    raw_name = raw.get('names')
    print(raw_name)
    raw_list.append(raw_name)

print(raw_list)
print(len(raw_list))
