# 1.导包
from ollama import chat


# 2.调用ollama模型发送请求，接收响应
response = chat(
  model="qwen2.5:7b",
  messages=[
    {"role": "user", "content": "给我讲个笑话"}
  ]
)
# 3.打印结果
print(response["message"]["content"])