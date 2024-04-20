# configuration files for flask application

# importing necessary modules
import os

# defining app base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# defining db URI
SQLALCHEMY_DATABASE_URI = 'postgresql://paulet:paulet@localhost/task_manager_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False