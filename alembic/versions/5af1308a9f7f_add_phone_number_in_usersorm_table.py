"""add phone number in usersORM table

Revision ID: 5af1308a9f7f
Revises: 1715271fff0a
Create Date: 2022-09-19 21:52:13.510225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5af1308a9f7f'
down_revision = '1715271fff0a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usersORM', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usersORM', 'phone_number')
    # ### end Alembic commands ###
