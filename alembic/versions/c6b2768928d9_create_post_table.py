"""create post table

Revision ID: c6b2768928d9
Revises: 
Create Date: 2022-08-15 20:02:20.653583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6b2768928d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))

def downgrade() -> None:
    op.create_table('posts')
    pass
