
import pymysql
import random


# ============================================================
# 1. 建库建表语句
SQL_CREATE_DATABASE = """
CREATE DATABASE IF NOT EXISTS kaoshi
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;
"""

SQL_CREATE_TABLE = """
USE kaoshi;

CREATE TABLE IF NOT EXISTS student (
    id      INT             NOT NULL,
    name    VARCHAR(50)     NOT NULL,
    age     INT             DEFAULT NULL,
    addr    VARCHAR(200)    DEFAULT NULL,
    height  FLOAT           DEFAULT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uk_id (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# ============================================================
# 2. 插入数据（2条SQL语句）
# 第一条SQL: 插入1条数据
SQL_INSERT_ONE = """
INSERT INTO student (id, name, age, addr, height)
VALUES (1, '张三', 20, '北京市海淀区', 175.5);
"""

# 第二条SQL: 插入2条数据
SQL_INSERT_TWO = """
INSERT INTO student (id, name, age, addr, height)
VALUES
    (2, '李四', 22, '上海市浦东新区', 168.0),
    (3, '王五', 21, '广州市天河区', 180.2);
"""


# ============================================================
# 3.向表中插入100条数据（id 100 ~ 199）
def random_name():
    """生成随机中文姓名"""
    surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈',
                '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许']
    names = ['伟', '芳', '娜', '敏', '静', '丽', '强', '磊', '洋', '勇',
             '艳', '杰', '娟', '涛', '明', '超', '秀英', '华', '慧', '鑫']
    return random.choice(surnames) + random.choice(names)


def random_addr():
    """生成随机地址"""
    cities = ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '南京',
              '西安', '重庆', '长沙', '青岛', '大连', '厦门', '苏州']
    districts = ['A区', 'B区', 'C区', 'D区', 'E区']
    return random.choice(cities) + '市' + random.choice(districts)


def insert_100_students():
    """向student表插入100条数据，id从100到199"""
    # 数据库连接配置
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'kaoshi',
        'charset': 'utf8',
    }

    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = "INSERT INTO student (id, name, age, addr, height) VALUES (%s, %s, %s, %s, %s)"

    inserted = 0
    for i in range(100, 200):  # id: 100 ~ 199，共100条
        name = random_name()
        age = random.randint(18, 30)
        addr = random_addr()
        height = round(random.uniform(155.0, 190.0), 1)

        try:
            cursor.execute(sql, (i, name, age, addr, height))
            inserted += 1
        except pymysql.err.IntegrityError:
            print(f"id={i} 已存在，跳过")

    conn.commit()
    print(f"成功插入 {inserted} 条数据")
    cursor.close()
    conn.close()



