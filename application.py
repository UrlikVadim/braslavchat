import json
import logging.config
from fastapi import FastAPI

# Инитим экземпляр приложения
__app = FastAPI()

def get_app():
    global __app
    return __app

# Читаем конфиг
__conf = None
with open('configuration.json', 'r') as f:
    __conf = json.load(f)
    logging.config.dictConfig(__conf["log"])

def get_conf():
    global __conf
    return __conf

