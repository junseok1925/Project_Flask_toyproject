from flask import Flask, render_template, request, jsonify
from flask import Blueprint


def create_app():
    app = Flask(__name__)

    from views import index, login, artist

    app.register_blueprint(index.bp)

    app.register_blueprint(login.bp)

    app.register_blueprint(artist.bp)

    

    return app

app = create_app()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)