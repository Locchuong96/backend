from marshmallow import Schema, fields, post_load,validate
import marshmallow

class Person:
   def __init__(self,name,age,email):
      self.name = name
      self.age = age
      self.email = email
   def __repr__(self):
      return f'{self.name} is {self.age} years old.'

def validate_age(age):
   if age < 20:
      raise marshmallow.exceptions.ValidationError("The age is too young")
      # return False

class PersonSchema(Schema):
   name = fields.String(validate = validate.Length(max = 5) )
   age = fields.Integer(validate= validate_age)
   email = fields.Email()
   location = fields.String(required = True) #

   @post_load
   def create_person(self,data, **kwargs):
      return Person(**data)

input_data = {}

input_data['name'] = input("What is your name? ")
input_data['age'] = input("How old are you? ")
input_data['email'] = input("What is your email?" )

print(input_data) # serialize

try:
   schema  = PersonSchema()
   print(schema)
   person = schema.load(input_data) # deserialize
   print(person)
except marshmallow.exceptions.ValidationError as err:
   print(err)
   print(err.valid_data) # print out the valid data

