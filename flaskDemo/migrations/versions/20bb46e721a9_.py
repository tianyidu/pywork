"""empty message

Revision ID: 20bb46e721a9
Revises: 
Create Date: 2017-08-16 11:29:58.344859

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '20bb46e721a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('mdlinfo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mdlinfo',
    sa.Column('name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('mdlPath', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('bakPath', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('script', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('pubPath', mysql.VARCHAR(length=500), nullable=True),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('user')
    # ### end Alembic commands ###