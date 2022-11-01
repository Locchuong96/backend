## Build your custom image to deploy app

Dockerfile content:


	FROM python:3.9.7

	WORKDIR /usr/src/app

	COPY requirements.txt ./

	RUN pip install -r requirements.txt

	COPY . .

	CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

- build the image from the same directory with Dockerfile `docker build - t fastapi .`

- check your image `docker images`

- run your docker image `docker run fastapi -p 8000:8000`

- or use docker-compose with content `docker-compose.yml`

		version: "3"

		services:
		  api:
		    build: .
		    ports:
		      - 8000:8000

- run docker-compose `docker-compose.yml`: `docker-compose up -d`

- view logs error `docker logs <your_container_name>`

- shut container down `docker compose down`

- login `docker login`

- push your image `docker push <your_account/your_image_name:tag_name>`

- deploy specidic .yml file : `docker-compose -f docker-compose-dev.yml up -d`