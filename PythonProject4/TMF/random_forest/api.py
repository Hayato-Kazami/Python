from rf_predict_fun import predict
from flask import Flask, request

# 实例化Flask对象
app = Flask(__name__)

# 定义路由和处理函数
@app.route('/predict', methods=['POST'])
def predict_api():
    # 获取请求数据
    try:
        data = request.get_json()
        # 调用预测函数
        result = predict(data)
        # 返回预测结果
        return result, 200
    except Exception as e:
        # 处理异常
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
    