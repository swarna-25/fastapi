"""create post table

Revision ID: 9b587b03a22a
Revises: 
Create Date: 2026-06-26 22:48:18.470077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b587b03a22a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(): 
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,
                                      primary_key=True),sa.Column('title',sa.String(),nullable=False))
    #pass


def downgrade(): 
    op.drop_table('posts')
    pass
