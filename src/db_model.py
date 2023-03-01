from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

# Configure attribute app connection database with Flask-SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Class Schema for Comment with database Columns
class Comment_Schema(ma.Schema):
    class Meta:
        fields = ('id_comment', 'user_comment', 'datetime_comment', 'title_comment', 'content_comment')

# Class Schema for Response with database Columns
class Response_Schema(ma.Schema):
    class Meta:
        fields = ('id_response', 'user_response', 'datetime_response', 'content_response', 'id_comment')
        
# Instance Class Comment_Schema for one o many rows database        
comment_schema = Comment_Schema()
comments_schema = Comment_Schema(many=True)
        
# Instance Class Response_Schema for one o many rows database        
response_schema = Response_Schema()
responses_schema = Response_Schema(many=True)
