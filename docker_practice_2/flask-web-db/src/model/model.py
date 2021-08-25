from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class test_table(db.Model):
    __tablename__ = 'test_table'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    text = db.Column(db.String(20, 'utf8mb4_unicode_ci'))

    def __init__(self, text):
        self.text = text