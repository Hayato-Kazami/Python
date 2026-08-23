# 1. 向模型解释什么是我们认为的文本匹配
# 2. 约束模型的输出格式
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# 例子
examples = {
    '是': [
        ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
        ('公司发布新课程新学科，投资者利好，营收大涨', '公司业务发展蒸蒸日上'),
    ],
    '不是': [
        ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
        ('央行降息，刺激经济增长。', '新能源技术的创新。')
    ]
}

# 问题
sentence_pairs = [
    ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
    ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
    ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
]

sys_prompt = f"你专注于文本语义匹配，我将给你2个句子，你判断2个句子是否匹配，回答是或不是。"
messages = [{"role": "system", "content": sys_prompt}]
for k, v in examples.items():
    for t in v:
        messages.append({"role": "user", "content": f"句子1：{t[0]}，句子2：{t[1]}"})
        messages.append({"role": "assistant", "content": k})

for t in sentence_pairs:
    r = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages + [{"role": "user", "content": f"句子1：{t[0]}，句子2：{t[1]}"}]
    )
    print("问题：", t)
    print("回答：", r.choices[0].message.content)