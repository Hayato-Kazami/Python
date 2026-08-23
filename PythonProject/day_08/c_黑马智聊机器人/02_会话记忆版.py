# 导包
import streamlit as st
from ollama import chat
from streamlit import session_state

if "message" not in st.session_state:
    st.session_state["message"] = [
        {
            "role":"system",
            "content":"你是一家名为《黑马程序员》的职业教育培训公司的智能客服，你的名字叫小黑。请以友好、热情的方式回答用户问题。"
        }
    ]
# 标题
st.title("黑马智聊机器人")

# 分割线
st.divider()

# 用户消息输入框
user_prompt = st.chat_input("请输入你的问题")

# 如果用户输入了问题，调用模型处理
if user_prompt:
    # 将用户提问的内容，添加到消息列表中
    session_state["message"].append({"role":"user","content":user_prompt})

    for message in session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])
    # 流式调用ollama模型
    with st.chat_message("assistant"):
        # 创建占位符，用于逐步更新流式输出内容
        placeholder = st.empty()
        full_response = ""
        # 调用ollama模型（开启流式输出）
        stream = chat(
            model="qwen2.5:7b",
            messages=session_state["message"],
            stream=True
        )
        # 逐块接收并实时显示
        for chunk in stream:
            full_response += chunk["message"]["content"]
            placeholder.markdown(full_response)
    # 将完整的回复内容添加到消息列表，保持会话记忆
    session_state["message"].append({"role":"assistant","content":full_response})
