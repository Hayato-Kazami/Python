class singer:
    """歌手类"""

    def __init__(self, song_name, singer_name):
        """初始化：歌曲名、歌手名字"""
        self.song_name = song_name      # 歌曲名
        self.singer_name = singer_name  # 歌手名字

    def fans(self):
        """打印粉丝打call信息"""
        print(f"{self.singer_name}歌手的{self.song_name}歌曲持续打榜，粉丝为喜欢的歌手打call")


# ============================================================
# 类外功能：
# 1) 逐行读取singer.txt，创建对象并存入列表
# 2) 遍历列表，调用fans()方法
if __name__ == '__main__':
    singer_list = []

    # 1) 读取文件，创建歌手对象
    with open('singer.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # 跳过空行
            # 格式：歌曲名，歌手名（中文逗号分隔）
            song_name, singer_name = line.split('，')
            singer_obj = singer(song_name, singer_name)
            singer_list.append(singer_obj)

    # 2) 遍历列表，调用fans()方法
    for obj in singer_list:
        obj.fans()
