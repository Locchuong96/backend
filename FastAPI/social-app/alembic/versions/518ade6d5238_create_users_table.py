"""create users table

Revision ID: 518ade6d5238
Revises: 446296b5bf28
Create Date: 2022-10-26 00:24:18.676732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '518ade6d5238'
down_revision = '446296b5bf28'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
    				sa.Column('id',sa.Integer(),nullable=False),
    				sa.Column('email',sa.String(),nullable=False),
    				sa.Column('password',sa.String(),nullable=False),
    				sa.Column('create_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
    				sa.PrimaryKeyConstraint('id'), # add constrain primary key
    				sa.UniqueConstraint('email')
    				)

def downgrade():
    op.drop_table('users')