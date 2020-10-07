import configparser
import json
import os

import base_path
from src.config.config import GlobalVar


class ReadConfig(object):

    def __init__(self, path=None):
        if path:
            config_path = path
        else:
            root_dir = base_path.get_path()
            config_path = os.path.join(root_dir, 'src/config/config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_version(self, param):
        """
        读取测试包版本
        :param param:
        :return:
        """
        return self.cf.get('app-version', param)

    def set_version(self, param, version):
        self.cf.set('app-version', param, version)

    def get_account(self, param):
        """
        读取账号
        :param param:
        :return:
        """
        return self.cf.get('account', param)

    def get_username(self, param):
        """
        读取用户昵称
        :param param:
        :return:
        """
        return self.cf.get('user-name', param)

    def get_country(self, param):
        """
        读取账号GUOJIA
        :param param:
        :return:
        """
        return self.cf.get('country', param)

    def get_eufyhome(self, param):
        """
        读取测试包信息
        :param param:
        :return:
        """
        return self.cf.get('eufyhome', param)

    def get_timezone(self, param):
        """
        读取时区列表名称
        :param param:
        :return:
        """
        return self.cf.get('timezone', param)

    def get_device(self, param):
        """
        读取设备名
        :param param:
        :return:
        """
        return self.cf.get('device-name', param)

    def get_device_udid(self, param):
        """
        读取设备编号
        :param param:
        :return:
        """
        return self.cf.get('device-udid', param)

    def get_faq(self, param):
        """
        读取faq产品名称列表
        :return:
        """
        return self.cf.get('faq-list', param)

    def get_robotic_status(self, param):
        """
        读取扫地机工作状态
        :param param:
        :return:
        """
        return self.cf.get('robotic-status', param)

    def get_phone(self, param):
        """
        读取电话
        :param param:
        :return:
        """
        if GlobalVar.get_platform() == GlobalVar.IOS:
            param = param+'_ios'
        else:
            param = param+'_a'
        return self.cf.get('callus', param)

    def read_json(self, param):
        """
        读取json文件
        :return:
        """
        path = '{}/src/config/helplist.json'.format(base_path.get_path())
        with open(path, 'r') as load_f:
            load_dict = json.load(load_f)
        return load_dict[param]['titles']

    def get_device_type(self, param):
        """
        读取list数据
        :param param:
        :return:
        """
        return eval(self.cf.get('type-list', param))

    def get_bulbs_group(self, param):
        """
        读取分组名称
        :param param:
        :return:
        """
        return self.cf.get('bulbs-group', param)

    def get_week_by_id(self, param):
        """
        获取week名称
        :param param:
        :return:
        """
        return self.cf.get('id-week', param)

    def get_wifi(self, param):
        """
        获取week名称
        :param param:
        :return:
        """
        return eval(self.cf.get('test-wifi', param))

    def get_area_util(self, param):
        """
        面积单位
        :param param:
        :return:
        """
        return self.cf.get('area-util', param)


data = ReadConfig()

if __name__ == '__main__':
    print(data.get_version('ios'))
    data.set_version('ios', 'gywejhbs')
    print(data.get_version('ios'))
