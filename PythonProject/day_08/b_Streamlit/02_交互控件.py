# 导入streamlit库
import streamlit as st
import time

st.header("黑马智聊机器人V3.3")
st.divider()

user_prompt  = st.chat_input('请输入要问的内容：')

if user_prompt :
    st.chat_message("user").write(user_prompt)
    with st.spinner('Thinking...'):
        time.sleep(3)
        st.write('Think Over.')
        st.chat_message("assistant").markdown("# 你真棒~~~")