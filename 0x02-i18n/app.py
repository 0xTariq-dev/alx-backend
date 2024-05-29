#!/usr/bin/env python3
"""Module for basic flask app with babel locale selector"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.before_request
def before_request():
    """Get user before request"""
    user = get_user()
    g.user = user
    g.username = user.get('name') if user else None


@babel.localeselector
def get_locale():
    """Get locale for babel"""
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Get timezone for babel"""
    if request.args.get('timezone'):
        g.timezone = request.args.get('locale')

    if g.user and g.user.get('timezone'):
        g.timezone = g.user.get('timezone')

    try:
        return pytz.timezone(g.timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=['GET'])
def index():
    """Route handler for index page"""
    g.timezone = get_timezone()
    g.time = format_datetime()
    print(g.time)
    return render_template('index.html', username=g.username)


def get_user():
    """Get user dictionary from users"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
