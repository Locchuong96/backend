from marshmallow import Schema,fields,post_load

class Person:
   def __init__(self,name,age):
      self.name = name
      self.age = age
   def __repr__(self):
      return f"{self.name} is {self.age} years old."

class PersonSchema(Schema):
   name= fields.String()
   age = fields.Integer()

   # create a function for deserialize anything loaded into the PersonSchema
   @post_load
   def create_person(self,data,**kwargs):
      return Person(**data)

input_data = {}

input_data['name'] = input("What is your name? ")
input_data["age"] = input("What is your age? ")

schema = PersonSchema()
#result = schema.load(input_data) # deserialize

person = Person(name = input_data["name"],age = input_data["age"])
result = schema.dump(person) # serialize
print(result)

