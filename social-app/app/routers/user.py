from typing import List
from fastapi import Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas import UserCreate,UserOut
from ..utils import hash_pass

router = APIRouter(prefix = '/users', tags = ['users'])

@router.get("/",response_model = List[UserOut])
def get_users(db: Session = Depends(get_db)):
	users = db.query(models.User)
	return users.all()

@router.get("/{id}",response_model = UserOut)
def get_user(id:int,db:Session = Depends(get_db)):
	user  = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"user with id {id} not found")
	return user

@router.post("/",status_code = status.HTTP_201_CREATED,response_model = UserOut)
def create_user(user: UserCreate ,db: Session = Depends(get_db)):

	# validate the email
	current_user = db.query(models.User).filter(models.User.email == user.email).first()
	print(current_user)

	if current_user:
		raise HTTPException(status_code = status.HTTP_409_CONFLICT,
							detail = f"{user.email} is already be taken")

	#hash the password -user.password
	hashed_password = hash_pass(user.password)
	user.password = hashed_password

	# create new user
	new_user = models.User(**user.dict()) # unpackage form 
	db.add(new_user) # add new row
	db.commit() # commit to save it to database
	db.refresh(new_user) # refesh to see brand new user
	return new_user# Follow PostResponse
	return {"message":"successed"}
