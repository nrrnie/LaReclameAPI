from flask import request

from api.items import items
from api.models import Items
from api import db

@items.route('/add/item', methods=['POST'])
def create_item():
	username = request.form.get('username')
	title = request.form.get('title')
	body = request.form.get('body')

	if None in [username, title, body]:
		return {
			'status': 'error',
			'error': 'Not all data was given.'
		}

	item = Items(author_username=username, title=title, body=body)
	db.session.add(item)
	db.session.commit()
	
	return {
		'status': 'ok'
	}

@items.route('/item_by_id/<item_id>', methods=['POST'])
def item_by_id(item_id: int):
	item = Items.query.get(item_id)

	if item is None:
		return {
			'status': 'error',
			'error': 'Item with such ID is not found.'
		}

	return {
		'status': 'ok',
		'item': item.get_json()
	}

@items.route('/items_by_username/<item_username>', methods=['POST'])
def items_by_username(item_username: str):
	itemList = Items.query.filter_by(author_username=item_username).all()

	if itemList is None:
		return {
			'status': 'error',
			'error': 'Items with such author username are not found.'
		}

	items = [item.get_json() for item in itemList]

	return {
		'status': 'ok',
		'items': items
	}


@items.route('/items_by_title/<item_title>', methods=['POST'])
def items_by_title(item_title: str):
	itemList = Items.query.filter(Items.title.like('%' + item_title + '%')).all()

	if itemList is None:
		return {
			'status': 'error',
			'error': 'Items with such title are not found.'
		}

	items = [item.get_json() for item in itemList]

	return {
		'status': 'ok',
		'items': items
	}

@items.route('/items_by_status/<item_status>', methods=['POST'])
def items_by_status(item_status: bool):
	itemList = Items.query.filter_by(is_active=item_status).all()

	if itemList is None:
		return {
			'status': 'error',
			'error': 'Items with such status are not found.'
		}

	items = [item.get_json() for item in itemList]

	return {
		'status': 'ok',
		'items': items
	}