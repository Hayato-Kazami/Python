# 1.导包
from ollama import chat
from ollama import ChatResponse

# 2.调用ollama模型发送请求，接收响应
stream : ChatResponse = chat(
    model="qwen2.5:7b",
    messages=[
        {"role": "user", "content": "帮我写关于冬天的词，豪放派和婉约派各一首"}
    ],
    stream=True
)
# 3.打印结果
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)