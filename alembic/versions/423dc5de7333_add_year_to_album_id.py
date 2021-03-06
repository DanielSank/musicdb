"""Add year to Album id.

Revision ID: 423dc5de7333
Revises: 0c45be4e0b8a
Create Date: 2017-01-11 22:40:41.523910

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '423dc5de7333'
down_revision = '0c45be4e0b8a'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('albums', 'year',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.create_unique_constraint('name_year_uc', 'albums', ['name', 'year'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('name_year_uc', 'albums', type_='unique')
    op.alter_column('albums', 'year',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###
