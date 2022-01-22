import abc

class CacheMeta(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send_message(self, id_group:int, message:str):
        pass

    @abc.abstractmethod
    def get_message(self, id_group:int):
        pass

    @abc.abstractmethod
    def set_user_data(self, id_user:int):
        pass

    @abc.abstractmethod
    def get_user_data(self, id_user:int):
        pass