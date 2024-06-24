import json
import random

# 假设您的JSON文件名为data.json
file_path = './course_data/gossipcop_v3-1_style_based_fake.json'
train_path = './course_data/extract/train.json'
test_path = './course_data/extract/test.json'
val_path = './course_data/extract/val.json'

# 打开并读取JSON文件
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 计算一半键的数量
half_length = len(data) // 3
# 取前一半键值对
keys = list(data.keys())
half_keys = keys[:half_length]
data = {key: data[key] for key in half_keys}

# print(json.dumps(next(iter(data.values())), indent=4, ensure_ascii=False))
# 获取所有键并随机打乱
keys = list(data.keys())
random.shuffle(keys)

# 计算分割点
total_len = len(keys)
train_len = int(total_len * 0.6)
val_len = int(total_len * 0.2)

# 根据计算的长度分割键
train_keys = keys[:train_len]
val_keys = keys[train_len:train_len + val_len]
test_keys = keys[train_len + val_len:]

# 使用这些键来创建对应的数据集
train_data = {key: data[key] for key in train_keys}
val_data = {key: data[key] for key in val_keys}
test_data = {key: data[key] for key in test_keys}
def process_data(data, name):
    # 创建一个列表来存储提取的数据
    extracted_data = []
    # 遍历JSON数据
    for index, (key, value) in enumerate(data.items()):
        # 提取需要的字段
        origin_label = value.get('origin_label')
        generated_text = value.get('generated_text')

        if origin_label == 'fake':
            origin_label = 0
        else:
            origin_label = 1

        origin_id = index
        # 将提取的数据添加到列表中
        extracted_data.append({
            'content': generated_text,
            'label': origin_label,
            'source_id': origin_id,
            # 'td_rationale': '',
            # 'td_pred': '',
            # 'td_acc': '',
            # 'cs_rationale': '',
            # 'cs_pred': '',
            # 'cs_acc': '',
            'split': name
        })
    return extracted_data

train_data = process_data(train_data, 'train')
test_data = process_data(test_data, 'test')
val_data = process_data(val_data, 'val')

# 保存数据到不同的JSON文件中
with open(train_path, 'w', encoding='utf-8') as file:
    json.dump(train_data, file, ensure_ascii=False, indent=4)

with open(test_path, 'w', encoding='utf-8') as file:
    json.dump(test_data, file, ensure_ascii=False, indent=4)

with open(val_path, 'w', encoding='utf-8') as file:
    json.dump(val_data, file, ensure_ascii=False, indent=4)

print("数据已分割并保存到指定文件")
