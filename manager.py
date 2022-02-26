import logging
import application

class Manager:

    def __init__(self, config:"dict", log_name: "str") -> None:
        self.conf = config
        self.log = logging.getLogger(log_name)
        self.log.debug("Manager inited")
    
    def get_user(self):
        pass

__manager = Manager(application.get_conf(), "chat")

def get_manager():
    global __manager
    return __manager

