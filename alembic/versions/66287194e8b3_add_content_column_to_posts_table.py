"""add content column to posts table

Revision ID: 66287194e8b3
Revises: 9b587b03a22a
Create Date: 2026-06-26 23:29:04.092428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66287194e8b3'
down_revision: Union[str, Sequence[str], None] = '9b587b03a22a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
