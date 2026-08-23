"""
测试使用OpenAI库调用阿里云平台云模型
"""
from openai import OpenAI
import os
# 创建类对象
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),         # 填入你的APIKEY
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"         # 填入你的模型供应商地址（OpenAI兼容端口）下载APIKEY文件内的（openAiCompatible）
)

# 发起对话
completion = client.chat.completions.create(
    model="qwen3.7-max",           # 模型名称
    messages=[
        {'role': 'system', 'content': '你是一个助理，回复言简意赅'},
        {'role': 'user', 'content': '你是谁，你能做什么'},
    ]
)

# 输出模型的回复
print(completion.choices[0].message.content)