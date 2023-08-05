from sqlalchemy import Table, Column, Integer, String, DateTime
from backend.src.util.db import metadata
from datetime import datetime


photos = Table(
    'photos',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('photo_name', String(50), nullable=False),
    Column('photo_url', String(100), nullable=False, unique=True),
    Column('status', String(), nullable=False),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime),
)
