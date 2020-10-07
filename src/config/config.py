'''
用于保存全局的变量
'''

from distutils.util import strtobool


class GlobalVar:
    PLATFORM = None
    FIRMWARE_NAME = None
    IOS = "ios"
    ANDROID = "android"
    TEST_FLAG = True
    REMOVE_ADD = 0
    RP_LOGGER = None

    @staticmethod
    def set_platform(platform):
        GlobalVar.PLATFORM = platform

    @staticmethod
    def get_platform():
        return GlobalVar.PLATFORM

    @staticmethod
    def set_firmware_name(firmware_name):
        GlobalVar.FIRMWARE_NAME = firmware_name

    @staticmethod
    def get_firmware_name():
        return GlobalVar.FIRMWARE_NAME

    @staticmethod
    def get_test_flag():
        return GlobalVar.TEST_FLAG

    @staticmethod
    def set_test_flag(test_flag):
        if test_flag == 'f':
            GlobalVar.TEST_FLAG = False
        elif test_flag == 't':
            GlobalVar.TEST_FLAG = True

    @staticmethod
    def set_add_remove(remove_add):
        GlobalVar.REMOVE_ADD = strtobool(remove_add.lower())

    @staticmethod
    def get_remove_add():
        return GlobalVar.REMOVE_ADD

    @staticmethod
    def set_rp_logger(rp_logger):
        GlobalVar.RP_LOGGER = rp_logger

    @staticmethod
    def get_rp_logger():
        return GlobalVar.RP_LOGGER
