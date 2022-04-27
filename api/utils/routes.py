from flask import send_file
from api.utils import utils
import os

@utils.route('/get-image/<filename>', methods=['GET', 'POST'])
def get_image(filename: str):
	path_to_project = os.path.split(os.path.abspath(__name__))[0]
	path_to_storage = os.path.join(path_to_project, 'image_storage')
	path_to_image = os.path.join(path_to_storage, filename)

	return send_file(path_to_image)
