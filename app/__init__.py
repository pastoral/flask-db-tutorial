##### App factory — creates the Flask app ####
'''
    The App Factory pattern creates your Flask app inside a function 
    rather than at module level. This makes the app easier to test and configure. 
    Notice that db = SQLAlchemy() is created without an app — it gets bound to the app 
    later via db.init_app(app). This is the recommended pattern for larger projects.
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

# Create the db instance OUTSIDE the factory
# so models can import it without circular imports
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Bind SQLAlchemy to this Flask app
    db.init_app(app)
    
    # Import and register routes
    from app.routes import main
    app.register_blueprint(main) #    # Register blueprints (our route groups)#
    
    """
    🗺️ What is a Blueprint?
    Think of your Flask app as a large restaurant. 
    You wouldn't have one single chef handling appetizers, main courses, and desserts 
    all at once. You'd organize the kitchen into stations — each with its own chef, 
    tools, and responsibilities.A Blueprint is exactly that — a way to organize your 
    Flask app into modular, reusable sections. 
    Each blueprint handles its own routes, errors, and logic, and is later "registered"
    onto the main app.
    A Blueprint is a recipe for a section of your app. It doesn't work on its own — 
    it needs to be registered onto a Flask app to come alive.
    """
    
    
    # Create all tables if they don't exist
    with app.app_context:
        db.create_all()
        
    return app



'''
    🔍 Code Breakdown
db = SQLAlchemy() — creates the database extension. We create it outside so models 
     can import db without causing circular import errors.
db.init_app(app) — links the db instance to this specific Flask app.
db.create_all() — reads your model classes and creates database tables automatically. 
                  You never write CREATE TABLE SQL!
app_context() — SQLAlchemy needs Flask's app context to know which database to 
              connect to.
'''
