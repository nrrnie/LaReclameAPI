from api.users import users
from api.models import Users

@users.route('/user_by_id/<user_id>', methods=['POST'])
def user_by_id(user_id: int):
	user = Users.query.get(user_id)

	if user is None:
		return {
			'status': 'error',
			'error': 'User with such ID is not found.'
		}

	return {
		'status': 'ok',
		'user': user.get_json()
	}

@users.route('/user_by_username/<user_name>', methods=['POST'])
def user_by_username(user_name: str):
	user = Users.query.filter_by(username=user_name).first()
	
	if user is None:
		return {
			'status': 'error',
			'error': 'User with such username is not found.'
		}

	return {
		'status': 'ok',
		'user': user.get_json()
	}

@users.route('/user_by_email/<user_email>', methods=['POST'])
def user_by_email(user_email: str):
	user = Users.query.filter_by(email=user_email).first()

	if user is None:
		return {
			'status': 'error',
			'error': 'User with such email is not found.'
		}

	return {
		'status': 'ok',
		'user': user.get_json()
	}