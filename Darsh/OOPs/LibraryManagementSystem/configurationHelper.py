import json


class Configuration:
    def __init__(self):
        self.__config = None  # readonly variable
        self.name = "Darsh"

    @property
    def config(self):
        if self.__config is None:
            self.load_config()
        return self.__config

    def load_config(self):
        with open("appsettings.json", 'r') as config_file: 
            self.__config = json.load(config_file)


__config__ = Configuration()
