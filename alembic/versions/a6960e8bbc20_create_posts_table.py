"""create posts table

Revision ID: a6960e8bbc20
Revises: 
Create Date: 2022-09-18 14:34:25.518956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6960e8bbc20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('postsORM', 
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_table('postsORM')
    pass
