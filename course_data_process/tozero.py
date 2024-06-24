import json

# 读取 JSON 文件
with open('./data/zh/val.json', 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

# 遍历每条数据，添加新属性 'pred'
for index, entry in enumerate(data):
    entry['td_rationale'] = ""
    entry['td_pred'] = 2
    entry['td_acc'] = 0

    entry['cs_rationale'] = ""
    entry['cs_pred'] = 2
    entry['cs_acc'] = 0

# 将修改后的数据写回 JSON 文件
with open('./course_data/zh_both_tozero/val.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
