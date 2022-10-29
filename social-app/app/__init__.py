import os
import time
import psycopg2
from psycopg2.extras import RealDictCursor # get extra field to get the column when where database
from .schemas import Settings
from pydantic import BaseModel,EmailStr,BaseSettings
from datetime import datetime
from typing import Optional
from .config import settings

while True: # MUST connect to database successfully before runing server API
	try:
		print(f"\nTrying to connect to postgres {settings.database_hostname} database {settings.database_name}")
		conn = psycopg2.connect(host = settings.database_hostname,
								database= settings.database_name,
								user = settings.database_username,
								password = settings.database_password,
								cursor_factory=RealDictCursor)
		cursor = conn.cursor()
		print(f"\nConnecting to postgres {settings.database_hostname} database {settings.database_name} connected successfully!")
		break # jump out while loop if successed
	except Exception as e:
		print(f"Connecting to postgres {settings.database_hostname} database {settings.database_name} FAILED!")
		print("Error: ",e)
		time.sleep(3)
