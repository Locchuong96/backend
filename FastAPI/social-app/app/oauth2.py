from .schemas import TokenData,UserOut
from .config import settings
from . import models
from . import conn,cursor
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from datetime import datetime,timedelta
import os 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

def create_access_token(data:dict): # define data is a dict
	to_encode = data.copy() # copy value to encode
	expire = datetime.utcnow() + timedelta(minutes = settings.access_token_expire_minutes) #declare time and expire token
	to_encode.update({"exp":expire})
	encoded_jwt = jwt.encode(to_encode,settings.secret_key,algorithm = settings.algorithm) # payload and signature
	return encoded_jwt

def verify_access_token(token:str,credentials_exception):
	'''
	Raise if Error
	Return token data if it valid
	'''
	try:
		# decode the token 
		payload = jwt.decode(token,settings.secret_key,algorithms = [settings.algorithm]) # if the time is expired also return none
		# get the id
		id: str = payload.get('user_id')
		# if there is a id exist
		if id is None:
			raise credentials_exception
		# create a schema for shaping data
		token_data = TokenData(id =id) # validate by TokenData schema
		return token_data
	except JWTError:
		raise credentials_exception

def get_current_user(token:str = Depends(oauth2_scheme)):

	credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
											detail = f"Could not validate this credentials",
											headers = {"WWW-Authenticate":"Bearer"})

	# get token data
	token = verify_access_token(token,credentials_exception) # {'id':id}
	
	cursor.execute(f"""SELECT * FROM users WHERE id = {token.id}""")
	user = cursor.fetchone()
	user = dict(user) #convert to dict 

	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"credentials user id {id} is not found")

	return {'user_id':user['id'],'email':user['email']}
