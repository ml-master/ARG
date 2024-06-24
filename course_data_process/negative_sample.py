import json
import random

# 读取JSON文件
file_path = './course_data/process2/test2.json'
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

# 过滤出label为0的数据
label_0_data = [item for item in data if item.get('label') == 0]

# 确定要删除的数量（例如删除一半的label为0的数据）
num_to_delete = 400

# 随机选择要删除的项
items_to_delete = random.sample(label_0_data, num_to_delete)

# 删除选中的项
filtered_data = [item for item in data if item not in items_to_delete]

# 保存过滤后的数据回JSON文件
with open('./course_data/process2/test3.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4, ensure_ascii=False)

# print(f"Deleted {num_to_delete} items with label 0.")

