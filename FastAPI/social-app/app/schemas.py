from pydantic import BaseModel,EmailStr,BaseSettings
from pydantic.types import conint
from datetime import datetime
from typing import Optional

class Settings(BaseSettings):
	database_username: str #tge name must be correct inside .env
	database_password: str
	database_name: str
	database_port: int
	database_hostname: str
	algorithm: str
	secret_key: str
	access_token_expire_minutes: int

	class Config:
		env_file = ".env"

class UserCreate(BaseModel):
	email: EmailStr# email validation
	password: str
	# create_at: datetime default

class UserOut(BaseModel):
	id: int
	email: EmailStr
	create_at: datetime
	class Config:
		orm_mode = True

class UserLogin(BaseModel):
	email:EmailStr
	password:str

class PostBase(BaseModel):
	'''
	PostBase inherited from BaseModel
	'''
	title: str
	content: str
	published: bool = True # default
	# owner_id: int

class PostCreate(PostBase):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

class PostUpdate(BaseModel):
	'''
	PostCreate inherited from PostBase
	'''
	pass # no more attribute

class PostCreated(PostBase):
	title: str
	content: str
	published: bool
	owner: UserOut # pydantic class

	class Config:
		orm_mode = True

class PostResponse(PostBase):
	id: int
	create_at: datetime #str
	owner_id: int
	class Config:
		'''
		Pydantic;s orm_mode will tell Pydantic model to read data even if it is not a dict, but ORM model
		(or nay other arbitrary object with attriutes) data['id'] = data.id
		'''
		orm_mode = True

class Post(BaseModel):
	published:bool
	title:str
	owner_id:int
	id:int
	content:str
	create_at: datetime
	class Config:
		orm_mode=True

class PostOut(BaseModel):
	Post: Post
	votes:int
	class Config:
		orm_mode=True

class PostTest(BaseModel):
	title:str
	content:str
	published:bool

class PostTest2(BaseModel):
	title:str
	content:str
	published:bool
	owner_id:int

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: Optional[str] = None

class Vote(BaseModel):
	post_id: int
	dir: conint(le=1) # less or equal 1

class Voted(BaseModel):
	post_id: int
	user_id: int

	class Config:
		orm_mode = True