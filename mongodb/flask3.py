from flask import Flask 
from flask_restful import Resource,Api,reqparse,abort,fields,marshal_with
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
	'db':'todomodel',
	'host':'localhost',
	'port':27017
}

db = MongoEngine()

db.init_app(app)


todos = {
	1:{"task":"Hello World Program","summary":"Video 2 source code"}
}

#create resource field

resource_fields = {'task':fields.String,
					'summary':fields.String}

# Create reqparse for post task menthod
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task",type= str, help = "Task is required", required = True)
task_post_args.add_argument("summary",type = str, help = "Summary is required",required = True)

#Create reqparse for update task menthod
task_update_args = reqparse.RequestParser()
task_update_args.add_argument("task",type = str)
task_update_args.add_argument("summary",type =str)

#create a rest api for ToDoList
class ToDoList(Resource):
	def get(self):
		return todos

# add this restful module into resource
api.add_resource(ToDoList,'/todolist')

#create a rest api for ToDo
class ToDo(Resource):
	@marshal_with(resource_fields)
	def get(self,todo_id):
		return todos[todo_id]

	@marshal_with(resource_fields)
	def post(self,todo_id):
		args = task_post_args.parse_args()
		if todo_id in todos:
			abort(409,"Task ID already taken")
		todos[todo_id] = {"task":args["task"],"summary":args["summary"]}
		return todos[todo_id]

	@marshal_with(resource_fields)
	def put(self,todo_id):
		args = task_update_args.parse_args()

		# Check if todo_id is in todos
		if todo_id not in todos:
			abort(404,message  ="Task doesn't exist, cannot update")
		
		# If there is required to update task in args 
		if args['task']:
			todos[todo_id]['task'] = args['task']

		# If there os required to update task in args
		if args['summary']:
			todos[todo_id]['summary'] = args['summary']

		return todos[todo_id]

	@marshal_with(resource_fields)
	def delete(self,todo_id):
		if todo_id not in todos:
			abort(402,message = "Task doesn't exists, cannot update")
		else:
			del todos[todo_id] # remove,del,pop

		return todos

# add this restful module into resource
api.add_resource(ToDo,"/todo/<int:todo_id>")

if __name__ == "__main__":
	app.run(debug = True)


