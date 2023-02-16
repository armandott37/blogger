from flask import request
from datetime import datetime
from db_model import app, db, ma, comment_schema, comments_schema, response_schema, responses_schema
from comment import Comment
from response import Response

# Function API REST POST create new comment database
@app.route('/api/v1/comments', methods=['POST'])
def create_comment():
    print(request.json)
    params = request.json    
    comment = Comment(params['user_comment'], datetime.now(), params['title_comment'], params['content_comment'])
    db.session.add(comment)
    db.session.commit()
    return comment_schema.jsonify(comment)

# Function API REST GET obtain all comments from database
@app.route('/api/v1/comments', methods=['GET'])
def get_comments():    
    comments = Comment.query.all()
    print(comments)    
    return comments_schema.jsonify(comments)

# Function API REST GET obtain comment from database with id parameter
@app.route('/api/v1/comments/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.filter_by(id_comment = id).first()
    return comment_schema.jsonify(comment)

# Function API REST PUT modified comment from database with id parameter
@app.route('/api/v1/comments/<int:id>', methods=['PUT'])
def put_comment(id):
    comment = Comment.query.filter_by(id_comment = id).first()
    params = request.json
    comment.user_comment = params['user_comment']
    comment.datetime_comment = datetime.now()
    comment.title_comment = params['title_comment']
    comment.content_comment = params['content_comment']
    db.session.commit()
    print(comment)
    return comment_schema.jsonify(comment)

# Function API REST DELETE delete comment from database with id parameter
@app.route('/api/v1/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.filter_by(id_comment = id).first()
    db.session.delete(comment)
    db.session.commit()
    print(comment)
    return comment_schema.jsonify(comment)

# Function API REST POST create new response database with id comment parameter
@app.route('/api/v1/responses/<int:id>', methods=['POST'])
def create_response(id):
    print(request.json)
    params = request.json    
    response = Response(params['user_response'], datetime.now(), params['content_response'], id)
    db.session.add(response)
    db.session.commit()
    return response_schema.jsonify(response)

# Function API REST GET obtain all responses of comment with id comment parameter
#@app.route('/api/v1/responses/<int:id>', methods=['GET'])
#def get_responses(id):    
#    responses = Response.query.filter_by(id_comment = id).all()
#    print(responses)    
#    return responses_schema.jsonify(responses)

# Function API REST GET obtain response from database with id response parameter
@app.route('/api/v1/responses/<int:id>', methods=['GET'])
def get_response(id):
    response = Response.query.filter_by(id_response = id).first()
    return response_schema.jsonify(response)

# Function API REST PUT modified response from database with id parameter
@app.route('/api/v1/responses/<int:id>', methods=['PUT'])
def put_response(id):
    response = Response.query.filter_by(id_response = id).first()
    params = request.json
    response.user_response = params['user_response']
    response.datetime_response = datetime.now()    
    response.content_response = params['content_response']
    db.session.commit()
    print(response)
    return response_schema.jsonify(response)

# Function API REST DELETE delete response from database with id parameter
@app.route('/api/v1/responses/<int:id>', methods=['DELETE'])
def delete_response(id):
    response = Response.query.filter_by(id_response = id).first()
    db.session.delete(response)
    db.session.commit()
    print(response)
    return response_schema.jsonify(response)


# Start run app
if __name__ == "__main__":
    app.run(debug=True)
