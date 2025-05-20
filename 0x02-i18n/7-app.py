#!/usr/bin/env python3
"""
Flask app with time zone selection based on user, request, or default
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import timezone, UnknownTimeZoneError


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
    """Store user in flask.g before each request"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user = g.get('user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the correct timezone"""
    tz_param = request.args.get('timezone')
    try:
        if tz_param:
            return timezone(tz_param).zone
    except UnknownTimeZoneError:
        pass

    user = g.get('user', None)
    try:
        if user:
            return timezone(user.get('timezone')).zone
    except (UnknownTimeZoneError, TypeError):
        pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """Render translated index page with user info"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
