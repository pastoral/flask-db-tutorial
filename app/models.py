### Database table definitions###
"""
This is the heart of your database design. 
Every attribute decorated with db.Column(...) becomes a column in the tasks table. 
SQLAlchemy handles the SQL CREATE TABLE statement automatically.
"""
from app import db
from datetime import datetime

class Task(db.Model):
    """Represents one row in the tasks table."""
 
    # Integer primary key — auto-increments for each new row
    id = db.Column(db.Integer, primary_key=True)
    
    # Task title — required (nullable=False), max 120 chars
    title = db.Column(db.String(120), nullable = False)
    
    # Optional description
    description = db.Column(db.Text, nullable=True)

    # Is the task done? Defaults to False
    is_done = db.Column(db.Boolean, default=False, nullable=False)

    # Priority: 'low', 'medium', or 'high'
    priority = db.Column(db.String(10), default='medium')

    # Automatically set when the task is created
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        # Makes debugging easier — readable output in the console
        return f'<Task {self.id}: {self.title}>'
    
    
    '''
        When you call db.create_all(), SQLAlchemy reads your model classes 
        and creates the matching SQL tables automatically. You never have to 
        write CREATE TABLE yourself!
    '''
    
    '''
        Here is what each column type does:
        •	db.Integer — stores whole numbers; used for IDs and counts
        •	db.String(n) — stores text up to n characters; use for short fields
        •	db.Text — stores unlimited-length text; ideal for descriptions
        •	db.Boolean — stores True or False; perfect for done/not-done flags
        •	db.DateTime — stores date and time; default=datetime.utcnow runs at insert time

        ✓	db.create_all() reads all your Model classes and creates 
        matching SQL tables.  You never write CREATE TABLE manually. 
        SQLAlchemy also skips tables that already exist.

    '''
    
    

    