import numpy as np

import cv2
import random
import socket

import os
import subprocess

'''
其他非appium方法
'''


def create_port(host, start, end):
    '''
    创建空闲的端口号
    :param host:
    :param start:
    :param end:
    :return:
    '''
    while True:
        num = random.randint(start, end)
        s = socket.socket()
        s.settimeout(0.5)
        try:
            if s.connect_ex((host, num)) != 0:
                return num
        finally:
            s.close()


def uninstall_uiautomator2_server():
    '''
    android only
    卸载uiautomator2.server
    :return:
    '''
    server = 'io.appium.uiautomator2.server'
    test = 'io.appium.uiautomator2.server.test'
    p = os.popen("adb shell pm list packages")
    out = p.read()
    if test in out:
        os.system("adb uninstall {}".format(test))
    if server in out:
        os.system("adb uninstall {}".format(server))


def get_iphone_name(sn):
    '''
    iphone手机的名字
    :param sn:
    :return:
    '''
    name = None
    p = subprocess.Popen("idevicename -u {}".format(sn), shell=True, stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()
    for line in out.splitlines():
        info = line.decode("utf-8")
        if info is not None and info != '':
            name = info
    return name


def get_iphone_version(sn):
    '''
    获取iphone手机系统版本号
    :param sn:
    :return:
    '''
    p = subprocess.Popen("ideviceinfo -u {} -k ProductVersion".format(sn),
                         shell=True, stdout=subprocess.PIPE)
    p.wait()
    out, err = p.communicate()
    for line in out.splitlines():
        info = line.decode("utf-8")
        return info


def cmpHash(hash1, hash2):
    # Hash值对比
    # 算法中1和0顺序组合起来的即是图片的指纹hash。顺序不固定，但是比较的时候必须是相同的顺序。
    # 对比两幅图的指纹，计算汉明距离，即两个64位的hash值有多少是不一样的，不同的位数越小，图片越相似
    # 汉明距离：一组二进制数据变成另一组数据所需要的步骤，可以衡量两图的差异，汉明距离越小，则相似度越高。汉明距离为0，即两张图片完全一样
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


def pHash(img):
    # 感知哈希算法
    # 通过imread方法直接读取物理路径
    img = cv2.imread(img)
    # 缩放32*32
    img = cv2.resize(img, (32, 32))  # , interpolation=cv2.INTER_CUBIC

    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct = cv2.dct(np.float32(gray))
    # opencv实现的掩码操作
    dct_roi = dct[0:8, 0:8]

    hash = []
    avreage = np.mean(dct_roi)
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i, j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash


