### Migration database with Alembic

**Step1:** init alembic floder `alembic init alembic`

**Step2:** change something in alembic/env.py

	 	from app.models import Base # import base from database
		from app.config import settings
		
		# access to the values within the .ini file in use.
		config = context.config 
		config.set_main_option('sqlalchemy.url',f'postgresql+psycopg2://{settings.database_username}:{settings.
		database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}')
		target_metadata = Base.metadata

**Step3:** change sqlalchemy.url in alembic.init:

		sqlalchemy.url = #driver://user:pass@localhost/dbname

**Step4:** make a revision to create table `alembic revision -m "create posts table"`

**Step5:** set upgrade to modify table,set downgrade to revert the chaning:

		from alembic import op
		import sqlalchemy as sa
		# revision identifiers, used by Alembic.
		revision = '628ca9a88fe3'
		down_revision = None
		branch_labels = None
		depends_on = None
		def upgrade():
		    '''
		    define action when modify table
		    '''
		    op.create_table('posts',sa.Column('id',sa.Integer(),nullable = False, primary_key = True),
		    				sa.Column('title',sa.String(),nullable=False))
		    pass
		def downgrade():
		    '''
		    define action when undo
		    '''
		    op.drop_table('posts')

**Step6:** `alembic current`

**Step7:** `alembic upgrade 628ca9a88fe3`

**Step8:** create the other revision to add new column on table `alembic revision -m "add add content column to posts table"` and inside revision file `.py` *(Note: When you set a upgrade function you also set a downrate function)*

**Step9:** Check current state `alembic current`

**Step10:** Check head revision (not execute yet thing) `alembic heads`

**Step11:** Execute head revision `alembic upgrade head` or `alembic upgrade +1`

**Step12:** If you want to downgrade `alembic downgrade <the previod revision>` or `alembic downgrade -1`

**Step13:** Check history `alembic history`

**Step14:** Auto generate tables `alembic revision --autogenerate -m 'auto create votes table'`

**Step14:** Auto check changing and auto generate revision `alembic revision --autogenerate -m 'add phone number'` and upgrade `alembic upgrade head`