"""create votes table

Revision ID: 2a72f4588612
Revises: 52a71d4ec889
Create Date: 2022-10-26 00:57:19.756687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a72f4588612'
down_revision = '52a71d4ec889'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
    	sa.Column('post_id',sa.Integer(),primary_key=True,nullable=False),
    	sa.Column('user_id',sa.Integer(),primary_key=True,nullable=False)
    	)
    op.create_foreign_key('votes_posts_fk',
							source_table='votes',
							referent_table ='posts',
							local_cols=['post_id'],
							remote_cols=['id'],
							ondelete='CASCADE'
							)
    op.create_foreign_key('votes_users_fk',
							source_table='votes',
							referent_table ='users',
							local_cols=['user_id'],
							remote_cols=['id'],
							ondelete='CASCADE'
							)


def downgrade():
    op.drop_constraint('votes_posts_fk',table_name='votes')
    op.drop_constraint('votes_users_fk',table_name='users')
    op.drop_table('votes')
