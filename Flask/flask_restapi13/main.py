from flask import Flask,request
from flask_restful import  Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

"""
Create a video dict to storage as a database
"""
videos = {}

"""
Make a video_put_args variable
and add all arguments required
"""
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type = str, help = "Name of the video", required = True)
video_put_args.add_argument("views",type = int, help = "Views of the video", required = True)
video_put_args.add_argument("likes",type = int , help = "Likes of the video", required = True)

"""
Create a function to abort if the video doesn't not exist
"""
def video_non_exist(video_id):
    if video_id not in videos:
        abort("Video ID: {} doesn't exits".format(video_id))

"""
Create a model
"""
class Video(Resource):
    def get(self,video_id):
        video_non_exist(video_id)
        return videos[video_id]
    
    def put(self,video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return{video_id: args}
        
"""
Make a route connect to your model
"""
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)