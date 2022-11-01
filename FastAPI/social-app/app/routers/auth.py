from fastapi import Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas import UserLogin,Token
from ..utils import verify
from ..oauth2 import create_access_token

router = APIRouter(prefix = '/login',tags= ['authentication'])

@router.post('/',response_model = Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),db :Session= Depends(get_db)): #user_credentials: UserLogin

	user = db.query(models.User).filter(models.User.email== user_credentials.username).first()
	
	if not user:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
							detail = f"Invalid Credentials")
	# compare the password new_hash = user.hash
	match = verify(user_credentials.password,user.password)
	if not match:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
							detail = f"Invalid Credentials")

	# create a token
	access_token = create_access_token(data = {"user_id":user.id})

	return {"access_token" : access_token,
			"token_type": "bearer"}