from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

# this is python model also databas table, Changing setup in here you need to delete the table from postgres
# if on table there are some column (attribute) were not declare in here, it still okay to diplay declared column
class Post(Base): # Capitialize
	__tablename__ = "posts"

	id = Column(Integer,primary_key = True,nullable = False)
	title = Column(String,nullable = False)
	content = Column(String,nullable=False)
	published = Column(Boolean,server_default = 'TRUE')
	create_at = Column(TIMESTAMP(timezone=True),nullable =False,server_default= text('now()'))
	owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False) # foreignkey tablename.column,delete if no long exist cascade
	owner = relationship("User") #auto create owner reference to users table,this is not a column

class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer,primary_key = True,nullable = False)
	email = Column(String,nullable=False,unique = True)
	password = Column(String,nullable=False)
	create_at = Column(TIMESTAMP(timezone=True),nullable = False,server_default = text('now()'))
	phone_number = Column(String) # create for testing alemic migrate database

class Vote(Base):
	__tablename__ = "votes"

	post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key = True,nullable=False)
	user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key = True,nullable=False)



	
