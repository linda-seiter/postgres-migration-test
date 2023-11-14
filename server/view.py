from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import db, User
from schema import UserSchema

blp = Blueprint("Postgres Test", __name__)

@blp.route("/users")
class Users(MethodView):
    
    @blp.response(200, UserSchema(many=True))
    def get(self):
        """List users"""
        return db.session.scalars(db.select(User))