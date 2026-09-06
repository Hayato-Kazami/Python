import streamlit as st
import requests
import time

# ================= 页面配置 =================
st.set_page_config(
    page_title="投满分 · 新闻标题分类系统",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================= 全局样式 =================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@400;500;600&display=swap');

/* 主容器：暗色底 + 霓虹网格背景 */
[data-testid="stAppViewContainer"] {
    background-color: #070b14;
    background-image:
        linear-gradient(rgba(0, 240, 255, 0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 240, 255, 0.06) 1px, transparent 1px),
        radial-gradient(ellipse at 20% 0%, rgba(0, 240, 255, 0.12) 0%, transparent 45%),
        radial-gradient(ellipse at 80% 100%, rgba(124, 92, 255, 0.12) 0%, transparent 45%);
    background-size: 44px 44px, 44px 44px, 100% 100%, 100% 100%;
}

/* 侧边栏 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220 0%, #0a0e18 100%);
    border-right: 1px solid rgba(0, 240, 255, 0.18);
}

/* 主标题 */
.neon-title {
    font-family: 'Orbitron', 'Segoe UI', sans-serif;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: 4px;
    text-transform: uppercase;
    background: linear-gradient(90deg, #00f0ff 0%, #7c5cff 50%, #00ff9d 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 30px rgba(0, 240, 255, 0.35);
    margin-bottom: 4px;
}
.neon-subtitle {
    font-family: 'Rajdhani', 'Segoe UI', sans-serif;
    color: #7ee6ff;
    letter-spacing: 6px;
    font-size: 15px;
    text-transform: uppercase;
    opacity: 0.85;
}

/* 面板卡片 */
.panel {
    background: rgba(13, 22, 40, 0.72);
    border: 1px solid rgba(0, 240, 255, 0.25);
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 0 18px rgba(0, 240, 255, 0.08), inset 0 0 24px rgba(0, 240, 255, 0.03);
    backdrop-filter: blur(6px);
}
.panel-label {
    font-family: 'Orbitron', 'Segoe UI', sans-serif;
    color: #00f0ff;
    letter-spacing: 3px;
    font-size: 13px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

/* 输入框（终端风格） */
[data-testid="stTextArea"] textarea {
    background: rgba(4, 10, 20, 0.9) !important;
    color: #9ffce0 !important;
    border: 1px solid rgba(0, 240, 255, 0.4) !important;
    border-radius: 10px !important;
    font-family: 'Consolas', 'Courier New', monospace !important;
    font-size: 15px !important;
    box-shadow: inset 0 0 12px rgba(0, 240, 255, 0.08) !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #00ff9d !important;
    box-shadow: 0 0 16px rgba(0, 255, 157, 0.35), inset 0 0 12px rgba(0, 240, 255, 0.08) !important;
}

/* 预测按钮 */
[data-testid="stButton"] > button {
    font-family: 'Orbitron', 'Segoe UI', sans-serif;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00f0ff;
    background: rgba(0, 240, 255, 0.06);
    border: 1px solid #00f0ff;
    border-radius: 10px;
    padding: 10px 28px;
    box-shadow: 0 0 12px rgba(0, 240, 255, 0.25);
    transition: all 0.25s ease;
}
[data-testid="stButton"] > button:hover {
    color: #04121a;
    background: #00f0ff;
    border-color: #00f0ff;
    box-shadow: 0 0 28px rgba(0, 240, 255, 0.7);
    transform: translateY(-1px);
}

/* 结果卡片 */
.result-card {
    background: rgba(13, 22, 40, 0.8);
    border: 1px solid rgba(0, 255, 157, 0.5);
    border-radius: 14px;
    padding: 26px 28px;
    box-shadow: 0 0 26px rgba(0, 255, 157, 0.25);
    animation: pulse-glow 2s ease-in-out infinite;
}
.result-class {
    font-family: 'Orbitron', 'Segoe UI', sans-serif;
    font-size: 40px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #00ff9d;
    text-shadow: 0 0 24px rgba(0, 255, 157, 0.8);
}
.error-card {
    background: rgba(30, 10, 20, 0.8);
    border: 1px solid rgba(255, 77, 109, 0.55);
    border-radius: 14px;
    padding: 20px 24px;
    box-shadow: 0 0 22px rgba(255, 77, 109, 0.25);
}
.error-text {
    font-family: 'Consolas', monospace;
    color: #ff7d96;
    font-size: 15px;
}

/* 侧边栏信息行 */
.sys-key {
    font-family: 'Rajdhani', sans-serif;
    color: #6fa8c9;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.sys-val {
    font-family: 'Consolas', monospace;
    color: #00f0ff;
    font-size: 14px;
}

@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(0, 255, 157, 0.2); }
    50% { box-shadow: 0 0 34px rgba(0, 255, 157, 0.45); }
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

# ================= 侧边栏：系统信息 =================
with st.sidebar:
    st.markdown(
        '<div class="panel-label">⚙ SYSTEM INFO</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="panel">
            <div class="sys-key">模型引擎</div>
            <div class="sys-val">Random Forest + TF-IDF</div>
            <br>
            <div class="sys-key">推理端点</div>
            <div class="sys-val">127.0.0.1:8000/predict</div>
            <br>
            <div class="sys-key">前端框架</div>
            <div class="sys-val">Streamlit</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div style="margin-top:18px;font-family:Consolas,monospace;color:#4c5a6b;font-size:12px;">'
        '>> 确保后端 API 已在 8000 端口运行<br>'
        '>> 输入标题 → 点击「开始预测」</div>',
        unsafe_allow_html=True,
    )

# ================= 主标题 =================
st.markdown(
    '<div class="neon-title">投满分 · 新闻标题分类</div>'
    '<div class="neon-subtitle">Neural News Classification Terminal</div>',
    unsafe_allow_html=True,
)
st.markdown("<br>", unsafe_allow_html=True)

# ================= 输入区 =================
st.markdown('<div class="panel-label">▸ INPUT</div>', unsafe_allow_html=True)
text_input = st.text_area(
    "输入标题",
    "中国人民公安大学2012年硕士研究生目录及书目",
    height=90,
    label_visibility="collapsed",
)

st.markdown("<br>", unsafe_allow_html=True)

col_btn, col_tip = st.columns([1, 3])
with col_btn:
    do_predict = st.button("⚡ 开始预测", use_container_width=True)
with col_tip:
    st.markdown(
        '<div style="font-family:Consolas,monospace;color:#4c5a6b;font-size:13px;padding-top:14px;">'
        '>>> 等待推理结果…</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ================= 结果区 =================
st.markdown('<div class="panel-label">▸ OUTPUT</div>', unsafe_allow_html=True)

if do_predict:
    data = {"text": text_input}
    url = "http://127.0.0.1:8000/predict"

    with st.spinner("正在进行模型推理…"):
        try:
            start = time.time()
            response = requests.post(url, json=data)
            elapsed_ms = (time.time() - start) * 1000

            if response.status_code == 200:
                result = response.json()
                pred_class = result["pred_class"]
                st.markdown(
                    f"""
                    <div class="result-card">
                        <div class="panel-label">✓ 分类结果</div>
                        <div class="result-class">{pred_class}</div>
                        <div style="font-family:Consolas,monospace;color:#6fa8c9;font-size:13px;margin-top:12px;">
                            输入标题：{data['text']}<br>
                            推理耗时：{elapsed_ms:.2f} ms
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                err = response.json().get("error", "未知错误")
                st.markdown(
                    f"""
                    <div class="error-card">
                        <div class="panel-label">✗ 请求失败</div>
                        <div class="error-text">{err}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        except Exception as e:
            st.markdown(
                f"""
                <div class="error-card">
                    <div class="panel-label">✗ 连接异常</div>
                    <div class="error-text">{str(e)}</div>
                    <div style="font-family:Consolas,monospace;color:#ff9db1;font-size:12px;margin-top:8px;">
                        请确认后端 API 已在 127.0.0.1:8000 运行
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
