from flask import request
from datetime import datetime
from db_model import app, db, ma, comment_schema, comments_schema, response_schema, responses_schema
from comment import Comment
from response import Response

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

# Function API REST POST create new response database
@app.route('/response_POST/<int:id_comment>', methods=['POST'])
def create_response(id_comment):
    print(request.json)
    params = request.json    
    response = Response(params['user_response'], datetime.now(), params['content_response'], id_comment)
    db.session.add(response)
    db.session.commit()
    return response_schema.jsonify(response)

# Function API REST GET obtain all responses of comment from database
@app.route('/responses_GET/<int:id_comment>', methods=['GET'])
def get_responses(id_comment):    
    responses = Response.query.filter_by(id_comment = id_comment).all()
    print(responses)    
    return responses_schema.jsonify(responses)

# Function API REST GET obtain response from database with id parameter
@app.route('/response_GET/<int:id_response>', methods=['GET'])
def get_response(id_response):
    response = Response.query.filter_by(id_response = id_response).first()
    return response_schema.jsonify(response)

# Function API REST PUT modified response from database with id parameter
@app.route('/response_PUT/<int:id_response>', methods=['PUT'])
def put_response(id_response):
    response = Response.query.filter_by(id_response = id_response).first()
    params = request.json
    response.user_response = params['user_response']
    response.datetime_response = datetime.now()    
    response.content_response = params['content_response']
    db.session.commit()
    print(response)
    return response_schema.jsonify(response)

# Function API REST DELETE delete response from database with id parameter
@app.route('/response_DEL/<int:id_response>', methods=['DELETE'])
def delete_response(id_response):
    response = Response.query.filter_by(id_response = id_response).first()
    db.session.delete(response)
    db.session.commit()
    print(response)
    return response_schema.jsonify(response)


# Start run app
if __name__ == "__main__":
    app.run(debug=True)
