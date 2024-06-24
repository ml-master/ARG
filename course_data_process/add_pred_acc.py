import json

# 读取 JSON 文件
with open('./course_data/process2/test3.json', 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)
sum = 0
# 遍历每条数据，添加新属性 'pred'
for index, entry in enumerate(data):
    entry['source_id'] = index
    # if entry['td_rationale'].find("1") != -1 and entry['td_rationale'].find("0") == -1:
    #     entry['td_pred'] = 1
    #     entry['td_acc'] = 1 if entry['label'] == 1 else 0
    # elif entry['td_rationale'].find("1") == -1 and entry['td_rationale'].find("0") != -1:
    #     entry['td_pred'] = 0
    #     entry['td_acc'] = 1 if entry['label'] == 0 else 0
    # else:
    #     entry['td_pred'] = 2
    #     entry['td_acc'] = 0
    #
    # if entry['cs_rationale'].find("1") != -1 and entry['cs_rationale'].find("0") == -1:
    #     entry['cs_pred'] = 1
    #     entry['cs_acc'] = 1 if entry['label'] == 1 else 0
    # elif entry['cs_rationale'].find("1") == -1 and entry['cs_rationale'].find("0") != -1:
    #     entry['cs_pred'] = 0
    #     entry['cs_acc'] = 1 if entry['label'] == 0 else 0
    # else:
    #     entry['cs_pred'] = 2
    #     entry['cs_acc'] = 0
    #     # print(index)
    if entry['label'] == 0:
        sum += 1
    # sum += 1
print(sum)
# 将修改后的数据写回 JSON 文件
with open('./course_data/process2/test3.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
