import requests
import time
start = time.time()
url = "http://127.0.0.1:8000/predict"

data = {'text': "中国人民公安大学2012年硕士研究生目录及书目"}
res = requests.post(url, json=data)
print(res.json())
print(time.time() - start,"s")