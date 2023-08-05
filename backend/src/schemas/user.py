from sqlalchemy import Table, Column, Integer, String, DateTime
from backend.src.util.db import metadata
from datetime import datetime


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(50), nullable=False, unique=True),
    Column('email', String(100), nullable=False, unique=True),
    Column('role', String(), nullable=False),
    Column('gender', String(), nullable=False),
    Column('delivery_area', String(100)),
    Column('phone', String(100), nullable=False, unique=True),
    Column('contact_links', String(100)),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime),
)
