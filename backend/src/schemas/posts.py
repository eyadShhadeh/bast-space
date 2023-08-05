from sqlalchemy import Table, Column, Integer, String, DateTime, ARRAY
from backend.src.util.db import metadata
from datetime import datetime


posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(50), nullable=False, unique=True),
    Column('body', String(1000), nullable=False, unique=True),
    Column('birth_date', String(), nullable=False),
    Column('user_id', Integer),
    Column('gender', String()),
    Column('health_status', String(), nullable=False),
    Column('breed', String(), nullable=False),
    Column('status', String(), nullable=False),
    Column('images', ARRAY(String()), nullable=False),
    Column('delivery_area', String(50)),
    Column('phone', String(20), nullable=False, unique=True),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime),
)
