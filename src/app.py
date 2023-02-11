from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@127.0.0.1:23306/db_blogger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Comment(db.Model):
    id_comment = db.Column(db.Integer, primary_key = True)
    user_comment = db.Column(db.String(30), nullable = False)
    datetime_comment = db.Column(db.DateTime, default = datetime.utcnow)
    title_comment = db.Column(db.String(50), nullable = False)
    content_comment = db.Column(db.String(200), nullable = False)

    def __init__(self, user_comment, datetime_comment, title_comment, content_comment):
        self.user_comment = user_comment
        self.datetime_comment = datetime_comment
        self.title_comment = title_comment
        self.content_comment = content_comment

    def __repr__(self):
        return f"User : {self.user_comment} Datetime : {self.datetime_comment} Title Comment : {self.title_comment} Content Comment : {self.content_comment}"


def create_db():    
    app.app_context().push()
    db.create_all() # In case user table doesn't exists already. Else remove it.    
    comment = Comment('Armando', datetime.now(), 'Title comment', 'Contain Comment')
    db.session.add(comment)
    db.session.commit() # This is needed to write the changes to database
    print(Comment.query.all())
    print(Comment.query.filter_by(user_comment='Armando').first())

@app.route('/comment', methods=['POST'])
def create_comment():
    print(request.json)
    params = request.json
    comment = Comment(params['user_comment'], datetime.now(), params['title_comment'], params['content_comment'])
    db.session.add(comment)
    db.session.commit()
    return params

#create_db()

if __name__ == "__main__":
    app.run(debug=True)
