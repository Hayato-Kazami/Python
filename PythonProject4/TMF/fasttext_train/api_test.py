import requests
import time
url = 'http://127.0.0.1:8000/predict'

data = {'text':"《赤壁OL》攻城战诸侯战硝烟又起"}


start = time.time()
res = requests.post(url, json=data)
use_time =( time.time() - start)*1000
print(f'预测结果:{res.json()["pred_class"]}, 耗时:{use_time}ms')


# 压力测试 模型的性能 测试模型qps和耗时

