from flask import Flask

def create_app():
    views = Flask(__name__)
    
    # Importing routes
    from .views import setup_routes
    setup_routes(views)
    
    return views