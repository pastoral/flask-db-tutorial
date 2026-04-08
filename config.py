####  Database URI & settings ####
import os

class Config:
    """Base configuration — shared across all environments."""
    SECRET_KEY = os.environ.get("SECRET_KEY","dev_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables a signal system we don't need

class DevelopmentConfig(Config):
    """SQLite — perfect for local development, no setup needed."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
    
class ProductionConfig(Config):
    """MySQL — for when you deploy to a real server."""
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://username:password@localhost:3306/task_manager_db'
    )
    
    """🔍 Code Breakdown
'sqlite:///tasks.db' — three slashes means "relative path". SQLite creates a file called tasks.db in your project folder. No server needed!
'mysql+pymysql://...' — the format is dialect+driver://user:password@host:port/database. Replace with your real credentials.
SQLALCHEMY_TRACK_MODIFICATIONS = False — suppresses a deprecation warning. Always set this.
Subclassing Config lets you switch between SQLite in dev and MySQL in prod just by changing one line.
    """