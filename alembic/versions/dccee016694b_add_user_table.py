"""add user table

Revision ID: dccee016694b
Revises: b1438b68cc12
Create Date: 2022-09-18 14:40:21.318872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dccee016694b'
down_revision = 'b1438b68cc12'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('usersORM', 
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_At', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')        
    )
    pass


def downgrade():
    op.drop_table('usersORM')
    pass
