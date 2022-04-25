from flask import Blueprint

items = Blueprint('/items', __name__)

from api.items import routes