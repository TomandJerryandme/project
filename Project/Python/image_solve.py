# -*- coding: utf-8 -*-

from random import random

import PIL.Image as Image
import os

from numpy import histogram, dot, sqrt, maximum, array, zeros, roll, interp
from numpy.linalg import linalg
from pylab import *
from numpy import *
from scipy.ndimage import filters
from scipy.ndimage import measurements, morphology

def get_imlist(path):
    # 一级文件夹下有用
    # return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    g = os.walk(path)
    image_list = []
    for path, d, filelist in g:
        for filename in filelist:
            if filename.endswith('jpg'):
                image_list.append(os.path.join(path, filename))
    return image_list


def histeq(im, nbr_bins=256):
    """ 对一幅灰度图像进行直方图均衡化"""
    # 计算图像的直方图
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    # cumulative distribution function
    cdf = 255 * cdf / cdf[-1]
    #  归一化
    #  使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


def pca(X):
    """ 主成分分析：    输入：矩阵X ，其中该矩阵中存储训练数据，每一行为一条训练数据
       返回：投影矩阵（按照维度的重要性排序）、方差和均值"""
    # 获取维数
    num_data, dim = X.shape
    # 数据中心化
    mean_X = X.mean(axis=0)
    X = X - mean_X
    if dim < num_data:
        # PCA- 使用紧致技巧
        M = dot(X, X.T)
        # 协方差矩阵
        e, EV = linalg.eigh(M)
        # 特征值和特征向量
        tmp = dot(X.T, EV).T
        # 这就是紧致技巧
        V = tmp[::-1]
        # 由于最后的特征向量是我们所需要的，所以需要将其逆转
        S = sqrt(e)[::-1]
        # 由于特征值是按照递增顺序排列的，所以需要将其逆转
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        # PCA- 使用SVD 方法
        U, S, V = linalg.svd(X)
        V = V[:num_data]
        # 仅仅返回前nun_data 维的数据才合理
        #  返回投影矩阵、方差和均值
    return V, S, mean_X


def denoise(im, U_init, tolerance=0.1, tau=0.125, tv_weight=100):
    """ 使用A. Chambolle（2005）在公式（11）中的计算步骤实现Rudin-Osher-Fatemi（ROF）去噪模型
       输入：含有噪声的输入图像（灰度图像）、U 的初始值、TV 正则项权值、步长、停业条件
        输出：去噪和去除纹理后的图像、纹理残留"""
    m, n = im.shape  # 噪声图像的大小

    #  初始化
    U = U_init
    Px = im  # 对偶域的x 分量
    Py = im  # 对偶域的y 分量
    error = 1
    while (error > tolerance):
        Uold = U

        # 原始变量的梯度
        GradUx = roll(U, -1, axis=1) - U  # 变量U 梯度的x 分量
        GradUy = roll(U, -1, axis=0) - U  # 变量U 梯度的y 分量

        #  更新对偶变量
        PxNew = Px + (tau / tv_weight) * GradUx
        PyNew = Py + (tau / tv_weight) * GradUy
        NormNew = maximum(1, sqrt(PxNew ** 2 + PyNew ** 2))
        Px = PxNew / NormNew  # 更新x 分量（对偶）
        Py = PyNew / NormNew  # 更新y 分量（对偶）
        #  更新原始变量
        RxPx = roll(Px, 1, axis=1)  # 对x 分量进行向右x 轴平移
        RyPy = roll(Py, 1, axis=0)  # 对y 分量进行向右y 轴平移

        DivP = (Px - RxPx) + (Py - RyPy)  # 对偶域的散度
        U = im + tv_weight * DivP  # 更新原始变量

        #  更新误差
        error = linalg.norm(U - Uold) / sqrt(n * m)
    return U, im - U  # 去噪后的图像和纹理残余


image_list = get_imlist("G:\\最后两种\\")

index = 6858
for image_address in image_list:
    index = index + 1
    dealIndex = 0
    for x in range(1, 17):
        image = Image.open(image_address)
        imageArray = array(image)
        dealIndex += 1
        if x == 1:
            # 反相处理
            imageArray = 255 - imageArray
            print("第" + str(index) + "张 反向处理")
        elif x == 2:
            # 将图像像素值变换到100...200 区间
            imageArray = (100.0 / 255) * imageArray + 100
            print("第" + str(index) + "张 像素值变换")
        elif x == 3:
            # 对图像像素值求平方后得到的图像
            imageArray = 255.0 * (imageArray / 255.0) ** 2
            print("第" + str(index) + "张 像素值求平方")
        elif x == 4:
            # 图像旋转
            image = image.rotate(random.randint(0, 360))
            imageArray = array(image)
            print("第" + str(index) + "张 图像旋转")
        elif x == 5:
            # 直方图均衡化
            imageArray, cdf = histeq(imageArray)
            print("第" + str(index) + "张 直方图均衡化")
        elif x == 6:
            # gaussian滤波
            imageArray = filters.gaussian_filter(imageArray, 5)
            print("第" + str(index) + "张 gaussian滤波")
        elif x == 7:
            # Sobel 导数滤波器
            imx = zeros(imageArray.shape)
            filters.sobel(imageArray, 1, imx)
            imy = zeros(imageArray.shape)
            filters.sobel(imageArray, 0, imy)
            magnitude = sqrt(imx ** 2 + imy ** 2)
            imageArray = magnitude
            print("第" + str(index) + "张  Sobel导数滤波器")
        elif x == 8:
            # 噪声
            imageArray = imageArray + 30 * random.standard_normal(imageArray.shape)
            print("第" + str(index) + "张  噪声")
        elif x == 9:
            # 反相处理+像素值变换
            imageArray = 255 - imageArray
            imageArray = (100.0 / 255) * imageArray + 100
            print("第" + str(index) + "张  反相处理+像素值变换")
        elif x == 10:
            # 反相处理+像素值求平方
            imageArray = 255 - imageArray
            imageArray = 255.0 * (imageArray / 255.0) ** 2
            print("第" + str(index) + "张  反相处理+像素值求平方")
        elif x == 11:
            # 像素值求平方+反相处理
            imageArray = 255.0 * (imageArray / 255.0) ** 2
            imageArray = 255 - imageArray
            print("第" + str(index) + "张  像素值求平方+反相处理")
        elif x == 12:
            # 像素值变换+像素值求平方
            imageArray = (100.0 / 255) * imageArray + 100
            imageArray = 255.0 * (imageArray / 255.0) ** 2
            print("第" + str(index) + "张  像素值变换+像素值求平方")
        elif x == 13:
            # 图像旋转+反相
            image = image.rotate(random.randint(0, 360))
            imageArray = array(image)
            imageArray = 255 - imageArray
            print("第" + str(index) + "张  图像旋转+反相")
        elif x == 14:
            # 图像旋转+噪声
            image = image.rotate(random.randint(0, 360))
            imageArray = array(image)
            imageArray = imageArray + 30 * random.standard_normal(imageArray.shape)
            print("第" + str(index) + "张  图像旋转+噪声")
        elif x == 15:
            # 噪声+直方图均衡化
            imageArray = imageArray + 30 * random.standard_normal(imageArray.shape)
            imageArray, cdf = histeq(imageArray)
            print("第" + str(index) + "张  噪声+直方图均衡化")

        imageArray = uint8(imageArray)
        image = Image.fromarray(imageArray)
        image = image.convert('RGB')
        if image_address.rfind("不规则") != -1:
            image.save("G:\\兔屎图片_二次处理\\不规则\\" + str(index) + "_" + str(dealIndex) + ".jpg")
        elif image_address.rfind("大小不一") != -1:
            image.save("G:\\兔屎图片_二次处理\\大小不一\\" + str(index) + "_" + str(dealIndex) + ".jpg")
        elif image_address.rfind("拉稀") != -1:
            image.save("G:\\兔屎图片_二次处理\\拉稀\\" + str(index) + "_" + str(dealIndex) + ".jpg")
        elif image_address.rfind("正常") != -1:
            image.save("G:\\兔屎图片_二次处理\\正常\\" + str(index) + "_" + str(dealIndex) + ".jpg")

        print("完事一个")
