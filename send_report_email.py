#!/usr/bin/python3
# -*- coding:utf-8 -*-
import argparse
import csv
import os
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header
import base_path


# 第三方 SMTP 服务
mail_host = "smtp.gmail.com"  #设置服务器
mail_user = "vega.lai@anker.com"    #用户名

sender = 'vega.lai@anker.com'
receivers = ['fei.xiong@anker.com', 'nica.li@anker.com', 'vega.lai@anker.com']
cc_mail = []
# receivers = ['kinwa.li@anker.com', 'fei.xiong@anker.com', 'nica.li@anker.com', 'vega.lai@anker.com', 'christina.yi@anker.com']  # 接收邮件
# cc_mail = ['homer.zhu@anker.com', 'jacky.xie@anker.com', 'sammy.yang@anker.com', 'lynne.xie@anker.com']  # 抄送
dst_file_path = '{}/apppackage/'.format(base_path.get_path())  # 本地目录
path = '{}/suites.csv'.format(base_path.get_path())

# 报告的html  <a href="http://10.1.54.233:8890/appliance/${platfrom}/${build_time}/index.html">${platfrom}测试报告</a>
mail_msg ='''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>接口测试报告</title>
        <style type="text/css">
            html,body,table,thead,tbody,tr,th,td,caption {
                margin: 0;
                padding: 0;
            }
            /**
             * "主体色调：anker品牌蓝(色号#0D2285，RGB-0:22:137)、黑色、白色
             * 字体型号：默认Arial
             * 字体大小：10
             * 字体颜色：默认黑色
             * 文字处理：默认上下居中
             */
            body {
                line-height: 20px;
                font-size: 16px;
                font-family: "Arial";
                color: #000;
            }
            table {
                width: 90%;
                margin: 20px auto 15px 30px;
                border-collapse: collapse;
                box-sizing: border-box;
            }
            table caption {
                margin-bottom: 10px;
                font-size: 20px;
                text-align: left;
            }
            table td,
            table th {
                padding: 5px;
            }
            /**
             * Title
             * 底色anker品牌主题色
             * 文字处理：白色、加粗、左右居中
             */
            table th {
                /*background:#91c5d4;*/
                font-weight: bold;
                color: #fff;
                text-align: center;
                background: #0D2285;
                border: 1px solid #000;
            }
            thead th:first-child {
                border-left-color: #0D2285;
            }
            thead th:last-child {
                border-right-color: #0D2285;
            }
            /*color设置字体颜色，background设置底色*/
            table th.red {
                color: #f00;
                background: #ff0;
            }
            table th.green {
                background: #008000;
            }
            thead th[colspan],
            thead th[rowspan] {
                /*background:#66a9bd;*/
            }
            tfoot th {
                color: #000;
                text-align: left;
                background: #fff;
                /*background:#91c5d4;*/
            }
            tbody {
                box-sizing: border-box;
            }
            tbody td {
                /*background: #d5eaf0;*/
                border: 1px solid #000;
            }
        </style>
    </head>
    '''


def get_all_fps(all_num, fail_num, err_data, build_time, platfrom, version):
    """
    解析测试数据
    :param all_num:
    :param fail_num:
    :param err_data:
    :param build_time:
    :param platfrom:
    :param version:
    :return:
    """
    suc_num = all_num - fail_num
    testALlCase = str(all_num)
    testSucCase = str(suc_num)
    testFailCase = str(fail_num)

    SENDTIME = datetime.now().strftime('%Y-%m-%d %H:%M')
    report_address = f"http://10.1.54.233:8890/appliance/{platfrom}/{build_time}/index.html"

    # 计算百分比啊
    try:
        testVal = "%.2f%%" % ((suc_num * 100) / float(all_num))
        need_val = float(format(float(suc_num) * 100 / float(all_num), '.2f'))
    except ZeroDivisionError as e:
        testVal = "0%"
        need_val = 0.00

    content1Val = ''
    content1 = f'''<body>
            <p style="color: rgb(34, 34, 34); font-family: Arial, Helvetica, sans-serif; font-size: small; white-space: normal; background-color: rgb(255, 255, 255);">
                <span style="font-size: 13px;">Hi ALL:<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EufyHome-{platfrom} UI测试报告如下所示， 本次测试共执行{testALlCase}用例，执行失败用例{testFailCase}。【本结果已筛除标记skip的用例】<br/>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;测试详情：</span><a href="{report_address}" target="_blank" style="color: rgb(17, 85, 204); font-size: 13px;">{report_address}</a>
                <br/>
            </p>
            <table width="0">
                <colgroup>
                    <col width="173"/>
                    <col width="173"/>
                    <col width="173"/>
                    <col width="386"/>
                </colgroup>
                <tbody>
                    <tr style="height:27px;" class="firstRow">
                        <td style="border-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(0, 22, 137); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; color: rgb(255, 255, 255); text-align: center;" rowspan="1" colspan="4">
                            EufyHome-{platfrom}测试报告
                        </td>
                    </tr>
                    <tr style="height:27px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            测试环境
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {platfrom}
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            测试版本
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {version}
                        </td>
                    </tr>
                    <tr style="height:25px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            执行用例总数
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {testALlCase}
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            执行时间
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {SENDTIME}
                        </td>
                    </tr>
                    <tr style="height:26px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(0, 22, 137); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; color: rgb(255, 255, 255); text-align: center;" rowspan="1" colspan="4">
                            版本测试统计
                        </td>
                    </tr>
                    <tr style="height:25px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            测试项总数
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            成功项
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            失败项
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            成功率
                        </td>
                    </tr>
                    <tr style="height:25px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {testALlCase}
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {testSucCase}
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                            {testFailCase}
                        </td>'''

    if need_val < 99.00:
        content1Val = f'''<td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                        <font color="red"><b>{testVal}</b></font>
                    </td>
                </tr>
                '''
    else:
        content1Val = f'''<td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; white-space: normal; overflow-wrap: break-word; text-align: center;">
                                    {testVal}
                                </td>
                            </tr>
                            '''

    #get fail mshg
    contentTitle2= f'''
                    <tr style="height:26px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(0, 22, 137); font-family: Arial; font-weight: bold; white-space: normal; overflow-wrap: break-word; color: rgb(255, 255, 255); text-align: center;" rowspan="1" colspan="4">
                            错误用例详细信息
                        </td>
                    </tr>
                    <tr style="height:25px;">
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            用例名称
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            用例Code
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            成功/失败
                        </td>
                        <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(207, 226, 243); white-space: normal; overflow-wrap: break-word; text-align: center;">
                            步骤描述
                        </td>
                    </tr>
                    '''
    content2=''
    if len(err_data) == 0:

        content2 = f'''
                <tr style="height:24px;">
                    <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                    NA
                    </td>
                    <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                    NA
                    </td>
                    <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                    NA
                    </td>
                    <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                    NA
                    </td>
                </tr>'''
    else:

        for sceneData in err_data:
            api_name = sceneData[0]
            api_utime = sceneData[1]
            api_result = sceneData[2]
            api_secne = sceneData[3]

            content2 = content2+f'''
                            <tr style="height:24px;">
                                <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                                {api_name}
                                </td>
                                <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                                {api_utime}
                                </td>
                                <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); 
                text-align: center;">
                                <font color="red"><b>{api_result}</b></font>
                                </td>
                                <td style="border-right-color: rgb(102, 102, 102); border-bottom-color: rgb(102, 102, 102); border-left-color: rgb(102, 102, 102); overflow: hidden; padding: 2px 3px; vertical-align: middle; background-color: rgb(255, 255, 255); font-family: Arial; overflow-wrap: break-word;">
                                    {api_secne}
                                </td>
                            </tr>'''

    contentEnd = f'''
        </tbody>
    </table>
    <p>
        <br/>
    </p>
            </body>
    </html>
    '''

    html = mail_msg+content1+content1Val+contentTitle2+content2+contentEnd
    return html


def get_result_data():
    """
    解析文件结果的数据
    :param path: suit.csv文件解读
    :return:
    """
    err_data = []
    all_num = 0

    with open(path) as file:
        f_csv = csv.reader(file)
        for row in f_csv:
            if row[0] == 'skipped':
                continue

            all_num = all_num + 1

            if row[0] in ['failed', 'broken']:
                case_status = row[0]
                case_name = row[1]
                # 提取有效部分，并且去除前后空格
                descrp = row[3].split(':return:', 1)[0].strip()
                test_descrp_arr = descrp.split('\n', 1)
                testcase_name = test_descrp_arr[0]
                case_step = ''
                if len(test_descrp_arr) > 1:
                    case_step = test_descrp_arr[1].strip().split(':param')[0]
                err_data.append((testcase_name, case_name, case_status, case_step))

    fail_num = len(err_data)
    return all_num, fail_num, err_data


def read_local_app_version(pf):
    version = 'none'
    with open('{}/version.txt'.format(base_path.get_path())) as f:
        for line in f:
            if pf in line.strip():
                version = line.strip().split('=')[1]
                break
    return version


def send_email(platfrom, now_date, mail_pass):
    all_num, fail_num, err_data = get_result_data()
    version = read_local_app_version(platfrom)
    html = get_all_fps(all_num, fail_num, err_data, now_date, platfrom, version)
    message = MIMEText(html, 'html', 'utf-8')
    message['From'] = Header("EufyHome 自动化", 'utf-8')
    message['To'] = ', '.join(receivers)
    message['Cc'] = ', '.join(cc_mail)

    subject = 'EufyHome【'+platfrom+'】自动化测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    send_result = '200'
    try:
        client = smtplib.SMTP(mail_host, 587)
        client.starttls()
        client.login(mail_user, mail_pass)
        client.sendmail(sender, receivers+cc_mail, message.as_string())
        client.quit()
        print("邮件发送成功")
    except Exception as e:
        send_result = '500'
        print("邮件发送失败:\n "+str(e))
    return send_result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='设备平台及报告文件夹')
    parser.add_argument("--report", type=str, default="ios=000000")  # FA6980308124
    parser.add_argument("--password", type=str, default="rsfihyhecbygxbll")
    args = parser.parse_args()
    ps = args.password
    info = args.report.split('=')
    pf = info[0]
    nowdate = info[1]
    print('平台：'+pf+',日期：'+nowdate)
    send_flag = True
    i = 1
    while send_flag and i < 4:
        res = send_email(pf, nowdate, ps)
        if res == '200':
            send_flag = False
        else:
            time.sleep(60)
        i += 1
