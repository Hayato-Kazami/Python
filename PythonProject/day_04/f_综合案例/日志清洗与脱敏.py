"""
日志清洗与脱敏（进阶题）
原始日志：
"  ERROR | user:张三 | PHONE:13812345678 | addr:CHENGDU-SICHUAN-CHINA  "
输出规范表格并脱敏手机号
"""
log = "  ERROR | user:张三 | PHONE:13812345678 | addr:CHENGDU-SICHUAN-CHINA  "

# 1. 去除两端空白，按 | 分割
parts = log.strip().split("|")

# 2. 提取各字段
level = parts[0].strip()                          # ERROR
username = parts[1].strip().split(":")[1]         # 张三
phone = parts[2].strip().split(":")[1]             # 13812345678
addr_raw = parts[3].strip().split(":")[1]          # CHENGDU-SICHUAN-CHINA

# 3. 脱敏手机号：前3位 + **** + 后4位
phone_hidden = phone[:3] + "****" + phone[-4:]

# 4. 处理地址：按 - 分割，首字母大写其余小写
addr_parts = addr_raw.split("-")
addr_formatted = " ".join([part.capitalize() for part in addr_parts])

# 5. 输出规范格式
print(f"{'Level':<14} {level}")
print(f"{'Username':<14} {username}")
print(f"{'Phone Number':<14} {phone_hidden}")
print(f"{'Address':<14} {addr_formatted}")
