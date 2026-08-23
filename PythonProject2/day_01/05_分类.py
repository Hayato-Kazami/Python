# 1. 向模型解释什么是我们认为的文本分类
# 2. 约束模型的输出格式
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)
# FewShot准备的例子
class_examples = {
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
    '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势'
}

# 问题列表
sentences = [
    "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
    "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
    "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
    "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会",
    "今天合肥开展了环巢湖自行车比赛，第一名以10小时完赛"
]

# 组装系统提示词
sys_prompt = f"""你是一个金融领域的文本分类专家，需要对输入的句子做分类；
                 分类是：{list(class_examples.keys())}，
                 对于无法分类的文本输出 不知道，或不是金融相关的内容也输出 不知道
"""

# 伪装和AI的聊天记录（FewShot），先提供消息列表的第一个（系统提示词）
messages = [{"role": "system", "content": sys_prompt}]
for k, v in class_examples.items():
    messages.append({"role": "user", "content": v})
    messages.append({"role": "assistant", "content": k})



# 循环处理每一个问题
for question in sentences:

    r = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages = messages + [{"role": "user", "content": question}],
    )

    print("问题：", question)
    print("答案：", r.choices[0].message.content)