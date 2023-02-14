from datetime import datetime
from db_model import db, app

# Class Comment attributes columns database
class Comment(db.Model):
    id_comment = db.Column(db.Integer, primary_key = True)
    user_comment = db.Column(db.String(30), nullable = False)
    datetime_comment = db.Column(db.DateTime, default = datetime.utcnow)
    title_comment = db.Column(db.String(50), nullable = False)
    content_comment = db.Column(db.String(200), nullable = False)

    # Constructor class Comment
    def __init__(self, user_comment, datetime_comment, title_comment, content_comment):
        self.user_comment = user_comment
        self.datetime_comment = datetime_comment
        self.title_comment = title_comment
        self.content_comment = content_comment

    # class Comment to String format
    def __repr__(self):
        return f"User : {self.user_comment} Datetime : {self.datetime_comment} Title Comment : {self.title_comment} Content Comment : {self.content_comment}"
 
app.app_context().push()    
db.create_all()
