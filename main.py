from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from extensions import db, migrate
from app.models.product import Products
from app.routes.product import product


def create_app():
    app = Flask(__name__)
    CORS(app, resource={
        r"/*": {
            "origins": "*"
        }
    })

    load_dotenv()
    db_host = os.getenv("DB_HOST")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    dbname = os.getenv("DB_NAME")

    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{username}:{password}@{db_host}/{dbname}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product, url_prefix='/api/v1')

    return app


api = create_app()
if __name__ == "__main__":
    api.run()