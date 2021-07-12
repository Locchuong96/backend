from flask import Flask,jsonify 

app = Flask(__name__)

courses = [ 
            {   'name':'Python Programming Certification',
                'course_id':'0',
                'Description': 'Python programming certification helps you learn'
                               'python in the structured learning path with innovative'
                               'out of box projects matching the industry stadards',
                'price': 'visit Edureka.co to know more'
            },
            {   'name':'Data Science With Python Certification',
                'course_id':'1',
                'Description': 'Data sciene with python helps you master the data science'
                               'life cycle processes a structured learning path',
                'price': 'visit Edureka.co to know more'
            },
            {   'name':'Ai and Machine Learning Certification',
                'course_id':'2',
                'Description': 'AI and ML certification will help you master AL/ML with'
                               'top notch projects like speechrecognition,chatbots,etc,.',
                'price': 'visit Edureka.co to know more'
            },
            {   'name':'ySpark Certification Traning',
                'course_id':'3',
                'Description': 'ySpark Certification Training is designed to provide you the knowledge and skillshat to become a successful Spark Developer using Python and prepare for the Cloudera Hadoop and Spark Developer Certification Exam',
                'price': 'visit Edureka.co to know more'
            },
            {   'name':'ySpark Certification Traning',
                'course_id':'4',
                'Description': 'ySpark Certification Training is designed to provide you the knowledge and skillshat to become a successful Spark Developer using Python and prepare for the Cloudera Hadoop and Spark Developer Certification Exam',
                'price': 'visit Edureka.co to know more'
            },
            {   'name':'Natural Language Certification with python',
                'course_id':'5',
                'Description': 'NLP course take you through the essrentialsof text processing all the way up to classifying text using Machine Learning algorithm',
                'price': 'visit Edureka.co to know more'
            }
            ]

@app.route('/')
def index():
    return 'Welcome to the course API'

@app.route('/courses',methods = ['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route('/courses/<int:course_id>',methods = ['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

@app.route('/courses',methods = ['POST'])
# curl -i -H "Content-Type: Application/json" -X POST http://127.0.0.1:5000/courses
def create():
    course = [{   'name':'Natural Language Certification with python',
                'course_id':'5',
                'Description': 'NLP course take you through the essrentialsof text processing all the way up to classifying text using Machine Learning algorithm',
                'price': 'visit Edureka.co to know more'
            }]
    courses.append(course)
    return jsonify({'Created':course})

@app.route("/courses/<int:course_id>",methods = ['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course': courses[course_id]})

@app.route("/courses/<int:course_id>",methods = ['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug = True)
