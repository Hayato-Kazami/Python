from cozepy import COZE_CN_BASE_URL, Coze, Message, TokenAuth, ChatEventType, ChatEvent

# 关键信息
# Coze API KEY
coze_api_token = r"pat_cRg4HlG3Z2Nq18tKythlKslTmTxe7vox7M4d06A36EAWzdKGvXqaaN21st8OBOc0"
# 智能体 bot id
bot_id = "7665539709375987712"
# 用户标识符（随意填）
user_id = "xiaocao"

# 1. TCP链接，创建Coze类对象
coze = Coze(
    auth=TokenAuth(coze_api_token),         # 授权，选择TokenAuth（token授权）类对象
    base_url=COZE_CN_BASE_URL,              # 选择BASE URL，即指向国内版Coze
)

# 2. 准备和机器人聊天的消息
messages = [
    Message.build_user_question_text("帮我规划明天合肥去杭州3天旅游行程")
]

# 3. 发起会话
stream = coze.chat.stream(
    bot_id = bot_id,                    # 你要和哪个机器人聊天
    user_id = user_id,                  # 用户ID
    additional_messages=messages,       # 添加消息
)

# 4. for循环流式对象（生成器）
for event in stream:
    # event表示事件
    # event.event 3个类型：
    # 1. CONVERSATION_MESSAGE_DELTA 表示AI正在回复中
    # 2. CONVERSATION_CHAT_COMPLETED 表示AI回复完成
    # 3. CONVERSATION_CHAT_FAILED 表示AI回复失败
    #
    # event.message.content是正式回复内容
    # event.message.reasoning_content是思考过程
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        if event.message.content:
            print(event.message.content, end="")
        elif event.message.reasoning_content:
            print(event.message.reasoning_content, end="")
    elif event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
        print("AI回复完成")
        break
    elif event.event == ChatEventType.CONVERSATION_CHAT_FAILED:
        print("AI回复失败")
        break