from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
	res = client.get("/")
	# print(res.json())
	assert res.status_code == 200
	assert res.json() == {"message":"wellcome to my api"}


def test_sqlalchemy():
	res = client.get("/sqlalchemy")
	assert res.status_code == 200
	assert res.json() == {"message":"Successfully!"}