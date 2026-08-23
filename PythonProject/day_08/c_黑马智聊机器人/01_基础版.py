# 导包
import streamlit as st
from ollama import chat


# 标题
st.title("黑马智聊机器人")

# 分割线
st.divider()

# 用户消息输入框
user_prompt = st.chat_input("请输入你的问题")

# 如果用户输入了问题，调用模型处理
if user_prompt:
    # 显示用户容器的内容
    st.chat_message("user").write(user_prompt)
    # 等待思考
    with st.spinner("思考中..."):
        # 调用ollama模型
        response = chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "system",
                    "content": "你是一家名为《黑马程序员》的职业教育培训公司的智能客服，你的名字叫小黑。请以友好、热情的方式回答用户问题。"
                },
                {
                    "role":"user",
                    "content":user_prompt
                }
            ]
        )
        # 将模型输出的内容显示到模型容器中
        st.chat_message("assistant").markdown(response["message"]["content"])