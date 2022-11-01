import pytest
from app import schemas

# GET

def test_vote_up_post(authorized_client,test_posts):
	res = authorized_client.post("/vote/",json = {"post_id":test_posts[0].id,"dir":1})
	assert res.status_code == 201
	print(res.json())

def test_vote_twice_post(authorized_client,test_posts):
	res = authorized_client.post("/vote/",json = {"post_id":test_posts[0].id,"dir":1})
	assert res.status_code == 409
	print(res.json())

def test_vote_down_post(authorized_client,test_posts):
	res = authorized_client.post("/vote/",json = {"post_id":test_posts[0].id,"dir":0})
	assert res.status_code == 201
	print(res.json())

def test_vote_down_non_exist_post(authorized_client,test_posts):
	res = authorized_client.post("/vote/",json = {"post_id":test_posts[1].id,"dir":0})
	assert res.status_code == 409
	print(res.json())

def test_vote_non_exist_post(authorized_client,test_posts):
	res = authorized_client.post("/vote/",json = {"post_id":888,"dir":1})
	assert res.status_code == 409
	print(res.json())

def test_vote_unauthorized_user(unauthorized_client,test_posts):
	res = unauthorized_client.post("/vote/",json = {"post_id":test_posts[1].id,"dir":1})
	assert res.status_code == 401
	print(res.json())
	

# UPDATE

# DELETE

# PUT