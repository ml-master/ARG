# ARG ["**Bad Actor, Good Advisor: Exploring the Role of Large Language Models in Fake News Detection**"] AAAI 2024

官方代码地址： https://arxiv.org/abs/2309.12247

## Dataset

论文中的数据集需要向作者申请，所以不会出现在我的仓库中。此处只提供申请地址：https://forms.office.com/r/eZELqSycgn
关于新的数据集是在gossipcop_v3-1_style_based_fake.json的基础上进行处理，处理代码在course_data_process，最终的数据集在course_data中，包括新的数据集、负采样数据集、消融实验数据集。

## Code

### Requirements
- python==3.10.13
- CUDA: 11.3

### Pretrained Models
论文中使用到bert的预训练模型，下载地址：
[bert-base-uncased]：https://huggingface.co/google-bert/bert-base-uncased
[chinese-bert-wwm-ext]：https://huggingface.co/hfl/chinese-bert-wwm-ext

### Run
运行只需执行run_en.sh或者run_zh.sh中的命令即可。
