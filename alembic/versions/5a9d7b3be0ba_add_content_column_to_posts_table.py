"""add content column to posts table

Revision ID: 5a9d7b3be0ba
Revises: c6b2768928d9
Create Date: 2022-08-15 20:16:53.052042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9d7b3be0ba'
down_revision = 'c6b2768928d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.Integer(),nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts','content')
    pass