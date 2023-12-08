import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, JSON, Boolean, TIMESTAMP

from app.models.user import user

metadata = MetaData()

task = Table(
    "task",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=True),
    Column("start_timestamp", TIMESTAMP, arbitrary_types_allowed=True, nullable=False),
    Column("user_creator_id", Integer, ForeignKey(user.c.id)),
    Column("user_executor_id", Integer, ForeignKey(user.c.id)),
    Column("end_timestamp", TIMESTAMP, arbitrary_types_allowed=True, nullable=True)
)