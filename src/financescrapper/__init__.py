# app/__init__.py

import logging
from flask import Flask

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO) 
# logger.addHandler(console_handler)

def create_app():
    app = Flask(__name__)
    app.json.ensure_ascii = False
    
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
