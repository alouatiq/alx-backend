#!/usr/bin/env python3
"""
Flask app with mocked login and user-specific message display
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_user() -> dict | None:
    """Retrieve user dictionary based on login_as param"""
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Store user in global flask.g before each request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match locale or use locale URL parameter"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render translated index page with user info"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
