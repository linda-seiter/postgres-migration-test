#!/usr/bin/env python3
from flask import Flask, redirect
from flask_migrate import Migrate
from flask_smorest import Api
import warnings

from models import db
from default_config import DefaultConfig
from view import blp as UserBlueprint

app = Flask(__name__)
app.config.from_object(DefaultConfig)
app.json.compact = False

Migrate(app, db)
db.init_app(app)

# Prevent warnings about nested schemas
with app.app_context():
    warnings.filterwarnings(
            "ignore",
            message="Multiple schemas resolved to the name "
        )

# Create the API
api = Api(app)
api.register_blueprint(UserBlueprint)

@app.route('/')
def index():
    return redirect(app.config["OPENAPI_SWAGGER_UI_PATH"])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
