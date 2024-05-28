#!/usr/bin/env python3
"""Module for basic flask app configuration"""


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    TIMEZONE = "UTC"
