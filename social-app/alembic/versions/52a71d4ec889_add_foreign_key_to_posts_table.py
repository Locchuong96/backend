"""add foreign key to posts table

Revision ID: 52a71d4ec889
Revises: 518ade6d5238
Create Date: 2022-10-26 00:35:41.481862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52a71d4ec889'
down_revision = '518ade6d5238'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',
							source_table='posts',
							referent_table ='users',
							local_cols=['owner_id'],
							remote_cols=['id'],
							ondelete='CASCADE'
							)


def downgrade():
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
