import os
from fastapi import FastAPI
from sqlalchemy import (
    create_engine, MetaData
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()
DATABASE_FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__), "app.db"))
DATABASE_URI = f'sqlite:///{DATABASE_FILENAME}?check_same_thread=False'

SECRET_KEY = 'eeabf7170c4a939ce3d74b0ddd89d75990eea99b18f1f32e'

engine = create_engine(DATABASE_URI)

metadata = MetaData(bind=engine)

Base = declarative_base(metadata=metadata)

from .__all_models import *

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()

from .routes import *

current_user = None
