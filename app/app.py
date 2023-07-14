from flask import Flask
from app import config

from app.controllers import (
    matrix,
    financial_statements,
    user_manager,
    auth
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(matrix.bp)
    app.register_blueprint(financial_statements.bp)
    app.register_blueprint(user_manager.bp)
    app.register_blueprint(auth.bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
