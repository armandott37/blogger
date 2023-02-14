from datetime import datetime
from db_model import db, app
from comment import Comment

# Class Response attributes columns database
class Response(db.Model):
    id_response = db.Column(db.Integer, primary_key = True)
    user_response = db.Column(db.String(30), nullable = False)
    datetime_response = db.Column(db.DateTime, default = datetime.utcnow)    
    content_response = db.Column(db.String(200), nullable = False)
    id_comment = db.Column(db.Integer, db.ForeignKey('comment.id_comment'), nullable = False)

    # Constructor class Response
    def __init__(self, user_response, datetime_response, content_response, id_comment):
        self.user_response = user_response
        self.datetime_response = datetime_response        
        self.content_response = content_response
        self.id_comment = id_comment

    # class Response to String format
    def __repr__(self):
        return f"User : {self.user_response} Datetime : {self.datetime_response} Content Response : {self.content_response}"
 
app.app_context().push()    
db.create_all()
