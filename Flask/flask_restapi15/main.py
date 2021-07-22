from flask import Flask,request
from flask_restful import  Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)

class VideoModel(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer,nullable = False)
    likes = db.Column(db.Integer,nullable = False)

    def __repr__(self):
        return f"Video(name: '{self.name}',views: '{self.views}',like: '{self.likes}')"

#db.create_all()

"""
Make a video_put_args variable
and add all arguments required
"""
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type = str, help = "Name of the video", required = True)
video_put_args.add_argument("views",type = int, help = "Views of the video", required = True)
video_put_args.add_argument("likes",type = int , help = "Likes of the video", required = True)

"""
Define Serialize form for data output
"""
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}
"""
Create a model
"""
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.get(video_id)
        return result
    
    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id = video_id,name = args['name'], views =args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video,201

    def delete(self,video_id):
        video = VideoModel.query.get(video_id)
        db.session.delete(video)
        db.session.commit()
        return 'Deleted',204
"""
Make a route connect to your model
"""
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)