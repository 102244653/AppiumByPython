# -*- coding:utf-8 -*-
import os
import subprocess

import base_path
import argparse
from ftplib import FTP


pf = ''
ftp_ip = "10.1.54.233"
ftp_username = "ftpadmin"
ftp_pwd = "123456"
ftp_android_path = "/09_CI-APP/Appliance/eufyhome_android/"  # FTP目录
ftp_ios_path = "/09_CI-APP/Appliance/eufyhome_ios/"  # FTP目录
dst_file_path = '{}/apppackage/'.format(base_path.get_path())  # 本地目录


def get_app_version(sn):
    if pf == 'ios':
        p = subprocess.Popen("ideviceinstaller -u {} -l | grep EufyHome".format(sn), shell=True,
                             stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        app_version = str(out).replace('"', '').split(',')[1]
    if pf == 'android':
        p = subprocess.Popen('adb -s {} shell dumpsys package com.eufylife.smarthome'.format(sn), shell=True,
                             stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        for line in out.splitlines():
            info = line.decode("utf-8")
            if 'versionName' in info:
                app_version = str(info).split('=')[1]
                break
    return app_version


def read_local_app_version():
    file_list = os.listdir(dst_file_path)
    for _file in file_list:
        if pf == 'ios' and '.ipa' in _file:
            return str(_file)
        if pf == 'android' and '.apk' in _file:
            return str(_file)
    print('本地暂无' + pf + '安装包，直接下载')
    return 'none'


def download_app(version):
    ftp = FTP()
    ftp.set_debuglevel(1)  # 不开启调试模式
    ftp.connect(host=ftp_ip)  # 连接ftp
    ftp.login(ftp_username, ftp_pwd)  # 登录ftp
    ftp.set_pasv(False)  ##ftp有主动 被动模式 需要调整
    buffer_size = 102400  # 默认是8192
    print(ftp.getwelcome())  # 显示登录ftp信息
    ftp_path = ''
    if pf == 'ios':
        ftp_path = ftp_ios_path
    if pf == 'android':
        ftp_path = ftp_android_path
    print('查看安装包文件夹：'+ftp_path)
    file_list = ftp.nlst(ftp_path)
    if len(file_list) == 0:
        print('ftp暂无'+pf+'安装包，请先上传！')
        return ''
    for _file in file_list:
        print('ftp版本：'+str(_file))
        file_name = _file.split('/')[-1]
        if version == 'none' or version not in file_name:
            ftp_file = os.path.join(ftp_path, _file)
            write_file = dst_file_path + file_name
            if version != 'none':
                os.remove(dst_file_path + version)
            with open(write_file, "wb") as f:
                ftp.retrbinary('RETR %s' % ftp_file, f.write, buffer_size)
        else:
            write_file = ''
    ftp.quit()
    print('下载安装包路径：'+write_file)
    return write_file


def install_app(sn):
    '''
    安装包到手机
    :param file_name:
    :return:
    '''
    app_path = ''
    file_list = os.listdir(dst_file_path)
    for _file in file_list:
        if '.ipa' in _file:
            ios_path = dst_file_path+_file.split('/')[-1]
        if '.apk' in _file:
            android_path = dst_file_path+_file.split('/')[-1]
    if pf == 'android':
        print('安装包版本：'+android_path)
        p = subprocess.Popen('adb -s {} install -r {}'.format(sn, android_path), shell=True,
                             stdout=subprocess.PIPE)
        # p.wait(timeout=120)
        out, err = p.communicate()
        print('@@@@@@@@安装结果：'+str(out)+'@@@@@@@@')
    if pf == 'ios':
        print('安装包版本：' + ios)
        p = subprocess.Popen('ideviceinstaller -u {} -i {}'.format(sn, ios_path), shell=True,
                             stdout=subprocess.PIPE)
        # p.wait(timeout=120)
        out, err = p.communicate()
        print('@@@@@@@@安装结果：'+str(out)+'@@@@@@@@')


def view_connect_device():
    if pf == 'ios':
        print('检查已连接的ios设备')
        p = subprocess.Popen("idevice_id -l", shell=True, stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        print('已连接的ios设备uuid：\n'+str(out))
    if pf == 'android':
        print('检查已连接的android设备')
        p = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
        p.wait()
        out, err = p.communicate()
        print('已连接的android设备uuid：\n'+str(out))


if __name__ == '__main__':
    # 执行命令
    # python check_app_version.py --android='android=1tiygwqhsbam' --ios='ios=32tyuqgjhambcxz'
    parser = argparse.ArgumentParser(description='设备平台及设备sn')
    parser.add_argument("--udid", type=str, default="")  # FA6980308124
    args = parser.parse_args()
    info = args.udid.split('&')
    android = info[0]
    ios = info[1]
    new_apk = ''
    new_ipa = ''
    print('                                              ')
    print('##############################################')
    print('——————————开始检查更新android设备APP版本——————————')
    print('##############################################')
    pf = android.split('=')[0]
    sn = android.split('=')[1]

    view_connect_device()
    print('当前操作的设备uuid：'+sn)
    android_app_version = read_local_app_version()
    print('android设备当前APP版本：'+android_app_version)

    print('开始检查ftp安装包')
    apk_path = download_app(android_app_version)

    if apk_path != '':
        print('android设备开始更新APP')
        install_app(sn)
        print('android设备APP更新完毕！')
        new_apk = apk_path.split('/')[-1]
    else:
        print('android设备APP暂无更新')
        new_apk = android_app_version

    print('                                           ')
    print('###########################################')
    print('——————————开始检查更新ios设备APP版本——————————')
    print('###########################################')
    pf = ios.split('=')[0]
    sn = ios.split('=')[1]
    view_connect_device()
    print('当前操作的设备uuid：'+sn)
    ios_app_version = read_local_app_version()
    print('ios设备当前APP版本：' + ios_app_version)

    print('开始检查ftp安装包')
    apk_path = download_app(ios_app_version)
    print('待安装：'+apk_path)
    if apk_path != '':
        print('ios设备开始更新APP')
        install_app(sn)
        print('ios设备APP更新完毕！')
        new_ipa = apk_path.split('/')[-1]
    else:
        print('ios设备APP暂无更新')
        new_ipa = ios_app_version
    with open('{}/version.txt'.format(base_path.get_path()), 'w') as f:
        f.write('android='+new_apk+'\n')
        f.write('ios='+new_ipa)


