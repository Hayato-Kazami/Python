"""
实现一个基础ReAct范式智能体（天气查询小助手）
"""
import datetime
from openai import OpenAI
import os
import random

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

def call_model(sys_prompt, user_prompt, model_name="qwen3.7-plus"):
    r = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return r.choices[0].message.content

# 天气查询小助手，是需要一些基础工具支持的，避免用户问题信息太少，这些工具辅助模型获得更多信息
def get_user_location():
    """获取用户所在位置"""
    return random.choices(['合肥', '杭州', '深圳', '广州'])

def get_today():
    """获取今日日期"""
    return datetime.date.today()

def get_weather(date, city):
    """获取天气"""
    return f"{date}，{city}，天气良好，气温26℃，多云转晴，湿度55%，AQI 22"

# 解析模型输出，提取思考过程、动作名称和动作参数或最终输出结果
def parse_model_output(output: str):
    """
    Thought:已知城市、日期和天气信息，可以整合结果回复用户
    Action:Final
    Info:明天2026-05-01日，合肥天气良好，气温舒适26℃，湿度舒服，适合户外活动
    """
    thought = ""
    action = ""
    info = ""

    lines = output.strip().split("\n")

    for line in lines:
        line = line.strip()         # 清理每一行前后的空格和回车等无效内容

        # 字符串.startswith(字符串) 判断字符串是否是某个字符串开头，是返回True
        if line.startswith("Thought:"):
            thought = line.replace("Thought:", "").strip()
        elif line.startswith("Action:"):
            action = line.replace("Action:", "").strip()
        else:
            info = line.replace("Info:", "").strip()

    return thought, action, info

def react(question):
    print(f"用户提问：{question}")

    context = []      # 记录中间每一次工具调用的结果

    for i in range(1, 6):       # 最多循环5次
        print(f"第{i}轮迭代开始，当前注入上下文信息：[{context}]")

        sys_prompt = f"""
        你是一个遵循ReAct范式的Agent智能代理，必须严格按照以下格式输出：
        Thought:<你的思考过程>
        Action:<只能从[get_user_location, get_today, get_weather]中选择，或在确定答案后填写Final>
        Info:<如果Action是动作名称，则填写改动作工具所需的参数；如果Action是Final，则填写最终输出结果>
        
        当前上下文信息：
        {str(context)}
        
        【工具说明】
        - get_user_location
        作用：获取用户所在地理位置
        传入参数：无
        返回结果：城市名称字符串，如合肥
        
        - get_today
        作用：获取今天日期
        传入参数：无
        返回结果：日期字符串，如2001-01-01
        
        - get_weather
        作用：获取指定城市指定日期的天气信息
        传入参数：
            - date，字符串，指定的日期
            - city，字符串，指定的城市
        返回结果：指定城市指定日期的天气字符串信息，如：晴天29度，湿度70%
        
        【正确示例】
        - 示例1（调用工具）
        Thought:要回答明天天气情况，我需要先知道今天是哪一天
        Action:get_today
        Info:
        
        - 示例2（调用工具）
        Thought:要获取2026-05-01日，合肥天气，我需要查询天气信息
        Action:get_weather
        Info:('2026-05-01', '合肥')
        
        - 示例3（输出最终答案）
        Thought:已知城市、日期和天气信息，可以整合结果回复用户
        Action:Final
        Info:明天2026-05-01日，合肥天气良好，气温舒适26℃，湿度舒服，适合户外活动
        
        用户提问，参考下文。
        """

        # 调用模型
        model_result = call_model(sys_prompt, question)
        # 解析结果
        thought, action, info = parse_model_output(model_result)

        print(f"解析Thought：", thought)
        print(f"解析Action：", action)
        print(f"解析Info：", info)

        if action == "Final":       # 最终回复
            print("模型最终回复：", info)
            return

        # 此处可以升级（如果有200个工具，请问要写200个if吗？）
        if action == "get_user_location":
            action_result = get_user_location()
            context.append(f"调用函数get_user_location，获取结果：{action_result}")
        if action == "get_today":
            action_result = get_today()
            context.append(f"调用函数get_today，获取结果：{action_result}")
        if action == "get_weather":
            args: tuple = eval(info)
            action_result = get_weather(*args)
            context.append(f"调用函数get_weather，获取结果：{action_result}")

        print(f"第{i}轮迭代结束\n\n")


if __name__ == '__main__':
    react("今天的天气怎么样？")