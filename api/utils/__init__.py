from flask import Blueprint

utils = Blueprint('/utils',__name__)

from api.utils import routes