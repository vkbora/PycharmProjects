import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\vkbora\\PycharmProjects\\nopcommerceApp\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
