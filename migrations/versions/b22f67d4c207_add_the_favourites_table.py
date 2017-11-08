"""add the favourites table

Revision ID: b22f67d4c207
Revises: 1a477fec1c0e
Create Date: 2017-11-08 15:28:38.734859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b22f67d4c207'
down_revision = '1a477fec1c0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favourites')
    # ### end Alembic commands ###
