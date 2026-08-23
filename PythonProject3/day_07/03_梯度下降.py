import torch

def gradient_descent():

    w = torch.tensor(100.,requires_grad=True)

    for i in range(1000):

        # 前向传播，计算损失
        loss = 2 * w ** 2 + 3 * w + 4

        #梯度清零
        if w.grad is not None:
            w.grad.zero_()

        # 反向传播，计算梯度
        loss.backward()

        # 更新参数
        w.data -= 0.01 * w.grad

        print(f'第{i}次迭代，w的值为：{w.item()}，损失为：{loss.item()}')

if __name__ == '__main__':
    gradient_descent()