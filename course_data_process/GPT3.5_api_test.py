import requests
from openai import OpenAI
import json

client = OpenAI(
    base_url = "***",
    api_key = "***"
)

def process_line(line):
    # 修复行的常见问题
    line = line.replace('}\n{', '},\n{')
    return line

data = []
with open('./course_data/process2/val2.json', 'r', encoding='utf-8', errors='ignore') as f:
    data = json.load(f)
# sum = 0
for index, item in enumerate(data):
    # data[index]['source_id'] = index
    # if index <= 903:
    #     continue
    if item['cs_rationale'] == "1" or item['cs_rationale'] == "0":
        print(index)
        # sum += 1
        content = item['content']
        # prompt就是输入的文本
        prompt = f"Given the following message, predict its veracity. If it is more likely to be a real message, return 1; otherwise, return 0. Please refrain from providing ambiguous assessments such as undetermined: {content} Let’s think from the perspective of commonsense. you must give your analysis more than 80 words, and return 0 or 1.\n"
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        # 调用 GPT 模型生成结果
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        cs_rationale = response.choices[0].message.content
        if cs_rationale == "1" or cs_rationale == "0":
            print("only 0 or 1.")
        data[index]['cs_rationale'] = cs_rationale
        # result = {
        #     'content': item['content'],
        #     'label': item['label'],
        #     'source_id': index,
        #     'td_rationale': td_rationale,
        #     'cs_rationale': item['cs_rationale'],
        #     'split': 'val'
        # }
    with open('./course_data/process2/val2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
# print(sum)


