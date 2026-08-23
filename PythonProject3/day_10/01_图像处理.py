"""
目标：通过 Python 的 matplotlib 库，直观地理解数字图像的构成，特别是像素值和 RGB 颜色通道的概念。
步骤：
1.像素值的理解
    1.全0为纯黑
    2.全255为全白
2.RGB三通道的理解
    1. 读取图像
    2.分离 R, G, B 三个通道
    3.展示原图像
    4.展示red层
    5.展示green层
    6.展示blue层
"""
import torch
import matplotlib.pyplot as plt

def demo01():
    # 创建一张黑色的图片
    tensor1 = torch.zeros(250,250,3)
    plt.imshow(tensor1)
    plt.show()

    tensor2 = torch.full([250,250,3],255)
    plt.imshow(tensor2)
    plt.show()

def demo02():
    img = plt.imread('./data/img.jpg')
    img_t = torch.tensor(img)
    print(img_t)
    print(img_t.shape)
    
    img_r = img_t[:,:,0]
    print(img_r)
    print(img_r.shape)
    x = torch.zeros_like(img_r)
    print(x)
    print(x.shape)
    # img_r_all = torch.stack([img_r,x,x],dim=-1)
    # print(img_r_all.shape)
    # plt.imshow(img_r_all)
    # plt.show()
    # # green
    # img_g = img_t[:, :, 2]
    # img_g= img_g.float()
    # img_g += 0.1
    # img_g_all = torch.stack([ x, x,img_g], dim=-1)
    # print(img_g_all)
    # print(img_r_all.shape)
    # plt.imshow(img_g_all)
    # plt.show()



if __name__ == '__main__':
    # demo01()
    demo02()


# 1.图像在计算机中 使用的是 [高，宽，通道]来存储的
# 2.放进张量中计算 将他转化成 [通道，高，宽]
# 3.图像的通道一般为3个，分别 r：red   g：green   b：blue
# 4.图像是由像素点组成的，图像内元素的范围是 [0,255],越靠近0的为黑色，越靠近255的是白色
# jpg格式像素点是0-255，png格式范围是0-1