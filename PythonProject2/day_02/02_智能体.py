from pathlib import Path
from cozepy import COZE_CN_BASE_URL,Coze,Message,TokenAuth,MessageObjectString,ChatEventType

coze_api_token = r"pat_cRg4HlG3Z2Nq18tKythlKslTmTxe7vox7M4d06A36EAWzdKGvXqaaN21st8OBOc0"
bot_id = "7665539709375987712"
user_id = "Red"

coze = Coze(
    auth=TokenAuth(coze_api_token),
    base_url=COZE_CN_BASE_URL,
    
)

upload_response = coze.files.upload(
    file=Path(r"D:\2026_智能体\02Coze智能体平台\02物料\刘大锤-简历.pdf")
)

if not upload_response:     # 如果是None上传失败
    print("文件上传失败")
    exit(0)         # 停止Python程序，传入0表示正常停止，非0表示异常

file_id = upload_response.id

messages = [
    Message.build_user_question_objects([
        MessageObjectString.build_file(file_id=file_id),
        MessageObjectString.build_text("帮我评估简历"),
    ])
]

stream = coze.chat.stream(
    bot_id=bot_id,
    user_id=user_id,
    additional_messages=messages
)

Path("report").mkdir(parents=True, exist_ok=True)
report_file = open("report/resume.md", "w", encoding="utf-8")

counter = 0
for event in stream:

    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        if event.message.content:
            print(event.message.content, end="")
            report_file.write(event.message.content)
        elif event.message.reasoning_content:
            if counter == 100:
                counter = 0
                print()
            print(".", end="")
            counter += 1

    elif event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
        print("AI回复完成")
        break
    elif event.event == ChatEventType.CONVERSATION_CHAT_FAILED:
        print("AI回复失败")
        break


report_file.close()