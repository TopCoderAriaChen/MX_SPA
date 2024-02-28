import logging
import os

from flask import Flask
from pythonjsonlogger import jsonlogger 

def config_log(app: Flask):
    log_path = os.path.join(app.root_path, "logs")
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    file_handler = logging.FileHandler(f"{log_path}/default.log")
    json_formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(module)s %(message)s"
    )
    file_handler.setFormatter(json_formatter) 
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)
    return app
