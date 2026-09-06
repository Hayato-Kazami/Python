import sys
from pathlib import Path

# 把 TMF 项目根目录加入 sys.path，使 `from data.config import Config` 在任何目录下运行都能导入
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pre_data.config import Config
from rf_predict_fun import predict
from fastapi import FastAPI, Request
import uvicorn

# 创建FastAPI应用实例
app1 = FastAPI()

# 定义路由
@app1.post("/predict")
async def predict_api(request: Request):
    try:
        print("接收到请求", request)
        data = await request.json()
        print("接收到的数据", data)
        result = predict(data)
        print("预测结果", result)
        return result
    except Exception as e:
        print("处理异常", e)
        return {"error": str(e)},400

if __name__ == "__main__":
    uvicorn.run(app1, host="0.0.0.0", port=8000)