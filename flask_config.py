"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    MEMBER_ID = os.environ.get('MEMBER_ID')
    if not MEMBER_ID:
        raise ValueError("No TRELLO_TOKEN set for Flask application.")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run setup.sh?")
    TRELLO_API_KEY = os.environ.get('TRELLO_KEY')
    if not TRELLO_API_KEY:
        raise ValueError("No TRELLO API KEY set for Flask application.")
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    if not TRELLO_TOKEN:
        raise ValueError("No TRELLO_TOKEN set for Flask application.")
