"""empty message

Revision ID: 807e20aaa606
Revises: 
Create Date: 2021-10-29 15:09:27.404997

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '807e20aaa606'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('_password', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.alter_column('house_listing', 'address',
               existing_type=mysql.VARCHAR(length=256),
               comment=None,
               existing_comment='所在地',
               existing_nullable=True)
    op.alter_column('house_listing', 'desc',
               existing_type=mysql.VARCHAR(length=256),
               comment=None,
               existing_comment='描述',
               existing_nullable=True)
    op.alter_column('house_listing', 'hx',
               existing_type=mysql.VARCHAR(length=256),
               comment=None,
               existing_comment='户型',
               existing_nullable=True)
    op.alter_column('house_listing', 'nature',
               existing_type=mysql.VARCHAR(length=32),
               comment=None,
               existing_comment='性质： 住宅',
               existing_nullable=True)
    op.alter_column('house_listing', 'price',
               existing_type=mysql.VARCHAR(length=256),
               comment=None,
               existing_comment='价格',
               existing_nullable=True)
    op.alter_column('house_listing', 'status',
               existing_type=mysql.VARCHAR(length=32),
               comment=None,
               existing_comment='状态： 在售， 未售',
               existing_nullable=True)
    op.drop_index('EVERY_DAY', table_name='house_listing')
    op.create_index('EVERY_DAY', 'house_listing', ['house_id', 'area_id', 'create_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('EVERY_DAY', table_name='house_listing')
    op.create_index('EVERY_DAY', 'house_listing', ['house_id', 'area_id', 'create_date'], unique=True)
    op.alter_column('house_listing', 'status',
               existing_type=mysql.VARCHAR(length=32),
               comment='状态： 在售， 未售',
               existing_nullable=True)
    op.alter_column('house_listing', 'price',
               existing_type=mysql.VARCHAR(length=256),
               comment='价格',
               existing_nullable=True)
    op.alter_column('house_listing', 'nature',
               existing_type=mysql.VARCHAR(length=32),
               comment='性质： 住宅',
               existing_nullable=True)
    op.alter_column('house_listing', 'hx',
               existing_type=mysql.VARCHAR(length=256),
               comment='户型',
               existing_nullable=True)
    op.alter_column('house_listing', 'desc',
               existing_type=mysql.VARCHAR(length=256),
               comment='描述',
               existing_nullable=True)
    op.alter_column('house_listing', 'address',
               existing_type=mysql.VARCHAR(length=256),
               comment='所在地',
               existing_nullable=True)
    op.drop_table('user')
    # ### end Alembic commands ###