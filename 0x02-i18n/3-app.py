#!/usr/bin/env python3
"""
Flask app with template translation support using Flask-Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determine best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render the translated index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
