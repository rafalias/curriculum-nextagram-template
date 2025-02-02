from flask_wtf.csrf import CSRFProtect
import peeweedbevolve
import os
import config
from flask import Flask, render_template
from models.base_model import db
from models.user import User
from flask_login import LoginManager

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'instagram_web')

app = Flask('NEXTAGRAM', root_path=web_dir)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

csrf = CSRFProtect(app)

@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

