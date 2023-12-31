import datetime as dt
from sqlalchemy import MetaData, Table, Column, String, ForeignKey, func, DateTime, Integer, UniqueConstraint

metadata = MetaData()

logger = Table(
    "logger",
    metadata,
    Column("log_id", Integer, primary_key=True),
    Column("log_subject", String, nullable=False),
    Column("log_id_user", Integer, nullable=False),
    Column("log_email_user", String, nullable=True),
    Column("log_time", DateTime(timezone=True), server_default=func.now(), default=dt.datetime.now().date(),
           nullable=False),
)
