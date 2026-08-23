import torch

def forward():
    x = torch.tensor(10, requires_grad=True,dtype=torch.float32)

    y = 2 * x ** 2 + 3 * x + 4

    print("y = ", y)

    y.backward()

    print("dy/dx = ", x.grad)

def forward1():
    x = torch.tensor([10,20], requires_grad=True,dtype=torch.float32)

    y = 2 * x ** 2 + 3 * x + 4

    print("y = ", y)

    y.sum().backward()

    print("dy/dx = ", x.grad)


if __name__ == "__main__":
    forward()
    forward1()