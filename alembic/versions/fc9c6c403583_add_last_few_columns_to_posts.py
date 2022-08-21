"""add last few columns to posts

Revision ID: fc9c6c403583
Revises: 317f71e11276
Create Date: 2022-08-15 20:35:56.766826

"""
from xmlrpc import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9c6c403583'
down_revision = '317f71e11276'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass



def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
