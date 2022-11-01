from typing import List
from fastapi import status,HTTPException,Depends,APIRouter,Header,Response
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas import Vote,Voted
from ..oauth2 import get_current_user

router = APIRouter(prefix = '/vote', tags = ['votes'])

@router.get("/",response_model = List[Voted])
def get_votes(db:Session = Depends(get_db),token: str = Header('Authentication')):
	# verify user token
	current_user = get_current_user(token)
	votes = db.query(models.Vote).all()
	return votes
	
@router.post("/",status_code = status.HTTP_201_CREATED)
def vote(vote:Vote,db:Session = Depends(get_db),token: str = Header('Authentication')):
	# get current_user
	current_user = get_current_user(token)
	# post a post -> get current user_id, find row by post_id , user_id
	vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
										models.Vote.user_id == current_user['user_id'])
	found_vote = vote_query.first()

	if found_vote:
		if vote.dir == 1:
			raise HTTPException(status_code = status.HTTP_409_CONFLICT,
				detail= f"User (user_id = {current_user['user_id']}) already vote this post (post_id = {vote.post_id})")
		else:
			vote_query.delete(synchronize_session =False)
			db.commit()
			return {"message":"successfully delete vote!"}

	else:
		post_query = db.query(models.Post).filter(models.Post.id==vote.post_id)
		post = post_query.first()
		if post and vote.dir ==1:
			new_vote = models.Vote(post_id=vote.post_id,user_id=current_user['user_id'])
			db.add(new_vote)
			db.commit()
			return {"message":"successfully vote!"}
		else:
			raise HTTPException(status_code = status.HTTP_409_CONFLICT,
				detail= f"This post is NOT exist or User did not vote post yet!")

@router.get("/mine/",response_model = List[Voted])
def my_vote(db:Session= Depends(get_db),token: str = Header('Authentication')): # None default arg before default arg	
	current_user = get_current_user(token)
	results = db.query(models.Vote).filter(models.Vote.user_id == current_user['user_id']).all()
	return results

@router.get("/search/",response_model = List[Voted])
def search_user(post_id:int,db:Session= Depends(get_db),token: str = Header('Authentication')):
	current_user = get_current_user(token)

	post_query = db.query(models.Post).filter(models.Post.id==post_id)
	post = post_query.first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
							detail = f"post with id =  {post_id} not found")

	results = db.query(models.Vote).filter(models.Vote.post_id == post_id).all()

	return results
