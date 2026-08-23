import torch
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def sigmoid():
    
    _,axs = plt.subplots(1,2)

    x = torch.linspace(-30, 30, 1000)

    y = torch.sigmoid(x)

    axs[0].plot(x,y)
    axs[0].grid()
    axs[0].set_title('Sigmoid函数')

    x = torch.linspace(-30, 30, 1000, requires_grad=True)
    torch.sigmoid(x).sum().backward()

    axs[1].plot(x.detach(),x.grad)
    axs[1].grid()
    axs[1].set_title('Sigmoid函数的梯度')
    plt.show()

def tanh():
    _,axs = plt.subplots(1,2)

    x = torch.linspace(-30, 30, 1000)

    y = torch.tanh(x)

    axs[0].plot(x,y)
    axs[0].grid()
    axs[0].set_title('Tanh函数')

    x = torch.linspace(-30, 30, 1000, requires_grad=True)
    torch.tanh(x).sum().backward()

    axs[1].plot(x.detach(),x.grad)
    axs[1].grid()
    axs[1].set_title('Tanh函数的梯度')
    plt.show()

def relu():
    _,axs = plt.subplots(1,2)
    
    x = torch.linspace(-30, 30, 1000)

    y = torch.relu(x)

    axs[0].plot(x,y)
    axs[0].grid()
    axs[0].set_title('ReLU函数')    

    x = torch.linspace(-30, 30, 1000, requires_grad=True)
    torch.relu(x).sum().backward()

    axs[1].plot(x.detach(),x.grad)
    axs[1].grid()
    axs[1].set_title('Relu函数的梯度')
    plt.show()

def softmax():
    torch.manual_seed(1)
    # 模拟内部状态值
    x = torch.randint(-5,100,[5]).float().requires_grad=True
    print('x =',x)
    print(x.shape)
    # 计算softmax
    y = torch.softmax(x,dim=-1)
    print('y =',y)

    x1 = torch.randint(-1, 4, [2,5]).float()
    print('x1 =',x1)
    print(x1.shape)
    y1 = torch.softmax(x1,dim=-1)
    print('y1 =',y1)
    
    # 计算softmax的梯度
    y.backward()
if __name__ == '__main__':
    softmax()