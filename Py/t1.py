import pymysql
import redis


class MySQLService:

    def __init__(self,
                 host="localhost",
                 port=3306,
                 user="root",
                 password="123456",
                 database="my_db",
                 charset="utf8"
                 ):
        # MySQL连接对象
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)
        # 游标对象用来干活
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_userinfo(self, username):
        sql = "SELECT * FROM userinfo WHERE name = %s"
        self.cursor.execute(sql, [username])

        return self.cursor.fetchall()


class RedisService:
    # 类属性
    TTL_TIME_DEFAULT_SECOND = 30

    def __init__(self,
                 ms: MySQLService,
                 host="localhost",
                 port=6379,
                 password=None,
                 db=0):
        self.conn = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True,
        )

        self.ms = ms

    def __del__(self):
        self.conn.close()

    def __ttl_reset(self, key, ttl_time=TTL_TIME_DEFAULT_SECOND):
        self.conn.expire(key, ttl_time)

    def __save_userinfo(self, key, infos):
        # key -> 周杰轮
        # infos -> ((1,周杰轮,11), (2,周杰轮,22))
        # 存入redis是： 周杰轮 -> ["1,周杰伦,11", "2,周杰伦,22"]
        for info in infos:
            # 每个info 就是1个元组，即(2,周杰轮,22)，转成字符串存入
            msg = ""
            for i in info:
                msg += f"{str(i)},"

            msg = msg[:-1]      # 从头到-1（不含-1），丢弃最后一个字符,
            self.conn.rpush(key, msg)

        # 设置Key的TTL
        self.conn.expire(key, RedisService.TTL_TIME_DEFAULT_SECOND)

    def get_userinfo(self, username):
        # 是否在redis中有
        if self.conn.exists(username):      # 1 True 0 False
            # 缓存有
            print(f"查询{username}，redis缓存命中")

            # 重设TTL
            self.__ttl_reset(username)

            # 从redis中取出信息  # 存入redis是： 周杰轮 -> ["1,周杰伦,11", "2,周杰伦,22"]
            return self.conn.lrange(username, 0, -1)    # ["1,周杰伦,11", "2,周杰伦,22"]

        # redis中没有，查mysql
        print(f"查询{username}，redis缓存未命中，跳转MySQL查询")

        infos = self.ms.get_userinfo(username)

        if infos:       # 查到了
            print(f"查询{username}，redis缓存未命中，跳转MySQL查询，查询到{len(infos)}条记录")
            self.__save_userinfo(username, infos)
            print(f"保存信息{infos}到redis中，key为：{username}")
        else:
            print(f"查询{username}，redis缓存未命中，跳转MySQL查询，也没查到，无此用户")

        return infos        # 要么是元组套元组（有数据） 要么空元组（没数据）


if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)

    r = rs.get_userinfo("用户003")
    print(r)