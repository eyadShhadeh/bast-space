import os
import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import Boolean, Column, DateTime, Float, SmallInteger, Text, UniqueConstraint, MetaData
from sqlalchemy.dialects.postgresql import UUID

pool_size = int(os.getenv('SQLALCHEMY_POOL_SIZE', 10))


def get_db_url():
    return 'postgresql://%s:%s@%s:%s/%s' % (
        os.getenv('PGUSER', 'postgres'),
        os.getenv('PGPASSWORD', 'password'),
        os.getenv('PGHOST', 'bast-space-db'),
        os.getenv('PGPORT', '5432'),
        os.getenv('PGDATABASE', 'postgres'),
    )


engine = sa.create_engine(get_db_url(), echo=False,
                          echo_pool=True, pool_size=pool_size, max_overflow=16)

metadata: MetaData = sa.MetaData()

now = datetime.utcnow
default_now = dict(default=now, server_default=sa.func.now())

if __name__ == "__main__":
    # Creating tables in the database
    metadata.create_all(engine)
