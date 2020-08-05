"""
This script runs the FoamToolTracker2020 application using a development server.
"""


from os import environ
#from FoamToolTracker2020 import app
from ProjectTracker import create_app

app = create_app

if __name__ == '__main__':
    
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    
    app(HOST, PORT)