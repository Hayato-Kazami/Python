from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# 系统提示词
system_prompt = """
你是一个反义词高手
"""

user_prompt = "i am cute"

completion = client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[
        # （可以理解为伪造聊天记录，修改模型的三观）达到FewShot少样本示例的作用
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "大"},
        {"role": "assistant", "content": "你大个蛋"},
        {"role": "user", "content": "高"},
        {"role": "assistant", "content": "你高个锤子"},
        {"role": "user", "content": "肥"},
    ],
)

print(completion.choices[0].message.content)