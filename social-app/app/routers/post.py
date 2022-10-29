from typing import List,Optional
from fastapi import Response,status,HTTPException,Depends,APIRouter,Header
from fastapi.params import Body
from sqlalchemy import func # to access count function
from sqlalchemy.orm import Session
from .. import models
from ..oauth2 import get_current_user
from ..database import get_db
from ..schemas import PostBase,PostCreate,PostUpdate,PostResponse,UserOut,PostCreated,PostOut

router = APIRouter(prefix = '/post',tags = ['posts']) # create router object

@router.get("/",response_model = List[PostOut])
def get_posts(db:Session= Depends(get_db),token: str = Header('Authentication')): # Pydantic format
	current_user = get_current_user(token)
	posts = db.query(models.Post).all()
	# post_query = db.query(models.Post) SELECT ALL
	# post_query = db.query(models.Post).join(models.Vote,models.Post.id == models.Vote.post_id,isouter = True)  LEFT OUTER JOIN
	post_query = db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(
					models.Vote,models.Post.id == models.Vote.post_id,isouter = True).group_by(
						models.Post.id)
	results = post_query.all()
	return results

@router.post("/",status_code = status.HTTP_201_CREATED,response_model = PostResponse)
def create_post(post:PostCreate,db:Session = Depends(get_db),token: str = Header('Authentication')): #,user_id: int = Depends(get_current_user)):
	current_user = get_current_user(token) # verify user login by token
	new_post = models.Post(owner_id = current_user['user_id'], **post.dict()) # unpackage form 
	db.add(new_post) # add new row
	db.commit() # commit to save it to database
	db.refresh(new_post)
	return new_post# Follow PostResponse 

@router.get("/{id}",response_model = PostOut)
def get_post(id: int,db: Session = Depends(get_db),token: str = Header('Authentication')): # str as default
	current_user = get_current_user(token)
	post_query = db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(
					models.Vote,models.Post.id == models.Vote.post_id,isouter = True).group_by(
						models.Post.id).where(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")

	if post.Post.owner_id != current_user['user_id']:
			raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
							detail = f"this post is not belong to this user")

	return post #{"post_detail": post}

@router.delete("/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),token: str = Header('Authentication')):
	current_user = get_current_user(token)
	post_query = db.query(models.Post).filter(models.Post.id==id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")
	else:
		if post.owner_id != current_user['user_id']:
			raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
							detail = f"this post is not belong to this user")
		else:
			post_query.delete(synchronize_session =False)
			db.commit()

	return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.get("/mine/",response_model = List[PostOut]) # '/mine/' NOT '/mine'
def my_posts(db:Session= Depends(get_db),token: str = Header('Authentication')):
	current_user = get_current_user(token)
	# my_posts = db.query(models.Post).filter(models.Post.owner_id == current_user['user_id']).all()
	post_query = db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(
					models.Vote,models.Post.id == models.Vote.post_id,isouter = True).group_by(
						models.Post.id).where(models.Post.owner_id == current_user['user_id'])
	posts = post_query.all()
	return posts

@router.get("/search/")
def search_post(keyword:Optional[str] = "",limit:int = 10,skip:int = 0,db:Session= Depends(get_db)): # None default arg before default arg
	
	# results_query = db.query(models.Post).filter(models.Post.title.contains(keyword))

	results_query =  db.query(models.Post,func.count(models.Vote.post_id).label('votes')).join(
					models.Vote,models.Post.id == models.Vote.post_id,isouter = True).group_by(
						models.Post.id).filter(models.Post.title.contains(keyword))

	results = results_query.limit(limit).offset(skip).all()
	
	return {"limit":limit,
			"skip":skip,
			"keyword":keyword,
			"results":results}

@router.put("/{id}",response_model = PostResponse)
def update_post(id:int,update_post:PostBase,db:Session = Depends(get_db),token: str = Header('Authentication')): #,data:dict=Body(...) must be in the last of declaration
	current_user = get_current_user(token) # verify user login by token
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")

	if post.owner_id != current_user['user_id']:
			raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
							detail = f"this post is not belong to this user")

	post_query.update(update_post.dict(),synchronize_session =False)
	db.commit()
	return post_query.first()

@router.patch("/{id}",response_model = PostResponse)
def update_field(id:int,response:Response,data:dict=Body(...),db: Session= Depends(get_db),token: str = Header('Authentication')): #,data:dict=Body(...) must be in the last of declaration
	current_user = get_current_user(token) # verify user login by token
	post_query = db.query(models.Post).filter(models.Post.id == id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id {id} not found")

	if post.owner_id != current_user['user_id']:
			raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
							detail = f"this post is not belong to this user")
	# update
	if 'title' in data.keys():
		post.title = data['title']

	if 'content' in data.keys():
		post.content = data['content']

	if 'published' in data.keys():
		post.published = data['published']

	db.commit()

	response.status_code = status.HTTP_202_ACCEPTED

	return post_query.first() #{"message":"successfully","data":post_query.first()}
