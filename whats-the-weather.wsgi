import sys
sys.path.insert(0, '/var/www/whats-the-weather/')

activate_this = '/root/.local/share/virtualenvs/whats-the-weather-MQ_X0hKL'
with open(activate_this) as file_:
    exec(file.read(), dict(__file__=activate_this))
    
from __init__.py import app as application
