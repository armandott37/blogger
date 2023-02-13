from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Configure attribute app connection database with Flask-SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@127.0.0.1:23306/db_blogger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

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
# Create database schema with class Comment
db.create_all()

# Class Schema with database Columns
class Comment_Schema(ma.Schema):
    class Meta:
        fields = ('id_comment', 'user_comment', 'datetime_comment', 'title_comment', 'content_comment')
        
# Instance Class Comment_Schema for one o many rows database        
comment_schema = Comment_Schema()
comments_schema = Comment_Schema(many=True)

# Function API REST POST create new comment database
@app.route('/comment_POST', methods=['POST'])
def create_comment():
    print(request.json)
    params = request.json    
    comment = Comment(params['user_comment'], datetime.now(), params['title_comment'], params['content_comment'])
    db.session.add(comment)
    db.session.commit()
    return comment_schema.jsonify(comment)

# Function API REST GET obtain all comments from database
@app.route('/comments_GET', methods=['GET'])
def get_comments():    
    comments = Comment.query.all()
    print(comments)    
    return comments_schema.jsonify(comments)

# Function API REST GET obtain comment from database with id parameter
@app.route('/comment_GET/<int:id_comment>', methods=['GET'])
def get_comment(id_comment):
    comment = Comment.query.filter_by(id_comment = id_comment).first()
    return comment_schema.jsonify(comment)

# Function API REST PUT modified comment from database with id parameter
@app.route('/comment_PUT/<int:id_comment>', methods=['PUT'])
def put_comment(id_comment):
    comment = Comment.query.filter_by(id_comment = id_comment).first()
    params = request.json
    comment.user_comment = params['user_comment']
    comment.datetime_comment = datetime.now()
    comment.title_comment = params['title_comment']
    comment.content_comment = params['content_comment']
    db.session.commit()
    print(comment)
    return comment_schema.jsonify(comment)

# Function API REST DELETE delete comment from database with id parameter
@app.route('/comment_DEL/<int:id_comment>', methods=['DELETE'])
def delete_comment(id_comment):
    comment = Comment.query.filter_by(id_comment = id_comment).first()
    db.session.delete(comment)
    db.session.commit()
    print(comment)
    return comment_schema.jsonify(comment)


# Start run app
if __name__ == "__main__":
    app.run(debug=True)
