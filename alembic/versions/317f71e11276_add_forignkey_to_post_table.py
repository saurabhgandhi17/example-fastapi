"""add forignkey to post table

Revision ID: 317f71e11276
Revises: 36df9ae398fc
Create Date: 2022-08-15 20:31:11.516433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317f71e11276'
down_revision = '36df9ae398fc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column("posts",'owner_id')
    pass
