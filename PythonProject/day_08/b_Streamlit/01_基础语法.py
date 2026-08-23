# 导入streamlit库
import streamlit as st

# 文本与标题
st.title("一级标题")
st.header("二级标题")
st.subheader("三级标题")
st.write("普通文本，支持 **加粗**、*斜体*、列表：[你好,2,5,8]")
# 分割线
st.divider()

# markdown语法格式
"## markdown语法格式"

"""
1. 有序列表
2. 有序列表
"""

"""
- 无序列表
- 无序列表
"""

"`print('行内代码')`"

"""
```python
def hello():
    print('代码块')
```
"""
st.divider()