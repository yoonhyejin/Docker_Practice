"""empty message

Revision ID: d7ad47ee78dd
Revises: 
Create Date: 2021-08-24 17:35:53.575511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd7ad47ee78dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Todo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Todo',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('text', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.drop_table('todo')
    # ### end Alembic commands ###
