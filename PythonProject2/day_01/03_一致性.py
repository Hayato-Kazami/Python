from openai import OpenAI
import os

way_num = 3

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ws-6nv3se8envhqisdk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

def call_model(sys_prompt, user_prompt, model_name="deepseek-v4-flash"):
    r = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return r.choices[0].message.content


question = """
小橡皮3元，大橡皮4.5元，大橡皮的使用寿命是小橡皮的2倍，
大橡皮占用空间是小橡皮的3.6倍，我有105元，
怎么组合购买橡皮可以最大化兼容使用时长和空间占用的最优；"""

# 步骤1，给思路
step1_sys = f"""
你是一个数学家，请用{way_num}种方法来推理问题，只给出推理思路不需要解答；
思路需要符合数学家核算逻辑，简洁明了，合理有效；
输出格式为：["思路1", "思路2", ..., "思路n", ...]
"""
#
solution_str: str = call_model(step1_sys, question)
# 将结果字符串转为list，eval可以将字符串作为代码执行
solution_list = eval(solution_str)
print("【step1】多个思路：", solution_list)


# 步骤2，让每个思路都得到结果
result_list = []        # 记录不同思路的结果
for solution in solution_list:
    step2_sys = f"你是一个数学教授，请用如下思路解决购买问题，只输出答案即可\n思路是：{solution}。问题参考下文"
    # 可以直接写成
    result_list.append(call_model(step2_sys, question))

print("【step2】多个思路的结果：", result_list)

# 步骤3，投票多个思路的结果
step3_sys = f"""
你是一个公平的投票专家，能够根据用户输入的list格式的多个答案进行投票，哪个答案正确你就返回哪个答案的结果，
只返回答案本身即可，无需额外内容
如果多个答案都不满意，则回复无结果；

用户输入的多个答案是：{result_list}，产生此答案的问题原文，请参考下文"""
result3 = call_model(step3_sys, question)
print("【step3】", result3)