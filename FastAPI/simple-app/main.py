from fastapi import FastAPI
from starlette import responses
from fastapi.middleware.cors import CORSMiddleware
# init app
app = FastAPI()

# domains list accepted pass COR policy [*] mean everything
origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
	)

@app.get("/")
async def root():
	return responses.RedirectResponse("/redoc")

@app.get("/methods")
async def get():
	return {"message":"GET successfully!"}

@app.post("/methods")
async def post():
	return {"message":"POST successfully!"} 