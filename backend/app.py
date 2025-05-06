from flask import Flask
from flask_cors import CORS
from models import db
from routes import api

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/payd.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
