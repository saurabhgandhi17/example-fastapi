"""add users table

Revision ID: 36df9ae398fc
Revises: 5a9d7b3be0ba
Create Date: 2022-08-15 20:24:16.137587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36df9ae398fc'
down_revision = '5a9d7b3be0ba'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
                            sa.Column('email',sa.String(),nullable=False),
                            sa.Column('password',sa.String(),nullable=False),
                            sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email'),
                    )

def downgrade() -> None:
    op.create_table('users')
    pass
