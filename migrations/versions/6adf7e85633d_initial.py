"""Initial

Revision ID: 6adf7e85633d
Revises: d7af94c50ad8
Create Date: 2023-12-11 20:07:20.768714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6adf7e85633d'
down_revision: Union[str, None] = 'd7af94c50ad8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('keywords', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'keywords')
    # ### end Alembic commands ###