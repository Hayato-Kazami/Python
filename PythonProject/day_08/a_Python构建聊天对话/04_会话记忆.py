# 1.导包
from ollama import chat
from ollama import ChatResponse

# 定义消息列表（存放：system、user、assistant 三种提示词）
messages = [
    {
        "role": "system",
        "content": "你是一家名为《黑马程序员》的职业教育培训公司的智能客服，你的名字叫小黑。请以友好、热情的方式回答用户问题。"
    }
]

#2.循环
while True:
    # 3.提示用户输入内容
    user_prompt = input("请输入您要问的问题（bye退出）：")

    if user_prompt == "bye":
        break

    # 将用户的问题追加到 消息列表中
    messages.append(
        {
            "role":"user",
            "content":user_prompt
        }
    )

    # 4.调用ollama
    stream = chat(
        model="qwen2.5:7b",
        messages=messages,
        stream = True
    )
    assistant_prompt  = ""
    #5.打印结果
    for chunk in stream:
        print(chunk["message"]["content"])
        assistant_prompt += chunk["message"]["content"]
    print() #换行
    # 将模型回答的结果追加到 消息列表
    messages.append(
        {
            "role":"assistant",
            "content":assistant_prompt
        }
    )