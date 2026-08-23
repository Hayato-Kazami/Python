"""
案例：构建一个简单的命令行交互程序，用户可以通过输入问题与AI模型进行对话。
该程序将使用qwen2.5:7b语言模型。用户可以通过命令行输入问题，程序将调用AI模型生成回答，并将结果输出到终端。
"""
# 1.导包
from ollama import chat

# 2. 循环
while True:
    # 3. 用户输入提示词
    user_prompt = input("请输入您的问题（bye退出）：")

    if user_prompt == "bye":
        break

    # 4.调用ollama发送请求
    response = chat(model="qwen2.5:7b", messages=[{"role": "system",
                                                   "content": "你是一家名为《黑马程序员》的职业教育培训公司的智能客服，你的名字叫小黑。请以友好、热情的方式回答用户问题。"},
                                                  {"role": "user", "content": user_prompt}])

    # 5.打印结果
    print(response["message"]["content"])