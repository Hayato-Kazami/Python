"""
案例：构建一个简单的命令行交互程序，用户可以通过输入问题与AI模型进行对话。
该程序将使用qwen2.5:7b语言模型。用户可以通过命令行输入问题，程序将调用AI模型生成回答，并将结果输出到终端。
"""
from http.client import responses

from ollama import chat
while True :
    chat_get = input("请输入您的问题：")
    if chat_get == "bye" :
        print("Fk U & Never come back !")
        break
    response = chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "user", "content": chat_get}
            ]
        )
    print(response["message"]["content"])
