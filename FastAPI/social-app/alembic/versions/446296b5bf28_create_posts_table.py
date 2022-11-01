"""create posts table

Revision ID: 446296b5bf28
Revises: 
Create Date: 2022-10-26 00:06:09.597460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '446296b5bf28'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
    	sa.Column('id',sa.Integer(),nullable = False, primary_key = True),
    	sa.Column('title',sa.String(),nullable=False),
    	sa.Column('content',sa.String(),nullable=False),
    	sa.Column('published',sa.Boolean(),server_default = 'TRUE'),
    	sa.Column('create_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False)
    	)

def downgrade():
    pass
    op.drop_table('posts')