import json

# 1. 读取整个文件内容为字符串
with open('./course_data/process2/val.json', 'r', encoding='utf-8', errors='ignore') as f:
    data_str = f.read()

# 2. 添加逗号分隔符和外部的 []
# 假设每个对象之间用 '}{' 连接，没有外部的 []，并且最后没有逗号分隔符
data_str = '[' + data_str.replace('}\n{', '},\n{') + ']'
# print(data_str)
# 3. 解析为 JSON 数据
data = json.loads(data_str)

# 5. 保存回文件
with open('./course_data/process2/val2.json', 'w') as f:
    json.dump(data, f, indent=4)
