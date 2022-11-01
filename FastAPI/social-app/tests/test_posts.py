import pytest
from typing import List
from app import schemas

# GET

def test_get_all_posts(authorized_client,test_posts):
	res = authorized_client.get("/post/")
	def validate(post):
		return schemas.PostOut(**post)
	assert res.status_code == 200 # check status
	print(res.json())
	assert len(res.json()) == len(test_posts) # check number of test posts
	posts_list = list(map(validate,res.json()))
	# print(posts_list[0].Post)
	# assert posts_list[0].Post.title == test_posts[0].title # check the first object title

def test_get_one_post(authorized_client,test_posts):
	res = authorized_client.get(f"/post/{test_posts[0].id}")
	assert res.status_code == 200
	print(res.json())
	post = schemas.PostOut(**res.json())
	print(post)
	assert post.Post.id == test_posts[0].id
	assert post.Post.title == test_posts[0].title
	assert post.Post.content == test_posts[0].content

def test_unauthorized_user_get_all_posts(unauthorized_client,test_posts):
	res = unauthorized_client.get("/post/")
	# print(unauthorized_client.headers)
	assert res.status_code == 401

def test_unauthorized_user_get_one_post(unauthorized_client,test_posts):
	res = unauthorized_client.get(f"/post/{test_posts[0].id}")
	assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client,test_posts):
	res = authorized_client.get("/post/888")
	print(res.json())
	assert res.status_code == 404

# CREATE

@ pytest.mark.parametrize("title,content,published",[
	("awesome first post","first awesome content",True),
	("awesome second post","second awesome content",True),
	("awesome third post","third awesome content",False),
	])
def test_create_post(authorized_client,test_user,title,content,published):
	res = authorized_client.post("/post/",json = {
		"title": title,
		"content": content,
		"published": published
		})
	assert res.status_code == 201
	# print(res.json())
	created_post = schemas.PostTest(**res.json())
	assert created_post.title == title
	assert created_post.content == content
	assert created_post.published == published
	#assert created_post.owner_id == test_user['id']

@ pytest.mark.parametrize("title,content,published",[
	("awesome first post","first awesome content",True),
	("awesome second post","second awesome content",True),
	("awesome third post","third awesome content",False),
	])
def test_unauthorized_create_post(unauthorized_client,test_user,title,content,published):
	res = unauthorized_client.post("/post/",json = {
		"title": title,
		"content": content,
		"published": published
		})
	assert res.status_code == 401

def test_create_post_with_default_published_true(authorized_client,test_posts):
	res = authorized_client.post("/post/",json = {"title":"arbitrary title","content":"some random content"})
	assert res.status_code == 201
	created_post = schemas.PostTest(**res.json())
	assert created_post.published == True
	assert created_post.title == "arbitrary title"
	assert created_post.content == "some random content"

# DELETE

def test_delete_post(authorized_client,test_posts):
	res = authorized_client.delete(f"/post/{test_posts[0].id}")
	assert res.status_code == 204

def test_unauthorized_user_delete_post(unauthorized_client,test_posts):
	res = unauthorized_client.delete(f"/post/{test_posts[0].id}")
	assert res.status_code == 401
	res.json()

def test_delete_post_non_exist(authorized_client,test_posts):
	res = authorized_client.delete("/post/888")
	assert res.status_code == 404

def test_delete_other_user_post(authorized_client,test_posts2):
	res = authorized_client.delete(f"/post/34")
	assert res.status_code == 401

# PUT

def test_update_post(authorized_client,test_posts):
	data = {
	'title':'updated title',
	'content':'updated content',
	'id': test_posts[0].id
	}
	res = authorized_client.put(f"/post/{test_posts[0].id}",json =data)
	assert res.status_code == 200
	print(res.json())
	updated_post = schemas.Post(**res.json())
	assert updated_post.title == data['title']
	assert updated_post.content == data['content']

def test_update_non_exist_post(authorized_client,test_posts):
	data = {
	'title':'updated title',
	'content':'updated content',
	'id': test_posts[0].id
	}
	res = authorized_client.put("/post/888",json =data)
	assert res.status_code == 404
	print(res.json())

def test_unauthorized_user_update_post(authorized_client,test_posts):
	data = {
	'title':'updated title',
	'content':'updated content',
	'id': test_posts[1].id
	}
	res = authorized_client.put(f"/post/33",json =data)
	assert res.status_code == 401 
	print(res.json())

def test_update_other_user_post(authorized_client,test_posts):
	data = {
	'title':'updated title',
	'content':'updated content',
	'id': test_posts[33].id
	}
	res = authorized_client.put("/post/33",json =data)
	assert res.status_code == 401
	print(res.json())