"""empty message

Revision ID: 1cfb8da1920e
Revises: 37eec3066945
Create Date: 2022-01-25 18:07:56.292951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cfb8da1920e'
down_revision = '37eec3066945'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('mothername', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
