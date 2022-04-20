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

