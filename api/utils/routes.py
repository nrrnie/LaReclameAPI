from flask import request, send_file
from api.utils import utils
import os

@utils.route('/get-image/<filename>', methods=['POST'])
def get_image(filename: str):
	path_to_project = os.path.abspath(__name__)
	path_to_storage = '\\images\\'

	return send_file(path_to_project + path_to_storage + filename)