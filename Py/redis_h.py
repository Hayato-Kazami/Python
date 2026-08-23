import pymysql
import redis

class MySqlService:

    def __init__(self, 
                 host="localhost", 
                 port=3306, 
                 user="root", 
                 password="123456", 
                 database="my_db", 
                 charset="utf8"):
        self.conn = pymysql.connect(host=host, port=port, 
                                    user=user, password=password, 
                                    database=database, charset=charset)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()        
        self.conn.close()

    def get_data(self, user_name):
        sql = "SELECT * FROM userinfo WHERE name = %s"
        self.cursor.execute(sql, [user_name])
        data = self.cursor.fetchall()
        print(f"获取的数据: {data}")  # 打印获取的数据以调试
        return data

class RedisService:

    TTL_DEFAULT = 20

    def __init__(self, ms: MySqlService, 
                 host="localhost", 
                 port=6379, 
                 password=None,
                 db=0):
        self.ms = ms
        self.conn = redis.Redis(host=host, port=port, 
                                db=db, password=password,
                                decode_responses=True)

    def __del__(self):
        self.conn.close()

    def __ttl_reset(self, key, ttl_time=TTL_DEFAULT):
        self.conn.expire(key, ttl_time)

    def __save_data(self, key, value):
        
        for item in value:
            msg = ",".join(map(str, item))  # 使用 join 方法更简洁地生成字符串
            self.conn.rpush(key, msg)
    
        self.conn.expire(key, RedisService.TTL_DEFAULT)

    def get_data(self, user_name):
        data = None

        if self.conn.exists(user_name):
            print("Redis中存在数据")
            self.__ttl_reset(user_name)
            data = self.conn.lrange(user_name, 0, -1)
            return data
        
        print("Redis中不存在数据")

        value = self.ms.get_data(user_name)
        print(f"从MySQL获取的数据: {value}")

        if value:
            print("MySQL中存在数据")
            print(f"查询用户{user_name}的数据,redis中不存在,从MySQL中获取数据,共{len(value)}条记录")
            self.__save_data(user_name, value)
            print(f"数据保存到Redis中,key为:{user_name}")
            data = value  # 确保 data 变量被正确赋值

        else:
            print("MySQL中不存在数据")
            
        return data

if __name__ == "__main__":
    ms = MySqlService()
    rs = RedisService(ms)
    r = rs.get_data("用户003")
    print(r)
