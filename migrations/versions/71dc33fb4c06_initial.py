"""Initial

Revision ID: 71dc33fb4c06
Revises: e4b17fba89b3
Create Date: 2023-12-09 02:41:04.330058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '71dc33fb4c06'
down_revision: Union[str, None] = 'e4b17fba89b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logger',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('log_subject', sa.String(), nullable=False),
    sa.Column('log_id_user', sa.Integer(), nullable=False),
    sa.Column('log_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['log_id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.alter_column('task', 'start_timestamp',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False)
    op.drop_column('task', 'end_timestamp')
    op.alter_column('user', 'register_timestamp',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'register_timestamp',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.add_column('task', sa.Column('end_timestamp', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.alter_column('task', 'start_timestamp',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.drop_table('logger')
    # ### end Alembic commands ###
