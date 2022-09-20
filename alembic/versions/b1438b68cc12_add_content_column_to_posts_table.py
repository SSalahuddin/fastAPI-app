"""add content column to posts table

Revision ID: b1438b68cc12
Revises: a6960e8bbc20
Create Date: 2022-09-18 14:38:03.671903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1438b68cc12'
down_revision = 'a6960e8bbc20'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('postsORM', 
        sa.Column('content', sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_column('postsORM', 'content')
    pass
