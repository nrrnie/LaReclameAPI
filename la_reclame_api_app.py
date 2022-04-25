from api import create_app, db
from flask_migrate import Migrate

from api.models import Users
from api.models import Items

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5001)
